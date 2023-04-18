from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
import unicodedata
import emoji


cite_btn = InlineKeyboardButton('Наш сайт', url='https://www.google.ru/')
help_btn = InlineKeyboardButton('Помощь', callback_data='help')

not_allowed_menu = InlineKeyboardMarkup(row_width=2)
not_allowed_menu.add(cite_btn, help_btn)

meat_btn = InlineKeyboardButton('Мясо 🍖', callback_data='meat')
milk_btn = InlineKeyboardButton('Молочная продукция🥛', callback_data='milk')
vege_btn = InlineKeyboardButton('Овощи 🍅', callback_data='vege')
anim_btn = InlineKeyboardButton('Для животных 🐶', callback_data='anim')
fish_btn = InlineKeyboardButton('Рыба 🐟', callback_data='fish')
kosm_btn = InlineKeyboardButton('Косметика💄', callback_data='kosm')

category_choose_menu = InlineKeyboardMarkup(row_width=2)
category_choose_menu.add(meat_btn, milk_btn, vege_btn, anim_btn, fish_btn, kosm_btn)
