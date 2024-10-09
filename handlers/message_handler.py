from datetime import datetime

from config import bot, dp, texts, btns
from aiogram.types import Message, CallbackQuery, InlineQuery
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from filter.admin import AdminFilter
from keyboards.Sinflar import Sinflar
from keyboards.blok import blok
from keyboards.keyboard import back
from sql.checker import compare
from sql.func import register_user, channel_ids, post_sql_query, get_user_data, Unblock, add_test, delete_tests, \
    select_test_all
from sql import func
from keyboards.InlineKeyboard import Vpagination_btn, channel_btn, oblats_btn, switch_btn, pagination_btn, \
    Ypagination_btn, Yoblats_btn, langs_btn, types_btn, Opagination_btn, help_btn, give
from keyboards.ReplyKeyboard import start_btn, ball_btn, bosh_btn, create_keyboard
import re
from messages import lan
import os
import bsp
from testlar.javoblar import javoblar
from .ball import get_ball

step, lin, grant = {}, {}, {}
import requests
from bs4 import BeautifulSoup


class Steps(StatesGroup):
    search = State()
    grant = State()
    kontrakt = State()


cesh = {}
search = {}


def numbers(s):
    return int(re.search(r"\d+", s).group(0))


async def pogin(msg, ball, a, name, typ):
    try:
        print(name)
        if name == 'kontr': fid = 5
        if name == 'grant': fid = 4
        print(ball)
        listID = []
        txt = ""
        i = 1
        for x in func.OTM(name, a, ball):
            listID.append(x[0])
            intt = numbers(x[2])
            get = str(x[2]).replace(f"{intt}", "")
            txt += f"{i}.{get}|{x[fid]}B\n"
            i += 1
        get = func.OTMCOUNT(name, ball)
        get2 = step.get('maqtaw')
        if get != 0 and get2 == msg.from_user.id:
            await msg.answer("🤓Bilimdon ekansiz {} ball bilan {}ta oliygohga kirasiz".format(ball, get))
        if typ == None:
            await msg.answer(f"*{txt}*", 'markdown', reply_markup=pagination_btn(key=listID, ball=ball, c=a, b=name))
        else:
            await msg.edit_text(f"*{txt}*", 'markdown', reply_markup=pagination_btn(key=listID, ball=ball, c=a, b=name))
        cesh.clear()
    except Exception as err:
        print(err)
        await msg.answer('*🤷🏻‍♂️ Bunday ma\'lumot yo\'q\nSaralash uchun ballni kiriting:*', 'markdown')


async def Vpogin(msg, v, a):
    try:
        print('Vpogin')
        b = a
        listID = []
        nam = []
        txt = ""
        i = 0
        print(v)
        for x in func.Votm(str(v), b):
            if x[1] not in nam:
                i += 1
                print(x[1])
                nam.append(x[1])
                listID.append(x[0])
                txt += f"{i}.{x[1]}\n"
        await msg.edit_text(f"*{txt}*", 'markdown', reply_markup=Vpagination_btn(listID, b, v))
        cesh.clear()
    except Exception as err:
        print(err)
        await msg.answer('*ma\'lumot topilmadi*', 'markdown')


async def Ypogin(msg, text):
    try:
        get = func.Fotm(text)
        if get[0] != []:
            await msg.answer(f"*viloyotlar*", 'markdown', reply_markup=Ypagination_btn(get[0], get[1]))
            cesh.clear()
        else:
            await msg.answer('*ma\'lumot topilmadi*', 'markdown', reply_markup=bosh_btn())
    except Exception as err:
        print(err)
        await msg.answer('*ma\'lumot topilmadi*', 'markdown', reply_markup=bosh_btn())


async def joinChan(bot, msg):
    resut = []
    for x in channel_ids():
        g = await bot.get_chat_member(x, msg.from_user.id)
        resut.append(g.status)
    if 'left' in resut:
        await bot.send_message(msg.from_user.id,
                               f"Assalomu alaykum {msg.from_user.first_name}. Botni ishga tushurish uchun kanallarga a'zo bo'ling va a'zolikni tekshirish buyrug'ini bosing.",
                               reply_markup=channel_btn())
    else:
        return True


@dp.callback_query_handler(text='chek')
async def chanellstatuschek(call: CallbackQuery):
    resut = []
    for x in channel_ids():
        g = await bot.get_chat_member(x, call.from_user.id)
        resut.append(g.status)
    if 'left' in resut:
        await call.answer("iltimos kanallarga a'zo bo'ling!", cache_time="1")
    else:
        await call.message.delete()
        await call.message.answer(lan.get('start'), parse_mode='html', reply_markup=start_btn())


