from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("KEYTOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

ADMIN = 1195853476