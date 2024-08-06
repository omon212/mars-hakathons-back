from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from utils.databace import referal_code


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    a = message.text.split("invite")
    invite_code = a[1]
    print(invite_code)
    message_id = message.from_user.id
    referal_code(invite_code, message_id)
