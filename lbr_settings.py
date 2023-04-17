from API.data.users import User
from API.data.goods import Goods
from API.data import db_session

from Special.password_hash import password_encrypt, password_crypt
from Special.big_variables import user_values_dict

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types


db_session.global_init("API/db/all.db")
