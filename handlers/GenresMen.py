from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# db_commands
from handlers.dbcommands import insert_db, update_db, select_db, delete_db

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import YearMark, StartMenuMark


@dp.message_handler(state=StateMachine.GenreMenu)
async def mes_state(message: Message):
    user_id = str(message.from_user.id)

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

    genre = message.text

    if genre == "Боевик🔫":
        await message.answer(f"Вы выбрали: {message.text}", reply_markup=YearMark)
        await message.answer(f"Выберите интервал:")

        await update_db("params", "user_id", "genre", user_id, 3)

        await StateMachine.YearMenu.set()

    if genre == "Мелодрама🥰":
        await message.answer(f"Вы выбрали: {message.text}", reply_markup=YearMark)
        await message.answer(f"Выберите интервал:")

        await update_db("params", "user_id", "genre", user_id, 7)

        await StateMachine.YearMenu.set()

    if genre == "Комедия😹":
        await message.answer(f"Вы выбрали: {message.text}", reply_markup=YearMark)
        await message.answer(f"Выберите интервал:")

        await update_db("params", "user_id", "genre", user_id, 6)

        await StateMachine.YearMenu.set()
    if genre == "Драма😥":

        await message.answer(f"Вы выбрали: {message.text}", reply_markup=YearMark)
        await message.answer(f"Выберите интервал:")

        await update_db("params", "user_id", "genre", user_id, 8)

        await StateMachine.YearMenu.set()

    if genre == "Мультфильм🧸":
        await message.answer(f"Вы выбрали: {message.text}", reply_markup=YearMark)
        await message.answer(f"Выберите интервал:")

        await update_db("params", "user_id", "genre", user_id, 14)

        await StateMachine.YearMenu.set()

    if genre == "Триллер😨":
        await message.answer(f"Вы выбрали: {message.text}", reply_markup=YearMark)
        await message.answer(f"Выберите интервал:")

        await update_db("params", "user_id", "genre", user_id, 4)

        await StateMachine.YearMenu.set()

    if genre == "Ужасы👻":
        await message.answer(f"Вы выбрали: {message.text}", reply_markup=YearMark)
        await message.answer(f"Выберите интервал:")

        await update_db("params", "user_id", "genre", user_id, 1)

        await StateMachine.YearMenu.set()

    if genre == "Фантастика🤖":
        await message.answer(f"Вы выбрали: {message.text}", reply_markup=YearMark)
        await message.answer(f"Выберите интервал:")

        await update_db("params", "user_id", "genre", user_id, 2)

        await StateMachine.YearMenu.set()

    if genre == "Фэнтези🦄":
        await message.answer(f"Вы выбрали: {message.text}", reply_markup=YearMark)
        await message.answer(f"Выберите интервал:")

        await update_db("params", "user_id", "genre", user_id, 5)

        await StateMachine.YearMenu.set()