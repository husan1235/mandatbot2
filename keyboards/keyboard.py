from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import btns

async def create_keyboard(sonlar):
    keyb = ReplyKeyboardMarkup(resize_keyboard=True)
    for son in sonlar:
        keyb.insert(KeyboardButton(text=son))
    keyb.add(KeyboardButton(text="Ortga qaytish"))
    return keyb


mainM = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text=btns["new_test"]),
        KeyboardButton(text=btns["result"])
    ],
    [
        KeyboardButton(text=btns["dtm_news"]),
        KeyboardButton(text=btns["video_instruction"])
    ],
    [
        KeyboardButton(text="📹 Video darslar"),
        KeyboardButton(text="🥇 Sertifikat olish")
    ],
    [
        KeyboardButton(text="📮 Tarjimon")
    ]
],
    resize_keyboard=True,
)

back = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Ortga qaytish")
    ],

],
    resize_keyboard=True,
)

test = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text=btns["in_uzbek"]),
        KeyboardButton(text=btns["in_russian"])
    ],
    [
        KeyboardButton(text=btns["blokli"]),
        KeyboardButton(text="📑 Majburiy fanlardan testlar")
    ],
    [
        KeyboardButton(text="📚 Tushgan testlar")
    ],
    [
        KeyboardButton(text=btns["back"])
    ]

],
    resize_keyboard=True,
)

uzbek = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="MATEMATIKA"),
        KeyboardButton(text="FIZIKA")
    ],
    [
        KeyboardButton(text="BIOLOGIYA"),
        KeyboardButton(text="KIMYO")
    ],
    [
        KeyboardButton(text="ONA TILI"),
        KeyboardButton(text="TARIX")
    ],
    [
        KeyboardButton(text="INGLIZ TILI"),
        KeyboardButton(text="GEOGRAFIYA"),

    ],
    [
        KeyboardButton(text="NEMIS TILI"),
        KeyboardButton(text="FRANSUZ TILI")
    ],
    [
        KeyboardButton(text=btns["back"])
    ]

],
    resize_keyboard=True,
)

rus = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="МАТЕМАТИКА"),
        KeyboardButton(text="ХИМИЯ")
    ],
    [
        KeyboardButton(text="БИОЛОГИЯ"),
        KeyboardButton(text="ФИЗИКА")
    ],
    [
        KeyboardButton(text="ИСТОРИЯ"),
        KeyboardButton(text="РУССКИЙ ЯЗЫК")
    ],
    [
        KeyboardButton(text="ГЕОГРАФИЯ"),
        KeyboardButton(text="АНГЛИЙСКИЙ ЯЗЫК"),

    ],
    [
        KeyboardButton(text="НЕМЕЦКИЙ ЯЗЫК"),
        KeyboardButton(text="ФРАНЦУЗСКИЙ ЯЗЫК"),

    ],
    [
        KeyboardButton(text=btns["back"])
    ],
],
    resize_keyboard=True,
)
