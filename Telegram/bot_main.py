from API.lbr import get_id, change_param, get_status
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
# Диспетчер для бота


dp.middleware.setup(LoggingMiddleware())
# Включаем логирование
# -----------------------------------------------------


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
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
    global ID_db

    state = dp.current_state(user=message.from_user.id)

    lep = message.text.split()
    ID_db = get_id(lep[0], lep[1], lep[2])

    if ID_db != 'Неверный пароль':
        msg_text = 'Вы успешно вошли в аккаунт!'
        change_param(ID_db, 5, message.from_user.id)

        await state.set_state(AwaitMessages.normal)

        if get_status(ID_db) == 'usr':
            msg_text = 'Этот бот создан для продавцов. Для продолжения работы здесь, вы должны сменить статус аккаунта'
            await state.set_state(AwaitMessages.not_allowed)
    else:
        msg_text = 'Введённые данные некорректны, попробуйте ещё раз.'

    await message.reply(msg_text)


if __name__ == '__main__':
    executor.start_polling(dp)
