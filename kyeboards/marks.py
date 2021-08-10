from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

StartMenuMark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Найти фильм🎈"),
        ],
    ],
    resize_keyboard=True
)

BackMark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад◀️"),
        ],
    ],
    resize_keyboard=True
)

GenresMark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Боевик🔫"),
            KeyboardButton(text="Мелодрама🥰"),
            KeyboardButton(text="Комедия😹"),
        ],
        [
            KeyboardButton(text="Драма😥"),
            KeyboardButton(text="Мультфильм🧸"),
            KeyboardButton(text="Триллер😨"),
        ],
        [
            KeyboardButton(text="Ужасы👻"),
            KeyboardButton(text="Фантастика🤖"),
            KeyboardButton(text="Фэнтези🦄"),
        ],
    ],
    resize_keyboard=True
)
YearMark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="2010-2020"),
            KeyboardButton(text="2000-2010"),
            KeyboardButton(text="1990-2000"),
        ],
        [
            KeyboardButton(text="1980-1990"),
            KeyboardButton(text="1970-1980"),
            KeyboardButton(text="1960-1970"),
        ],
        [
            KeyboardButton(text="Назад◀️"),
        ],
    ],
    resize_keyboard=True
)
NextMark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Следующий⚡️"),
            KeyboardButton(text="Сбросить🔥"),
        ],
    ],
    resize_keyboard=True
)

AdminMark = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Боевик - 3💎"),
            KeyboardButton(text="Мелодрама - 7💎"),
            KeyboardButton(text="Комедия - 6💎"),
        ],
        [
            KeyboardButton(text="Драма - 8💎"),
            KeyboardButton(text="Мультфильм💎 - 14"),
            KeyboardButton(text="Триллер - 4💎"),
        ],
        [
            KeyboardButton(text="Ужасы - 1💎"),
            KeyboardButton(text="Фантастика - 2💎"),
            KeyboardButton(text="Фэнтези - 5💎"),
        ],
    ],
    resize_keyboard=True
)