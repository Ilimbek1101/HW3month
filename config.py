from aiogram import Bot, Dispatcher
from decouple import config

TOKEN = config("KEYTOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

ADMIN = 1195853476