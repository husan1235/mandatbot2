from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from sql.func import post_sql_query


def pagination_btn(key, ball, c, b):
    markup = InlineKeyboardMarkup(row_width=5)
    a = []
    i = 1
    for x in key:
        a.append(InlineKeyboardButton(i, callback_data=f"infoID={x}"))
        i = i + 1
    btn1 = InlineKeyboardButton('⬅️', callback_data=f'back={ball}={c}={b}')
    btn2 = InlineKeyboardButton('➡️', callback_data=f'next={ball}={c}={b}')
    markup.add(*a)
    markup.add(btn1, btn2)
    return markup
    
give = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🕹 Yuklash",url="https://telegra.ph/Abituriyentlar-ruxsatnomasini-olish-07-29")
    ]
])

def Vpagination_btn(key, c, n):
    markup = InlineKeyboardMarkup(row_width=5)
    a = []
    i = 1
    for x in key:
        a.append(InlineKeyboardButton(i, callback_data=f"univerID={x}"))
        i = i + 1
    # btn1 = InlineKeyboardButton('⬅️', callback_data=f'vback={c}={n}')
    # btn2 = InlineKeyboardButton('➡️', callback_data=f'vnext={c}={n}')
    markup.add(*a)
    # markup.add(btn1, btn2)
    return markup

def Opagination_btn(key, c, n):
    markup = InlineKeyboardMarkup(row_width=5)
    a = []
    i = 1
    for x in key:
        a.append(InlineKeyboardButton(i, callback_data=f"infoID={x}"))
        i = i + 1
    btn1 = InlineKeyboardButton('⬅️', callback_data=f'Oback={c}={n}')
    btn2 = InlineKeyboardButton('➡️', callback_data=f'Onext={c}={n}')
    markup.add(*a)
    markup.add(btn1, btn2)
    return markup

def Ypagination_btn(key, key2):
    markup = InlineKeyboardMarkup(row_width=2)
    a = []
    i = 1
    for x, y in zip(key, key2):
        a.append(InlineKeyboardButton(x, callback_data=f"infoID={y}"))
        i = i + 1
    markup.add(*a)
    return markup

def langs_btn(key, key2, otmID):
    markup = InlineKeyboardMarkup(row_width=3)
    a = []
    for x, y in zip(key, key2):
        a.append(InlineKeyboardButton(x, callback_data=f"lanOTM#{y}#{otmID}"))
    markup.add(*a)
    return markup

def types_btn(key, key2, otmID, lan):
    markup = InlineKeyboardMarkup(row_width=3)
    a = []
    for x, y in zip(key, key2):
        a.append(InlineKeyboardButton(x, callback_data=f"typesOTM#{y}#{otmID}#{lan}"))
    markup.add(*a)
    return markup

def oblats_btn():
    l = ['Andijon viloyati', 'Toshkent shahri', 'Buxoro viloyati', 'Fargʻona viloyati', 'Sirdaryo viloyati', 'Samarqand viloyati', 'Jizzax viloyati', 'Namangan viloyati', 'Navoiy viloyati', 'Qoraqalpog‘iston Respublikasi', 'Qashqadaryo viloyati', 'Xorazm viloyati', 'Toshkent viloyati', 'Surxondaryo viloyati']
    markup = InlineKeyboardMarkup(row_width=2   )
    g = []
    for x in l:
        g.append(InlineKeyboardButton(x, callback_data=f"hudud={x}"))
    return markup.add(*g)

def Yoblats_btn(lis, lisID):
    markup = InlineKeyboardMarkup(row_width=2)
    g = []
    for x, y in zip(lis, lisID):
        g.append(InlineKeyboardButton(x, callback_data=f"yoblas={y}"))
    return markup.add(*g)

def send_btn():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('➕Add channel', callback_data='addcha'))
    markup.add(InlineKeyboardButton('➖del channel', callback_data='delchan'))
    markup.add(InlineKeyboardButton('Send Message', callback_data='msg'))
    markup.add(InlineKeyboardButton('Send Forward', callback_data='forward'))
    return markup

def can_btn():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('cancel', callback_data='cancel'))
    return markup

def channelbtn():
    us = post_sql_query("SELECT * FROM CHANNELS")
    markup = InlineKeyboardMarkup(row_width=2)
    i = 0
    for r in us:
        i +=1
        r1 = r[1].replace('@', '')
        r1 = 'https://t.me/' + r1
        btn = InlineKeyboardButton(text=f"{r[2]}", url=r1)
        btnn = InlineKeyboardButton('❌', callback_data=f'kanaldel={r[0]}')
        markup.add(btn, btnn)
    return markup

def channel_btn():
    us = post_sql_query("SELECT * FROM CHANNELS")
    markup = InlineKeyboardMarkup(row_width=2)
    i = 0
    for r in us:
        i +=1
        r1 = r[1].replace('@', '')
        r1 = 'https://t.me/' + r1
        btn = InlineKeyboardButton(text=f"{i}- kanalga a'zo bo'ling", url=r1)
        markup.add(btn)
    btn2 = InlineKeyboardButton('🔔 Tekshirish ', callback_data='chek')
    markup.add(btn2)
    return markup

def switch_btn():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔎Qidiruv", switch_inline_query_current_chat=""))
    return markup

def help_btn():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📄 Qo'llanmani o'qish", url="https://telegra.ph/Mandatlar-2022-botdan-foydalanish-qo%CA%BBllanmasi-03-23-2"))
    return markup