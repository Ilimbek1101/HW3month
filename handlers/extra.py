from aiogram import types, Dispatcher
from config import bot, dp

async def echo(message: types.Message):
    try:
        n = float(message.text)
        await message.answer(n**2)
    except:
        await bot.send_message(message.chat.id, message.text)

    if message.reply_to_message:
        if message.text.startswith("!pin"):
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)

def register_message_handler_extra(dp: Dispatcher):
    dp.register_message_handler(echo)