from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from utils.databace import referal_code
from aiogram.dispatcher.filters.state import StatesGroup,State
from aiogram.dispatcher.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import *
import sqlite3

conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()


main_page = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Mening shikoyatlarim 📝"),
            KeyboardButton("Mening ma'lumotlarim 📝"),
            KeyboardButton("Parol ozgartirish 📝")

        ],
    ],
    resize_keyboard=True
)



class Passwoard(StatesGroup):
    old_password = State()
    new_passwoard = State()



@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    a = message.text.split("invite")
    invite_code = a[1]
    print(invite_code)
    message_id = message.from_user.id
    referal_code(invite_code, message_id)
    await message.answer(f"Salom - {message.from_user.full_name}\nO'zingizga kerakli bolimni tanlang!",reply_markup=main_page)


@dp.message_handler(text="Mening shikoyatlarim 📝")
async def shikoyat(message: types.Message):
    select_model_user_id = cursor.execute("SELECT id FROM Calculator_homemodel WHERE connected_telegram = ?",
                                          (message.from_user.id,)).fetchone()
    reporter_id = ""
    for i in select_model_user_id:
        reporter_id += str(i)
    select_report = cursor.execute("SELECT report_description FROM Calculator_reportmodel WHERE id = ?",
                                   (reporter_id,)).fetchall()
    report = ""
    for i in select_report:
        report += str(f"{i}🧩")

    if not select_report:
        await message.answer("Sizning ma'lumotlaringiz topilmadi.", reply_markup=main_page)
    else:
        report = ""
        for i in select_report:
            report += str(i) + "\n"
        await message.answer(f"Sizning shikoyatlaringiz:\n{report}", reply_markup=main_page)


@dp.message_handler(text="Parol ozgartirish 📝")
async def parol_ozgartirish(message: types.Message):
    await message.answer("Eski parolingizni kiriting:")
    await Passwoard.old_password.set()

@dp.message_handler(state=Passwoard.old_password)
async def old_password(message: types.Message):
    old_passwd = message.text
    old_passwd_database = cursor.execute(
        "SELECT password FROM Calculator_homemodel WHERE id = ?",
        (message.from_user.id,)
    ).fetchone()

    if old_passwd == old_passwd_database:
        old_passwd_database_check = old_passwd_database[0]

        if old_passwd == old_passwd_database_check:
            await message.answer("Yangi parolni kiriting:")
            await Passwoard.new_passwoard.set()
        else:
            await message.answer("Eski parol noto'g'ri.")



    else:
        print("wrong password")
        await message.answer("parol hato kodni qaytib kiriting")
        await Passwoard.new_passwoard.set()

@dp.message_handler(state=Passwoard.new_passwoard)
async def new_passwoard(message: types.Message, state: FSMContext):
    new_passwd = message.text
    cursor.execute("UPDATE Calculator_homemodel SET password = ? WHERE id = ?", (new_passwd, message.from_user.id))
    conn.commit()
    await message.answer("Parol ozgartirildi")
    await state.finish()


@dp.message_handler(text="Mening ma'lumotlarim 📝")
async def mas_lumotlarim(message: types.Message):
    user_id = message.from_user.id
    user_data_database = cursor.execute("SELECT * FROM Calculator_homemodel WHERE id = ?", (user_id,)).fetchone()

    if user_data_database:
        user_data = ""

        for i in user_data_database:
            user_data += str(i) + "\n"

        await message.answer(f'Sizning ma\'lumotlaringiz:\n{user_data}', reply_markup=main_page)
    else:
        await message.answer("Sizning ma'lumotlaringiz topilmadi.", reply_markup=main_page)