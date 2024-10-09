from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Sinflar = ReplyKeyboardMarkup(resize_keyboard=True)

sonlar = range(5, 12)
for son in sonlar:
    button = KeyboardButton(text=f"{son} - sinf")
    Sinflar.insert(button)
Sinflar.insert(KeyboardButton(text="Ortga qaytish"))


