from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# db_commands
from handlers.dbcommands import insert_db, update_db, select_db, delete_db

# find_commands
from handlers.findcommands import get_rand

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import StartMenuMark


@dp.message_handler(state=StateMachine.ShowRandMenu)
async def mes_state(message: Message):
    user_id = str(message.from_user.id)

    # ----- start and back
    if message.text == "/start" or message.text == "Сбросить🔥":
        user_name = message.from_user.username
        try:
            await insert_db("params", "user_id", user_id)
        except:
            pass
        await message.answer(f"Привет, {user_name}!", reply_markup=StartMenuMark)
        await StateMachine.StartMenu.set()
    # -----

    if message.text == "Следующий⚡️":
        await get_rand(user_id, dp)