@dp.message_handler(text=['🏠 Bosh menu', '/start'], state='*')
async def hello(msg: Message, state: FSMContext):
    res = get_user_data(user=msg.from_user.id)
    try:
        if msg.from_user.id in res[0]:
            Unblock(cid=msg.from_user.id)

    except:
        register_user(msg.from_user.id, msg.from_user.username, first_name=msg.from_user.first_name,
                      last_name=msg.from_user.last_name)
    if await joinChan(bot, msg) == True:
        await state.finish()
        await msg.reply(lan.get('start'), 'html', reply_markup=start_btn())


@dp.message_handler(text="📊 To'plangan ball bo'yicha")
async def ballyetadi(msg: Message):
    if await joinChan(bot, msg) == True:
        await msg.answer("O'quv turini tanlang 👇", reply_markup=ball_btn())


@dp.message_handler(text='🏆 Grant')
async def grantball(msg: Message):
    if await joinChan(bot, msg) == True:
        await Steps.grant.set()
        await msg.answer("Saralash uchun ballni kiriting:")


@dp.message_handler(text="📄 Kontrakt")
async def KrontFun(msg: Message):
    if await joinChan(bot, msg) == True:
        await Steps.kontrakt.set()
        await msg.reply("Saralash uchun ballni kiriting:")


@dp.message_handler(text="📍Viloyat bo'yicha")
async def OtishBall(msg: Message):
    if await joinChan(bot, msg) == True:
        await msg.answer("📍 Hududni tanlang:", reply_markup=oblats_btn())


@dp.message_handler(text="🏬  Yo'nalishlar bo'yicha")
async def Yonalsh(msg: Message):
    if await joinChan(bot, msg) == True:
        await Steps.search.set()
        await msg.answer("Tezkor qidiruvdan foydalaning...", reply_markup=switch_btn())
        await msg.reply("📚 Ta'lim yo'nalishini turini yozing...",
                        'html', reply_markup=bosh_btn())


@dp.message_handler(text='Mandat')
async def MandatFunc(msg: Message):
    if await joinChan(bot, msg) == True:
        await msg.reply('Bu bo\'lim mandat natijasi chiqqanda ishlaydi😅')


@dp.message_handler(text='📄 Qo\'llanma')
async def HelpFunc(msg: Message):
    if await joinChan(bot, msg) == True:
        await msg.reply("Botdan qanday foydalanishni bilish uchun pa'stdagi tugmani bosing:", reply_markup=help_btn())


@dp.message_handler(text="Abituriyent ruxsatnomasini yuklab olish")
async def send(msg: types.Message):
    await msg.answer(
        "👨🏻‍💻 Abituriyentlar test sinovlarida ishtirok etish uchun “Abituriyent ruxsatnomasi”ni my.dtm.uz saytiga shaxsiy identifikatsiya raqami hamda pasport seriyasi va raqamini kiritgan holda olishlari mumkin.\n\n📥 Shuningdek, ruxsatnomani Davlat test markazining quyidagi maxsus telegram botlari orqali ham yuklab olish imkoniyati mavjud:\n\n👉 @e_dtm_mandatbot\n👉 @e_dtm_mandat1bot\n👉 @e_dtm_mandat2bot\n👉 @e_dtm_mandat3bot\n👉 @e_dtm_mandat4bot\n\n📆 Test sinovlari 8-avgustdan boshlanishini inobatga olgan holda abituriyentlardan ruxsatnomalarni 7-avgustga qadar yuklab olishlarini so‘raymiz.\n\n📌 Eslatib o‘tamiz, abituriyentlar test sinovlariga pasport (ID-karta) va abituriyent ruxsatnomasi bilan kelishlari lozim.")


# steplar
@dp.message_handler(state=Steps.search)
async def searchFUNC(msg: Message, state: FSMContext):
    print('YOZADI')
    try:
        get = func.Fotm(msg.text)
        print("viloyatlar: " + str(get[0]))
        if get[0] != []:
            await msg.answer(f"*viloyotlar*", 'markdown', reply_markup=Ypagination_btn(get[0], get[1]))
            await state.finish()
        else:
            await msg.answer('*ma\'lumot topilmadi*', 'markdown', reply_markup=bosh_btn())
    except Exception as err:
        print(err)
        await msg.answer('*ma\'lumot topilmadi*', 'markdown', reply_markup=bosh_btn())


@dp.message_handler(state=Steps.grant)
async def GrantBall(msg: Message, state: FSMContext):
    try:
        ball = float(msg.text)
        st = step.update({'maqtaw': msg.from_user.id})
        await pogin(msg, ball, 0, name='grant', typ=None)
        await state.finish()
    except:
        await msg.answer('*🤷🏻‍♂️ Bunday ma\'lumot yo\'q\nSaralash uchun ballni kiriting:*', 'markdown',
                         reply_markup=bosh_btn())


