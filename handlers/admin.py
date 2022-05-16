from aiogram import types, Dispatcher
from config import bot, ADMIN
import random

async def game(message: types.Message):

    if message.chat.type != 'private':
        if message.from_user.id != ADMIN:
            await message.reply("Ты не админ, для тебя данная команда не работает!")
        else:
            a = ['⚽', '🏀', '🎲', '🎯', '🎳', '🎰']
            await bot.send_message(message.chat.id, random.choice(a))
    else:
        await message.answer("Это работает только в группах!")

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(game, commands=['ame'], commands_prefix="g/")