from aiogram import types, Bot, Dispatcher
from decouple import config

TOKEN = config("KEYTOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)