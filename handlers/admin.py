from aiogram import types, Dispatcher
from config import bot, ADMIN
import random

# async def game(message: types.Message):
#     if message.chat.type != 'private':
#         if message.from_user.id == ADMIN:
#             if message.text.startswith("game"):
#                 a = ['⚽', '🏀', '🎲', '🎯', '🎳', '🎰']
#                 await bot.send_message(message.chat.id, random.choice(a))
#
# def register_handlers_admin(dp: Dispatcher):
#     dp.register_message_handler(game, commands="game")