@dp.message_handler(state=Steps.kontrakt)
async def KontrBall(msg: Message, state: FSMContext):
    try:
        ball = float(msg.text)
        st = step.update({'maqtaw': msg.from_user.id})
        await pogin(msg, ball, 0, name='kontr', typ=None)
        await state.finish()
    except:
        await msg.answer('*🤷🏻‍♂️ Bunday ma\'lumot yo\'q\nSaralash uchun ballni kiriting:*', 'markdown',
                         reply_markup=bosh_btn())


@dp.callback_query_handler(lambda call: call.data.split('=')[0] == 'hudud')
async def hududCall(call: CallbackQuery):
    print('hudud')
    await call.answer()
    await Vpogin(call.message, call.data.split('=')[1], 0)


# 📍Viloyat bo'yicha->Viloyat->OTM->Yonalish->next and back
@dp.callback_query_handler(lambda call: call.data.split('=')[0] == 'Onext')
async def OOnext(call: CallbackQuery):
    print('OOnext')
    try:
        await call.answer()
        x = str(call.data).split("=")
        print(x[1])
        b, otm = int(x[1]) + 10, x[2]
        if b >= 0:
            get = func.V_to_Yotm(otm, b)
            i = 1
            txt = ""
            if len(get[0]) != 0:
                for x in get[0]:
                    txt += f"*{i}.{x}*\n"
                    i += 1
                await call.message.edit_text(txt, 'markdown', reply_markup=Opagination_btn(get[1], b, otm))
        else:
            await call.answer("Malumot topilmadi")
    except Exception as err:
        await call.answer("Malumot topilmadi")
        print(err)


@dp.callback_query_handler(lambda call: call.data.split('=')[0] == 'Oback')
async def OOBacl(call: CallbackQuery):
    print('OOBack')
    try:
        await call.answer()
        x = str(call.data).split("=")
        print(x[1])
        b, otm = int(x[1]) - 10, x[2]
        if b >= 0:
            get = func.V_to_Yotm(otm, b)
            i = 1
            txt = ""
            if len(get[0]) != 0:
                for x in get[0]:
                    txt += f"*{i}.{x}*\n"
                    i += 1
                await call.message.edit_text(txt, 'markdown', reply_markup=Opagination_btn(get[1], b, otm))
        else:
            await call.answer(text="Malumot topilmadi")
    except Exception as err:
        print(err)
        await call.answer("Malumot topilmadi")


# 📍Viloyat bo'yicha->Viloyat->OTM->Yonalish->next and back


# grant or kontrant next and back
@dp.callback_query_handler(lambda call: call.data.split('=')[0] == 'next')
async def nextFUnN(call: types.CallbackQuery):
    print('next')
    await call.answer()
    x = str(call.data).split("=")
    ball, a, name = x[1], x[2], x[3]
    await pogin(call.message, float(ball), int(a) + 10, name=name, typ='ok')


@dp.callback_query_handler(lambda call: call.data.split('=')[0] == 'back')
async def nextFUnN(call: types.CallbackQuery):
    print('next')
    await call.answer()
    x = str(call.data).split("=")
    ball, a, name = x[1], x[2], x[3]
    await pogin(call.message, float(ball), int(a) - 10, name=name, typ='ok')


# end grant or kontrant next and back


@dp.callback_query_handler(lambda call: call.data.split('=')[0] == 'univerID')
async def univer_to_yonalish(call: types.CallbackQuery):
    print('univerID')
    await call.answer()
    otm = call.data.split('=')[1]
    get = func.V_to_Yotm(otm, 0)
    print(get)
    txt = ""
    i = 1
    for x in get[0]:
        txt += f"*{i}.{x}*\n"
        i += 1
    await call.message.edit_text(txt, 'markdown', reply_markup=Opagination_btn(get[1], 0, otm))


@dp.callback_query_handler(lambda call: call.data.split('=')[0] == 'infoID')
async def characters_page_callback(call: types.CallbackQuery):
    print('infoID')
    await call.answer()
    otm = func.infoOTM(call.data.split('=')[1])[0]
    url = otm[6]
    k = str(otm[3]).split('/')
    txt = '''🏛 OLIYGOH: *{}*

📚 TAʼLIM YO‘NALISHI - *{}*

🇺🇿 TAʼLIM TILI - *{}*

🔰 TAʼLIM SHAKLI - Kunduzgi

🔄 QABUL KVOTASI: *{}* ta
Grant - *{}* ta | Kontrakt - *{}* ta

📈 OʻTISH BALLARI:
 Grant - *{}* ball | Kontrakt - *{}* ball
'''.format(otm[1], otm[2], 'uzbek', k[0], k[1], k[2], otm[4], otm[5])
    get = bsp.langs(url)
    print(get[0])
    print(get[1])
    try:
        await call.message.answer_photo(otm[7], txt, 'markdown', reply_markup=langs_btn(get[0], get[1], otm[0]))
    except:
        await call.message.answer(txt, 'markdown', reply_markup=langs_btn(get[0], get[1], otm[0]))


