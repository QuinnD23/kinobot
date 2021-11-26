from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# db_commands
from handlers.dbcommands import insert_db, update_db, select_db, delete_db

# find_commands
from handlers.findcommands import get_rand

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import StartMenuMark, GenresMark, NextMark


@dp.message_handler(state=StateMachine.YearMenu)
async def mes_state(message: Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)

    # ----- start
    if message.text == "/start":
        await message.answer(f"Привет, {user_name}!", reply_markup=StartMenuMark)
        await StateMachine.StartMenu.set()
    # -----

    # ----- back
    if message.text == "Назад◀":
        await message.answer("Выберите жанр:", reply_markup=GenresMark)
        await StateMachine.GenreMenu.set()
    # -----

    years = message.text

    if years == "2010-2020":
        await message.answer(f"Вы выбрали: {message.text}", reply_markup=NextMark)

        await update_db("params", "user_id", "min_year", user_id, 2010)
        await update_db("params", "user_id", "max_year", user_id, 2020)

        await get_rand(user_id, dp)

        count = int(await select_db("params", "user_id", "count", user_id)) + 1
        await update_db("params", "user_id", "count", user_id, count)

        await StateMachine.ShowRandMenu.set()

    if years == "2000-2010":
        await message.answer(f"Вы выбрали: {message.text}", reply_markup=NextMark)

        await update_db("params", "user_id", "min_year", user_id, 2000)
        await update_db("params", "user_id", "max_year", user_id, 2010)

        await get_rand(user_id, dp)

        count = int(await select_db("params", "user_id", "count", user_id)) + 1
        await update_db("params", "user_id", "count", user_id, count)

        await StateMachine.ShowRandMenu.set()

    if years == "1990-2000":
        await message.answer(f"Вы выбрали: {message.text}", reply_markup=NextMark)

        await update_db("params", "user_id", "min_year", user_id, 1990)
        await update_db("params", "user_id", "max_year", user_id, 2000)

        await get_rand(user_id, dp)

        count = int(await select_db("params", "user_id", "count", user_id)) + 1
        await update_db("params", "user_id", "count", user_id, count)

        await StateMachine.ShowRandMenu.set()

    if years == "1980-1990":
        await message.answer(f"Вы выбрали: {message.text}", reply_markup=NextMark)

        await update_db("params", "user_id", "min_year", user_id, 1980)
        await update_db("params", "user_id", "max_year", user_id, 1990)

        await get_rand(user_id, dp)

        count = int(await select_db("params", "user_id", "count", user_id)) + 1
        await update_db("params", "user_id", "count", user_id, count)

        await StateMachine.ShowRandMenu.set()

    if years == "1970-1980":
        await message.answer(f"Вы выбрали: {message.text}", reply_markup=NextMark)

        await update_db("params", "user_id", "min_year", user_id, 1970)
        await update_db("params", "user_id", "max_year", user_id, 1980)

        await get_rand(user_id, dp)

        count = int(await select_db("params", "user_id", "count", user_id)) + 1
        await update_db("params", "user_id", "count", user_id, count)

        await StateMachine.ShowRandMenu.set()

    if years == "1960-1970":
        await message.answer(f"Вы выбрали: {message.text}", reply_markup=NextMark)

        await update_db("params", "user_id", "min_year", user_id, 1960)
        await update_db("params", "user_id", "max_year", user_id, 1970)

        await get_rand(user_id, dp)

        count = int(await select_db("params", "user_id", "count", user_id)) + 1
        await update_db("params", "user_id", "count", user_id, count)

        await StateMachine.ShowRandMenu.set()