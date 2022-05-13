from aiogram import types, Dispatcher
from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode


async def test_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)
    vopros = "А в каком году началась Вторая Мировая Война?"
    otvety = ['1956', '1914', '1941', '1945', '1939']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=vopros,
        options=otvety,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="Давайте изучать свою историю",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

async def test_3(call: types.CallbackQuery):

    vopros = "А в каком году началась Первая Мировая Война?"
    otvety = ['1956', '1914', '1941', '1945', '1939']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=vopros,
        options=otvety,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Давайте изучать свою историю",
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )

def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(test_2,
                                       lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(test_3,
                                       lambda call: call.data == "button_call_2")