@dp.callback_query_handler(lambda call: call.data.split('#')[0] == 'lanOTM')
async def LangInfo(call: types.CallbackQuery):
    ex = call.data.split("#")
    lan, otmID = ex[1], ex[2]
    otm = func.infoOTM(otmID)[0]
    link = str(otm[6]).replace("?lang=uz", f"?lang={lan}")
    for_types = bsp.langs(link)
    try:
        INFO = bsp.INFOY(link, otm[2])
        kv = str(INFO[1]).split('/')
        txt = '''🏛 OLIYGOH: *{}*

📚 TAʼLIM YO‘NALISHI - *{}*

🇺🇿 TAʼLIM TILI - *{}*

🔰 TAʼLIM SHAKLI - Kunduzgi

🔄 QABUL KVOTASI: *{}* ta
Grant - *{}* ta | Kontrakt - *{}* ta

📈 OʻTISH BALLARI:
Grant - *{}* ball | Kontrakt - *{}* ball
    '''.format(otm[1], otm[2], lan, kv[0], kv[1], kv[2], INFO[3], INFO[2])
        try:
            print(lan)
            await call.message.answer_photo(INFO[4], txt, 'markdown',
                                            reply_markup=types_btn(for_types[2], for_types[2], otmID, lan))
        except:
            await call.message.answer(txt, 'markdown',
                                      reply_markup=types_btn(for_types[2], for_types[2], otmID, lan))
    except:
        await call.answer('Malumot Topilmadi')


@dp.callback_query_handler(lambda call: call.data.split('#')[0] == 'typesOTM')
async def typeFilter(call: CallbackQuery):
    ex = call.data.split("#")
    print(ex)
    types, otmID, lan = ex[1], ex[2], ex[3]
    otm = func.infoOTM(otmID)[0]
    lin1 = str(otm[6]).split('https://abt.uz/university/')
    lin = f"view?slug={lin1[1]}"
    lann = str(lin).replace("?lang=uz", f"&lang={lan}")
    link = f"https://abt.uz/university/{lann}&type={str(types).lower()}"
    ''''
    primer:
    https://abt.uz/university/qoraqalpoq-davlat-universiteti?lang=kk&type=Sirtqi
    https://abt.uz/university/view?slug=qoraqalpoq-davlat-universiteti&lang=kk&type=sirtqi
    https://abt.uz/university/view?slug=qoraqalpoq-davlat-universiteti&lang=kk&type=sirtqi
    https://abt.uz/university/view?slug=qoraqalpoq-davlat-universiteti&lang=kk&type=Sirtqi
    '''
    try:
        INFO = bsp.INFOY(link, otm[2])
        kv = str(INFO[1]).split('/')
        txt = '''🏛 OLIYGOH: *{}*

📚 TAʼLIM YO‘NALISHI - *{}*

🇺🇿 TAʼLIM TILI - *{}*

🔰 TAʼLIM SHAKLI - *{}*

🔄 QABUL KVOTASI: *{}* ta
Grant - *{}* ta | Kontrakt - *{}* ta

📈 OʻTISH BALLARI:
Grant - *{}* ball | Kontrakt - *{}* ball
    '''.format(otm[1], otm[2], lan, types, kv[0], kv[1], kv[2], INFO[3], INFO[2])
        print(txt)
        try:
            print(lan)
            await call.message.answer_photo(INFO[4], txt, 'markdown',
                                            reply_markup=bosh_btn())
        except:
            await call.message.answer(txt, 'markdown',
                                      reply_markup=bosh_btn())
    except:
        await call.answer("Malumot topilmadi")


@dp.inline_handler(lambda inline_query: True, state='*')  # Обработчик любых инлайн-запросов
async def inline(query: InlineQuery):
    text = query.query or None
    print(text)
    offset = int(query.offset) if query.offset else 1

    items = []
    lis = []
    i = 0
    if text:
        post = post_sql_query(f"SELECT yonalish FROM OTM WHERE yonalish LIKE '%{text}%' LIMIT 0, 50")
        for b in post:
            nonumtext = " ".join(str(b[0]).split()[:-1])
            tt = re.sub(r'\([^)]*\)', "", nonumtext)
            if tt not in lis:
                print(tt)
                lis.append(tt)
        for tt in lis[:50]:
            items.append(
                types.InlineQueryResultArticle(
                    id=str(offset + i),
                    title=f"{tt}",
                    input_message_content=types.InputTextMessageContent(
                        message_text=f"{tt}",
                    )
                )
            )
            i = i + 1
        await query.answer(items, is_personal=True, cache_time=0)
    if text == None:
        for b in post_sql_query("SELECT yonalish FROM OTM"):
            nonumtext = " ".join(str(b[0]).split()[:-1])
            tt = re.sub(r'\([^)]*\)', "", nonumtext)
            if tt not in lis:
                lis.append(tt)
        for tt in lis[:50]:
            items.append(
                types.InlineQueryResultArticle(
                    id=str(offset + i),
                    title=f"{tt}",
                    input_message_content=types.InputTextMessageContent(
                        message_text=f"{tt}",
                    )
                )
            )
            i = i + 1

        await query.answer(items, is_personal=True, cache_time=0)
    # await query.answer(items2, next_offset="2", cache_time=1)
    # await query.answer(items3, next_offset="1", cache_time=1)
    # print(lis)


