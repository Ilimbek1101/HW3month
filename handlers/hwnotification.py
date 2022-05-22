import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot

async def get_chat_id(message: types.Message):
    global hwchat_id
    hwchat_id = message.chat.id
    await bot.send_message(chat_id=hwchat_id, text="Ваш chat id получен!")

async def start_python_training():
    await bot.send_message(chat_id=hwchat_id, text="Пора начать учебу по Python!")

async def finish_python_training():
    file = open("mempicture/gohome.mp4", "rb")
    await bot.send_video(chat_id=hwchat_id, video=file, caption="Конец учебы, беги домой!!!")

async def scheduler():
    aioschedule.every().tuesday.at("18:00").do(start_python_training)
    aioschedule.every().tuesday.at("20:00").do(finish_python_training)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(3)

def register_handler_hwnotification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'учеба' in word.text)

