from lbr_settings import *
from API.lbr import get_id


# -----------------------------------------------------

token = '6130555686:AAHVqnlN6efSd3xASDtmTFmSxN82CaWXZTc'
bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())
# Объект бота


class AwaitMessages(StatesGroup):
    login = State()
    normal = State()
# Диспетчер для бота


dp.middleware.setup(LoggingMiddleware())
# Включаем логирование
# -----------------------------------------------------


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(AwaitMessages.login)

    msg_text = f'Здравствуйте, чтобы пользоваться функционалом бота, необходимо войти в свой аккаунт.\n' \
               f'Для этого введите ваш логин, email и пароль через пробел.'

    await message.reply(msg_text)


@dp.message_handler(state=AwaitMessages.login)
async def crit(message: types.Message):
    lep = message.text.split()
    print(get_id(lep[0], lep[1], lep[2]))


if __name__ == '__main__':
    executor.start_polling(dp)