@dp.message_handler(AdminFilter(), text="/add_test")
async def welcome(msg: types.Message, state: FSMContext):
    await msg.answer("Testlarni yuboring")
    await state.set_state("add_test")


@dp.message_handler(AdminFilter(), state="add_test", text="/finish")
async def welcome(msg: types.Message, state: FSMContext):
    await msg.answer("Tayyor")
    await state.finish()


@dp.message_handler(AdminFilter(), state="add_test", content_types=types.ContentType.ANY)
async def welcome(msg: types.Message, state: FSMContext):
    add_test(fmid=msg.chat.id, mid=msg.message_id)
    await msg.answer("Qoshildi")


@dp.message_handler(AdminFilter(), text="/clear")
async def welcome(msg: types.Message, state: FSMContext):
    delete_tests()
    await msg.answer("Testlar tozalandi")


@dp.message_handler(text="📚 Tushgan testlar")
async def welcome(msg: types.Message, state: FSMContext):
    t = select_test_all()
    array = []
    son = len(t)
    if son == 0:
        await msg.answer("Bu bo'lim hali bo'sh")
    else:
        longness = range(1, son + 1)
        for long in longness:
            array.append(long)
        key = await create_keyboard(array)
        await msg.answer("Kerakli sonni tanlang", reply_markup=key)
        await state.set_state("test_yubor")


@dp.message_handler(state="test_yubor", text="Ortga qaytish")
async def welcome(msg: types.Message, state: FSMContext):
    await msg.answer("Kerakli menyuni tanlang", reply_markup=start_btn())
    await state.finish()


@dp.message_handler(state="test_yubor")
async def welcome(msg: types.Message, state: FSMContext):
    try:
        test = select_test_all()
        num = int(msg.text) - 1
        await bot.copy_message(chat_id=msg.from_user.id, from_chat_id=test[num][0], message_id=test[num][1])
    except:
        await msg.answer("Xatolik yuz berdi kutib turing")


@dp.message_handler(text="📈 To'plagan balini bilish")
async def welcome(msg: types.Message, state: FSMContext):
    await msg.answer_photo("https://t.me/testiszlar/238", caption="*Namunaga binoan ID raqamingizni kiriting*",
                           parse_mode="markdown")
    await state.set_state("ball")


@dp.message_handler(state="ball")
async def test(msg: types.Message, state: FSMContext):
    array = []
    try:
        url = f"https://mandat.dtm.uz/Home2022/AfterFilter?name={msg.text}"
        rawdata = requests.get(url)
        html = rawdata.content
        soup = BeautifulSoup(html, 'html.parser')
        tr = soup.find_all('td')
        array = []
        for t in tr:
            text = t.text
            array.append(text)
        print(array)
        await msg.answer(f"Sizning ismingiz : {array[1]}\nSizning to'plagan balingiz : {array[4]}")
        await state.finish()
    except:
        print(array)
        await msg.answer("Xatolik yuz berdi birozdan so'ng urinib ko'ring")
        await state.finish()

        # Translate


from PIL import Image
from aiogram import types
from aiogram.types.base import InputFile
from googletrans import Translator
from pytesseract import pytesseract

from keyboards import keyboard, modules
from config import dp, bot
from aiogram.dispatcher import FSMContext
from deep_translator import GoogleTranslator
from handlers.translate_image import translate_image


@dp.message_handler(text="📮 Tarjimon")
async def new_test_handler(msg: types.Message):
    await msg.answer("Salom qaysi tilga tarjima qilmoqchisiz marhamat tanlang :\n\n/uzen - O'zbek tilidan ingliz "
                     "tiliga\n/enuz - Ingliz tilidan o'zbek tiliga tarjima qilish\n/uzru - O'zbek tilidan rus tiliga "
                     "tarjima qilish\n/ruuz - Rus tilidan o'zbek tiliga tarjima qilish\n\nO'zingizga kerakli "
                     "komandani menga jo'nating")


