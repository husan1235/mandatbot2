from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
modules = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="1 - Modul"),
        KeyboardButton(text="2 - Modul")
    ],

],
    resize_keyboard=True,
)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
modules2 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Modul - 1"),
        KeyboardButton(text="Modul - 2")
    ],

],
    resize_keyboard=True,
)