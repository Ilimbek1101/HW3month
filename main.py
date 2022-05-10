from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
import logging
from decouple import config

TOKEN = config("KEYTOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['test'])
async def test_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)
    vopros = "В каком году началась ВОВ?"
    otvety = ['1956', '1913', '1941', '1945', '1939']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=vopros,
        options=otvety,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Давайте изучать свою историю",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def test_2(call: types.CallbackQuery):
    vopros = "А в каком году началась Вторая Мировая Война?"
    otvety = ['1956', '1913', '1941', '1945', '1939']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=vopros,
        options=otvety,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="Давайте изучать свою историю",
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )

@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    mem = open("mempicture/shoes.jpg", "rb")
    await bot.send_photo(message.from_user.id, photo=mem)

@dp.message_handler()
async def echo(message: types.Message):
    try:
        n = float(message.text)
        await message.answer(n*n)
    except:
        await bot.send_message(message.from_user.id, message.text)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)