@dp.message_handler(text="Ortga qaytish", state=["uzen", "enuz", "uzru", "ruuz","result"])
async def in_russian_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Siz asosiy menyuga qaytdingiz", reply_markup=start_btn())
    await state.finish()


@dp.message_handler(text="/uzen")
async def in_russian_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Rasm yoki matn yuboring..", reply_markup=keyboard.back)
    await state.set_state("uzen")


@dp.message_handler(text="/enuz")
async def in_russian_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Rasm yoki matn yuboring..", reply_markup=keyboard.back)
    await state.set_state("enuz")


@dp.message_handler(text="/uzru")
async def in_russian_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Rasm yoki matn yuboring..", reply_markup=keyboard.back)
    await state.set_state("uzru")


@dp.message_handler(text="/ruuz")
async def in_russian_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Rasm yoki matn yuboring..", reply_markup=keyboard.back)
    await state.set_state("ruuz")


@dp.message_handler(state="uzen")
async def enuz(msg: types.Message):
    to_translate = msg.text
    translated = GoogleTranslator(source='auto', target='en').translate(to_translate)
    await msg.answer(translated)


@dp.message_handler(state="enuz")
async def enuz(msg: types.Message):
    to_translate = msg.text
    translated = GoogleTranslator(source='auto', target='uz').translate(to_translate)
    await msg.answer(translated)


@dp.message_handler(state="enuz", content_types=types.ContentType.PHOTO)
async def enuz(msg: types.Message, state: FSMContext):
    await msg.answer("Kutib turing....")
    id = msg.photo[2]["file_id"]
    file = await bot.get_file(id)
    file_path = file.file_path
    await bot.download_file(file_path, destination="/home/ergashfx2/mandatbot/handlers/images/image.png")
    img = Image.open('/home/ergashfx2/mandatbot/handlers/images/image.png')
    result = pytesseract.image_to_string(img)
    translated = GoogleTranslator(source='auto', target='uz').translate(result)
    await msg.answer(translated)


@dp.message_handler(state="uzen", content_types=types.ContentType.PHOTO)
async def enuz(msg: types.Message, state: FSMContext):
    await msg.answer("Kutib turing....")
    id = msg.photo[2]["file_id"]
    file = await bot.get_file(id)
    file_path = file.file_path
    await bot.download_file(file_path, destination="/home/ergashfx2/mandatbot/handlers/images/image.png")
    img = Image.open('/home/ergashfx2/mandatbot/handlers/images/image.png')
    result = pytesseract.image_to_string(img)
    translated = GoogleTranslator(source='auto', target='en').translate(result)
    await msg.answer(translated)


@dp.message_handler(state="uzru", content_types=types.ContentType.PHOTO)
async def enuz(msg: types.Message, state: FSMContext):
    await msg.answer("Kutib turing....")
    id = msg.photo[2]["file_id"]
    file = await bot.get_file(id)
    file_path = file.file_path
    await bot.download_file(file_path, destination="/home/ergashfx2/mandatbot/handlers/images/image.png")
    img = Image.open('/home/ergashfx2/mandatbot/handlers/images/image.png')
    result = pytesseract.image_to_string(img)
    translated = GoogleTranslator(source='auto', target='ru').translate(result)
    await msg.answer(translated)


@dp.message_handler(state="ruuz", content_types=types.ContentType.PHOTO)
async def enuz(msg: types.Message, state: FSMContext):
    await msg.answer("Kutib turing....")
    id = msg.photo[2]["file_id"]
    file = await bot.get_file(id)
    file_path = file.file_path
    await bot.download_file(file_path, destination="/home/ergashfx2/mandatbot/handlers/images/image.png")
    img = Image.open('/home/ergashfx2/mandatbot/handlers/images/image.png')
    result = pytesseract.image_to_string(img, lang='rus')
    translated = GoogleTranslator(source='auto', target='uz').translate(result)
    await msg.answer(translated)


@dp.message_handler(state="uzru")
async def enuz(msg: types.Message):
    to_translate = msg.text
    translated = GoogleTranslator(source='auto', target='ru').translate(to_translate)
    await msg.answer(translated)


@dp.message_handler(state="ruuz")
async def enuz(msg: types.Message):
    to_translate = msg.text
    translated = GoogleTranslator(source='auto', target='uz').translate(to_translate)
    await msg.answer(translated)


@dp.message_handler(text=btns["in_uzbek"])
async def in_russian_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Kerakli modulni tanlang", reply_markup=modules.modules)


@dp.message_handler(text=btns["in_russian"])
async def in_russian_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Выберите нужный модуль", reply_markup=modules.modules2)


@dp.message_handler(text="1 - Modul")
async def in_uzbek_handler(msg: types.Message, state: FSMContext):
    await msg.answer(texts["select_subject"], reply_markup=keyboard.uzbek)
    await state.set_state("test")


