from aiogram import types, Dispatcher
from config import bot, dp
import random

async def echo(message: types.Message):

    bad_words = ['bitch', 'damn', 'foolish']
    if message.text.lower() in bad_words:
        await bot.send_message(message.chat.id,
                               f"don't say it {message.from_user.full_name}")
        await bot.delete_message(message.chat.id, message.message_id)

    if message.text.startswith("game"):
        game = ['⚽', '🏀', '🎲', '🎯', '🎳', '🎰']
        await bot.send_message(message.chat.id, random.choice(game))

    if message.reply_to_message:
        if message.text.startswith("!pin"):
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)

def register_message_handler_extra(dp: Dispatcher):
    dp.register_message_handler(echo)