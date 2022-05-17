from aiogram.utils import executor
from config import dp
from handlers import admin, client, callback, extra, fsmAdminMenu
import logging

client.register_handler_client(dp)
callback.register_handler_callback(dp)
admin.register_handlers_admin(dp)
fsmAdminMenu.register_handler_fsmmenu(dp)
extra.register_message_handler_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)