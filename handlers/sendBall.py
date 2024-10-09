from aiogram import types

from config import texts
from main import dp
from aiogram.dispatcher import FSMContext
from sql.ball import get_ball


@dp.message_handler(text="📈 To'plagan balini bilish", state=None)
async def test(msg: types.Message, states: FSMContext):
    await msg.answer_photo("https://t.me/testiszlar/238", caption="*Namunaga binoan ID raqamingizni kiriting*",
                           parse_mode="markdown")
    await states.set_state("ball")


@dp.message_handler(state="ball", content_types=types.ContentType.TEXT)
async def test(msg: types.Message):
    ball = await get_ball(ID=msg.text)
    await msg.answer(ball[4])
