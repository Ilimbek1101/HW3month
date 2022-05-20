from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot, ADMIN
from hwkeyboards.hw_kb import cancel_markup
from hwdatabase import hwbot_db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

async def fsm_start_menu(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.photo.set()
        await bot.send_message(
            message.chat.id,
            f"Привет {message.from_user.full_name}, скинь фотку блюда",
            reply_markup=cancel_markup
        )
    else:
        await message.answer("Пиши в личку!")

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Как называется блюдо?")

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Дайте описание блюда:")

async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer("Какова цена блюда?")

async def load_price(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['price'] = int(message.text)
        await hwbot_db.sql_command_insert(state)
        await state.finish()
        await message.answer("Спасибо за работу!")
    except:
        await message.answer("Цена должна быть только в цифрах!!!")

async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.reply("Внесение информации по блюду отменено!")

async def delete_data(message: types.Message):
    if message.from_user.id == ADMIN:
        result = await hwbot_db.sql_command_all()
        for i in result:
            await bot.send_photo(message.from_user.id,
                                 i[0],
                                 caption=f"Name: {i[1]}\n"
                                         f"Description: {i[2]}\n"
                                         f"Price: {i[3]}\n",
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(
                                     f"delete: {i[1]}",
                                     callback_data=f'{i[1]}'
                                 ))
                                 )
    else:
        await message.answer("Ты не админ!!!")

async def complete_delete(call: types.CallbackQuery):
    await hwbot_db.sql_command_delete(call.data)
    await call.answer(text=f"{call.data} deleted", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)

def register_handler_fsmmenu(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state='*', commands="cancel")
    dp.register_message_handler(cancel_registration, Text(equals='cancel', ignore_case=True), state='*',)
    dp.register_message_handler(fsm_start_menu, commands=['menu'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=["photo"])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(delete_data, commands=["del"])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data)

