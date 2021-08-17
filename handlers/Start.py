from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command

# config
from data.config import admin_id

# db_commands
from handlers.dbcommands import insert_db, update_db, select_db, delete_db

# find_commands
from handlers.findcommands import get_films

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import StartMenuMark, GenresMark, AdminMark


@dp.message_handler(Command("start"))
async def command_start(message: Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)

    if admin_id == user_id:
        try:
            await insert_db("params", "user_id", user_id)
        except:
            pass
        await update_db("params", "user_id", "user_name", user_id, user_name)

        await message.answer(f"Привет, админ!", reply_markup=AdminMark)
        await StateMachine.StartMenu.set()
    else:
        try:
            await insert_db("params", "user_id", user_id)
        except:
            pass
        await update_db("params", "user_id", "user_name", user_id, user_name)

        await message.answer(f"Привет, {user_name}!", reply_markup=StartMenuMark)
        await StateMachine.StartMenu.set()


@dp.message_handler(state=StateMachine.StartMenu)
async def mes_state(message: Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)

    # ----- start
    if message.text == "/start":
        user_name = message.from_user.username
        try:
            await insert_db("params", "user_id", user_id)
        except:
            pass
        await message.answer(f"Привет, {user_name}!", reply_markup=StartMenuMark)
        await StateMachine.StartMenu.set()
    # -----

    # ----- admin
    if message.text == "Боевик(3)" and admin_id == user_id:
        await get_films(3, dp)
    if message.text == "Мелодрама(7)" and admin_id == user_id:
        await get_films(7, dp)
    if message.text == "Комедия(6)" and admin_id == user_id:
        await get_films(6, dp)
    if message.text == "Драма(8)" and admin_id == user_id:
        await get_films(8, dp)
    if message.text == "Мультфильм(14)" and admin_id == user_id:
        await get_films(14, dp)
    if message.text == "Триллер(4)" and admin_id == user_id:
        await get_films(4, dp)
    if message.text == "Ужасы(1)" and admin_id == user_id:
        await get_films(1, dp)
    if message.text == "Фантастика(2)" and admin_id == user_id:
        await get_films(2, dp)
    if message.text == "Фэнтези(5)" and admin_id == user_id:
        await get_films(5, dp)

    if message.text == "Стать обычным☀":
        await message.answer(f"Привет, {user_name}!", reply_markup=StartMenuMark)
    # -----

    if message.text == "Найти фильм🎈":
        await message.answer("Выберите жанр:", reply_markup=GenresMark)
        await StateMachine.GenreMenu.set()
