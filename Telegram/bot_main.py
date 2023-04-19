from API.lbr import get_id, change_param, get_status, get_login, get_id_teleg, create_goods
from imp_control import *
import keyboards as kbs
from bot_funcs import *

# -----------------------------------------------------

token = '6130555686:AAHVqnlN6efSd3xASDtmTFmSxN82CaWXZTc'
bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())
# Объект бота


class AwaitMessages(StatesGroup):
    login = State()
    normal = State()
    not_allowed = State()
    goods_cost = State()
    goods_cost_2 = State()
    goods_des = State()
    goods_amo = State()


dp.middleware.setup(LoggingMiddleware())
# Включаем логирование
# -----------------------------------------------------


@dp.message_handler(content_types=['photo'], state=AwaitMessages.normal)
async def process_photo(message: types.Message):
    full_inf = []
    photo = message.photo[3]
    ID = get_id_teleg(message.from_user.id)[0]

    msg_text = f'Отличная фотография!\nЧтобы закончить загрузку товара, вам необходимо указать\n' \
               f'Название товара, категорию товара, описание и его количество.\n' \
               f'Введите название'
    await message.reply(msg_text)


    @dp.message_handler(state=AwaitMessages.normal)
    async def name_process(msg: types.Message):
        full_inf.append(msg.text)
        msg_text = f'Теперь выберите категорию, нажав на кнопку.'
        await msg.reply(msg_text, reply_markup=kbs.category_choose_menu)


    @dp.callback_query_handler(state=AwaitMessages.normal)
    async def cat_process(callback_query: types.CallbackQuery):
        full_inf.append(callback_query.data)
        msg_text = f'Опишите ваш товар'
        await bot.send_message(callback_query.from_user.id, msg_text)

        state = dp.current_state(user=callback_query.from_user.id)
        await state.set_state(AwaitMessages.goods_cost)


    @dp.message_handler(state=AwaitMessages.goods_cost)
    async def name_process(msg: types.Message):
        full_inf.append(msg.text)
        msg_text = f'Введите цену'
        await msg.reply(msg_text)
        state = dp.current_state(user=msg.from_user.id)
        await state.set_state(AwaitMessages.goods_des)


    @dp.message_handler(state=AwaitMessages.goods_cost_2)
    async def name_process(msg: types.Message):
        full_inf = full_inf[:-1]
        msg_text = f'Введите цену'
        state = dp.current_state(user=msg.from_user.id)
        await state.set_state(AwaitMessages.goods_des)
        await msg.reply(msg_text)


    @dp.message_handler(state=AwaitMessages.goods_des)
    async def name_process(msg: types.Message):
        try:
            full_inf.append(int(msg.text))
            msg_text = f'Осталось лишь ввести количество'
            state = dp.current_state(user=msg.from_user.id)
            await state.set_state(AwaitMessages.goods_amo)
        except:
            msg_text = f'Неккоректный ввод'
            await state.set_state(AwaitMessages.goods_cost_2)
        await msg.reply(msg_text)


    @dp.message_handler(state=AwaitMessages.goods_amo)
    async def name_process(msg: types.Message):
        try:
            full_inf.append(int(msg.text))
            msg_text = f'На этом всё!'
            state = dp.current_state(user=msg.from_user.id)
            create_goods(full_inf[0], ID, full_inf[1], full_inf[3], f'../static/photos/{full_inf[0]}.jpg', amount=full_inf[4], cost=full_inf[2])
            await state.set_state(AwaitMessages.normal)
            await photo.download(destination_file=f'../static/photos/{full_inf[0]}.jpg')
        except:
            msg_text = f'Неккоректный ввод'

        await msg.reply(msg_text)



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    state = dp.current_state(user=message.from_user.id)

    if get_id_teleg(message.from_user.id)[1] != 'usr':
        await state.set_state(AwaitMessages.normal)
        msg_text = f'С возвращением {get_login(get_id_teleg(message.from_user.id)[0])}!'
        await message.reply(msg_text)
        return None

    await state.set_state(AwaitMessages.login)

    msg_text = f'Здравствуйте {message.from_user.first_name}, чтобы пользоваться функционалом бота, ' \
               f'необходимо войти в свой аккаунт.\n' \
               f'Для этого введите ваш логин, email и пароль через пробел.\n' \
               f'При появлении вопросов воспользуйтесь командой /help'

    await message.reply(msg_text)


@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    msg_text = f'Этот бот создан для быстрого просмотра статистики продаж для продавцов.\nСписок команд:'

    await message.reply(msg_text)


@dp.callback_query_handler(text='help')
async def help_callback(callback_query: types.CallbackQuery):
    msg_text = f'Этот бот создан для быстрого просмотра статистики продаж для продавцов.\nСписок команд:'

    await bot.send_message(callback_query.from_user.id, msg_text)


@dp.message_handler(state=AwaitMessages.not_allowed)
async def not_allowed(message: types.Message):
    msg_text = 'Этот бот создан исключительно для продавцов.' \
               'Для продолжения работы здесь, вы должны сменить статус аккаунта'
    await message.reply(msg_text, reply_markup=kbs.not_allowed_menu)


@dp.message_handler(state=AwaitMessages.login)
async def login(message: types.Message):
    msg_text = ''

    state = dp.current_state(user=message.from_user.id)

    lep = message.text.split()
    try:
        ID = get_id(lep[0], lep[1], lep[2])

        if ID != 'Неверный пароль':
            msg_text = 'Вы успешно вошли в аккаунт!'

            await state.set_state(AwaitMessages.normal)

            if get_status(ID) == 'usr':
                msg_text = 'Этот бот создан для продавцов.' \
                           'Для продолжения работы здесь, вы должны сменить статус аккаунта'
                await state.set_state(AwaitMessages.not_allowed)
            else:
                change_param(ID, 5, message.from_user.id)
        else:
            msg_text = 'Введённые данные некорректны, попробуйте ещё раз.'

    except IndexError:
        msg_text = 'Введённые данные некорректны, попробуйте ещё раз.'

    if msg_text != '':
        await message.reply(msg_text)


@dp.message_handler()
async def process_photo(message: types.Message):
    print(message.content_type)

if __name__ == '__main__':
    executor.start_polling(dp)
