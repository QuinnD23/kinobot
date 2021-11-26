from aiogram.dispatcher.filters.state import StatesGroup, State


class StateMachine(StatesGroup):
    StartMenu = State()

    GenreMenu = State()
    YearMenu = State()

    ShowRandMenu = State()