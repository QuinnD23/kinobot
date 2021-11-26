from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# db_commands
from handlers.dbcommands import insert_db, update_db, select_db, delete_db

# find_commands
from handlers.findcommands import get_rand

# date
import datetime

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import StartMenuMark


@dp.message_handler(state=StateMachine.ShowRandMenu)
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

    # ----- back
    if message.text == "Сбросить🔥":
        await message.answer(f"Сброс...", reply_markup=StartMenuMark)
        await StateMachine.StartMenu.set()
    # -----

    if message.text == "Следующий⚡":
        await get_rand(user_id, dp)

        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).strftime("%d-%m-%Y")
        await update_db("params", "user_id", "last_date", user_id, now)

        count = int(await select_db("params", "user_id", "count", user_id)) + 1
        await update_db("params", "user_id", "count", user_id, count)
