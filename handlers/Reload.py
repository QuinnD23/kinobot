from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# config
from data.config import admin_id

# db_commands
from handlers.dbcommands import insert_db, update_db, select_db, delete_db

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import StartMenuMark, AdminMark


@dp.message_handler()
async def mess(message: Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)

    if user_id == admin_id:
        check = True

        try:
            await select_db("params", "user_id", "user_num", user_id)
        except:
            check = False

        if check:
            await message.answer(f"Привет, админ!", reply_markup=AdminMark)
            await StateMachine.StartMenu.set()
    else:
        check = True

        try:
            await select_db("params", "user_id", "user_num", user_id)
        except:
            check = False

        if check:
            await message.answer(f"Привет, {user_name}!", reply_markup=StartMenuMark)
            await StateMachine.StartMenu.set()

