from aiogram.utils import executor
from config import dp
from handlers import admin, client, callback, extra, fsmAdminMenu, hwnotification
import logging
from hwdatabase import hwbot_db
import asyncio

async def on_startup(_):
    asyncio.create_task(hwnotification.scheduler())
    hwbot_db.sql_create()

client.register_handler_client(dp)
callback.register_handler_callback(dp)
admin.register_handlers_admin(dp)
fsmAdminMenu.register_handler_fsmmenu(dp)
hwnotification.register_handler_hwnotification(dp)
extra.register_message_handler_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)