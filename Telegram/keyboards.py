from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
import unicodedata


cite_btn = InlineKeyboardButton('Наш сайт', url='https://www.google.ru/')
help_btn = InlineKeyboardButton('Помощь', callback_data='help')

not_allowed_menu = InlineKeyboardMarkup(row_width=2)
not_allowed_menu.add(cite_btn, help_btn)