@dp.message_handler(text="2 - Modul")
async def in_uzbek_handler(msg: types.Message, state: FSMContext):
    await msg.answer(texts["select_subject"], reply_markup=keyboard.uzbek)
    await state.set_state("test2")


@dp.message_handler(text="Modul - 1")
async def in_russian_handler(msg: types.Message, state: FSMContext):
    await msg.answer(texts["ru_select_subject"], reply_markup=keyboard.rus)
    await state.set_state("testru")


@dp.message_handler(text="Modul - 2")
async def in_russian_handler(msg: types.Message, state: FSMContext):
    await msg.answer(texts["ru_select_subject"], reply_markup=keyboard.rus)
    await state.set_state("testru2")


@dp.message_handler(text=btns["result"])
async def result_handler(msg: types.Message, state: FSMContext):
    await msg.answer(texts["instruction"], reply_markup=back, parse_mode="HTML")
    await state.set_state("result")


@dp.message_handler(state="result")
async def check_handler(msg: types.Message, state: FSMContext):
    try:
        test_number = msg.text[:-31]
        string = msg.text
        yuborildi = re.sub(r'.', '', string, count=5)
        arr = list(yuborildi)
        javob = javoblar.javoblar[0][test_number]
        arr2 = list(javob)
        res = await compare(arr, arr2)
        result = len(res)

        now = datetime.now()
        xatolar = str()
        current_time = now.strftime("%H:%M:%S")
        await msg.answer(
            f"👤 Foydalanuvchi ismi: {msg.from_user.full_name}\n📖 Test nomeri: {test_number}\n✏️ Jami savollar soni: 30 "
            f"ta\n✅ To'g'ri javoblar soni: {30 - int(result)} ta\n❌ Xato javoblar: {result} ta\n🕐{current_time}")
        for r in res:
            xatolar += f"{int(r) + 1})\n"

        await msg.answer(f"Quyidagi savollarda xato qilgansiz\n\n{xatolar}")
        await state.finish()
    except:
        await msg.answer("Qandaydir xatolik yuz berdi /start buyrug'ini bosing va javoblar sonini tekshirib qayta "
                         "urinib ko'ring...")
        await state.finish()


@dp.message_handler(text=btns["video_instruction"])
async def teach(msg: types.Message):
    await msg.answer_video("https://t.me/testiszlar/29",
                           caption=texts["caption_instruction"],
                           parse_mode="HTML")


@dp.message_handler(text=btns["blokli"])
async def result_handler(msg: types.Message, state: FSMContext):
    await msg.answer("*Kerakli fanni tanlang:*", reply_markup=blok, parse_mode="markdown")
    await state.set_state("blokli")


@dp.message_handler(text=btns["new_test"])
async def new_test_handler(msg: types.Message):
    await msg.answer(texts["select_test_language"], reply_markup=keyboard.test)


@dp.message_handler(text="Ortga qaytish", state=["mother", "matem"])
async def welcome(msg: types.Message, state: FSMContext):
    await msg.answer(f"Kerakli fanni tanlang", reply_markup=blok)
    await state.finish()


@dp.message_handler(text="Ortga qaytish")
async def welcome(msg: types.Message, state: FSMContext):
    await msg.answer(f"Kerakli fanni tanlang", reply_markup=start_btn())
    await state.finish()


@dp.message_handler(text="Matematika (5-11)", state="blokli")
async def welcome(msg: types.Message, state: FSMContext):
    name = msg.from_user.full_name
    await msg.answer(f"*Kerakli sinfni tanlang*", reply_markup=Sinflar, parse_mode="markdown")
    await state.set_state("matem")


@dp.message_handler(text="Ona tili (5-11)", state="blokli")
async def welcome(msg: types.Message, state: FSMContext):
    name = msg.from_user.full_name
    await msg.answer(f"*Kerakli sinfni tanlang*", reply_markup=Sinflar, parse_mode="markdown")
    await state.set_state("mother")


@dp.message_handler(state="matem")
async def welcome(msg: types.Message, state: FSMContext):
    sinf = msg.text[:2]
    son = int(sinf)
    raqami = 222 + son
    await msg.answer_document(f"https://t.me/testiszlar/{raqami}", caption=f"{sinf} *Sinf matematika testlar to'plami*",
                              reply_markup=Sinflar, parse_mode="markdown")


@dp.message_handler(state="mother")
async def welcome(msg: types.Message, state: FSMContext):
    sinf = msg.text[:2]
    son = int(sinf)
    raqami = 215 + son
    await msg.answer_document(f"https://t.me/testiszlar/{raqami}",
                              caption=f"{sinf} *Sinf Ona tili fanidan testlar to'plami*", reply_markup=Sinflar,
                              parse_mode="markdown")


