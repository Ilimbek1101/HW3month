from aiogram import types, Dispatcher
from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from hwparser import lastvideos

async def mem(message: types.Message):
    mem = open("mempicture/shoes.jpg", "rb")
    await bot.send_photo(message.from_user.id, photo=mem)

async def test_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)
    vopros = "В каком году началась ВОВ?"
    otvety = ['1956', '1914', '1941', '1945', '1939']
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

async def parser_videos(message: types.Message):
    data = lastvideos.parser()
    for item in data:
        await bot.send_message(message.chat.id,
                               f"{item['title']}\n"
                               f"{item['desc']}\n\n"
                               f"{item['link']}")

def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(test_1, commands=['test'])
    dp.register_message_handler(parser_videos, commands=['videos'])