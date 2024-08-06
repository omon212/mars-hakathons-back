from aiogram.types import *

main_page = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Mening shikoyatlarim 📝"),
            KeyboardButton("Mening ma'lumotlarim 📝")
        ],
    ],
    resize_keyboard=True
)