@dp.message_handler(text="📑 Majburiy fanlardan testlar")
async def send_majburiy(msg: types.Message):
    await msg.answer_document("https://t.me/testiszlar/195", caption="Matematika")
    await msg.answer_document("https://t.me/testiszlar/196", caption="Ona tili")
    await msg.answer_document("https://t.me/testiszlar/197", caption="Tarix")
    await msg.answer(
        "Ushbu variyantlar DTM ning pulli variyantlar bo'limiga kirganligi sababli javoblarini olish ilojisi bo'lmadi hozircha bizda javoblar mavjud emas.\n\nAgar ushbu variyantlarning aniq javoblarini ishlab bera olsangiz va holis yordam berishga tayyor bo'lsangiz bizga bog'laning va biz javob variyantlarini kiritib qo'yamiz")


from aiogram import types
from testlar.variyantlar import variyantuz, uzbtest, rutestnum, rutest, variyantuz2, rutest2
from config import texts
from main import dp
from aiogram.dispatcher import FSMContext
from keyboards.keyboard import test
from testlar.variyantlar import blokli2, blokli1


@dp.message_handler(state="blokli")
async def result_handler(msg: types.Message, state: FSMContext):
    matn = msg.text
    try:
        await msg.answer_document(blokli1[0][f"{msg.text}"], caption="Siz so'ragan to'plam marhamat")
        await msg.answer_document(blokli2[0][f"{msg.text}"], caption="To'plam javoblari")
    except:
        await msg.answer(texts["select_test_language"], reply_markup=test)
        await state.finish()


@dp.message_handler(state="test")
async def result_handler(msg: types.Message, state: FSMContext):
    matn = msg.text
    try:
        await msg.answer_document(variyantuz[str(msg.text)],
                                  caption=f"Fan : {msg.text}\nTest raqami : {uzbtest[str(msg.text)]}")
        await msg.answer(
            "Javoblarini tekshirish uchun Natijalarni bilish bo'limiga kirasiz \n\n KItobcha nomidagi sonlardan keyin "
            "/ belgisini qoyib o'z javoblaringizni yozasiz \n\n Misol :1017/acbbdbcddgcdabdbabcdbddbbabcca")
        # await msg.answer_document(blokli2[0][f"{msg.text}"],caption="To'plam javoblari")
    except:
        await msg.answer(texts["select_test_language"], reply_markup=test)
        await state.finish()


@dp.message_handler(state="testru")
async def result_handler(msg: types.Message, state: FSMContext):
    matn = msg.text
    try:
        await msg.answer_document(rutest[str(msg.text)],
                                  caption=f"Наука : {msg.text}\nНомер теста : {rutestnum[str(msg.text)]}")
        await msg.answer(
            "Для проверки ответов перейдите в раздел Результаты \n\n После цифр в названии буклета поставьте / и напишите свои ответы\n\nПример:1017/acbbdbcddgcdabdbabcdbddbbabcca")  # await msg.answer_document(blokli2[0][f"{msg.text}"],caption="To'plam javoblari")
    except:
        await msg.answer(texts["select_test_language"], reply_markup=test)
        await state.finish()


@dp.message_handler(state="test2")
async def result_handler(msg: types.Message, state: FSMContext):
    matn = msg.text
    try:
        await msg.answer_document(variyantuz2[str(msg.text)], caption=f"Fan : {msg.text.title()}")
        await msg.answer(
            "Ushbu test DTM saytining rasmiy botidan olindi shu sabab faqatgina ushbu bot orqali javoblarni tekshirishingiz mumkin\n\nDTM ning rasmiy boti : @e_dtm_bot\n\nQuyida ushbu botni qanday ishlatish qo'llanmasi 👇 \n\nhttps://telegra.ph/Botdan-foydalanish-boyicha-qollanma-02-14  ")  # await msg.answer_document(blokli2[0][f"{msg.text}"],caption="To'plam javoblari")
    except:
        await msg.answer(texts["select_test_language"], reply_markup=test)
        await state.finish()


@dp.message_handler(state="testru2")
async def result_handler(msg: types.Message, state: FSMContext):
    matn = msg.text
    try:
        await msg.answer_document(rutest2[str(msg.text)], caption=f"Fan : {msg.text.title()}")
        await msg.answer(
            "Ushbu test DTM saytining rasmiy botidan olindi shu sabab faqatgina ushbu bot orqali javoblarni tekshirishingiz mumkin\n\nDTM ning rasmiy boti : @e_dtm_bot\n\nQuyida ushbu botni qanday ishlatish qo'llanmasi 👇 \n\nhttps://telegra.ph/Botdan-foydalanish-boyicha-qollanma-02-14  ")  # await msg.answer_document(blokli2[0][f"{msg.text}"],caption="To'plam javoblari")
    except:
        await msg.answer(texts["select_test_language"], reply_markup=test)
        await state.finish()
