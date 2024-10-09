from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import btns
fanlar = ["Matematika(2020)","Fizika 2019","Fizika 2020","Kimyo 2019","Biologiya 2020","Matematika (5-11)","Ona tili (5-11)"]
blok = ReplyKeyboardMarkup(resize_keyboard=True,)

for fan in fanlar:
    button = KeyboardButton(text=fan)
    blok.insert(button)
blok.add(KeyboardButton(text="Ortga qaytish"))