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
