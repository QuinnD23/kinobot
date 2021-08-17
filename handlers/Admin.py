from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command

# config
from data.config import admin_id

# db_commands
from handlers.dbcommands import insert_db, update_db, select_db, delete_db

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import AdminMark


@dp.message_handler(Command("admin"))
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
        await message.answer("У вас нет прав🔒\n"
                             "Напишите: /start")
