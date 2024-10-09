from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

async def create_keyboard(sonlar):
    keyb = ReplyKeyboardMarkup(resize_keyboard=True)
    for son in sonlar:
        keyb.insert(KeyboardButton(text=son))
    keyb.add(KeyboardButton(text="Ortga qaytish"))
    return keyb

def start_btn():
    btn1 = KeyboardButton(text="🏬  Yo'nalishlar bo'yicha")
    btn2 = KeyboardButton(text="📍Viloyat bo'yicha")
    btn3 = KeyboardButton(text="📊 To'plangan ball bo'yicha")
    btn4 = KeyboardButton(text="Mandat")
    btn5 = KeyboardButton(text="📄 Qo'llanma")
    btn7 = KeyboardButton(text="📚 Tushgan testlar")
    btn6 = KeyboardButton(text="📮 Tarjimon")
    btn8 = KeyboardButton(text="🔠 Natijalarni bilish")
    btn9 = KeyboardButton(text="📚 Test variyantlari")
    markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn6,btn9)
    markup.add(btn7)
    markup.add(btn8)
    markup.add(btn4, btn5)
    return markup

def ball_btn():
    btn1 = KeyboardButton(text="🏆 Grant")
    btn2 = KeyboardButton(text="📄 Kontrakt")
    btn3 = KeyboardButton(text="🔙 Orqaga")
    btn4 = KeyboardButton(text="🏠 Bosh menu")
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(btn1, btn2)
    # markup.add(btn2, btn3)
    markup.add(btn4)
    return markup

def bosh_btn():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn4 = KeyboardButton(text="🏠 Bosh menu")
    return markup.add(btn4)