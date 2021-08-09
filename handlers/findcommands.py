from aiogram import Dispatcher
import random

# requests
import requests
from bs4 import BeautifulSoup

# config
from data.config import admin_id

# db_commands
from handlers.dbcommands import insert_db, update_db, select_db, delete_db


# Боевик - 3
# Мелодрама - 7
# Комедия - 6
# Драма - 8
# Мультфильм - 14
# Триллер - 4
# Ужасы - 1
# Фантастика - 2
# Фэнтези - 5

# 2010-2020
# 2000-2010
# 1990-2000
# 1980-1990
# 1970-1980
# 1960-1970


async def get_rand(user_id, dp: Dispatcher):
    genre = str(await select_db("params", "user_id", "genre", user_id))
    min_year = str(await select_db("params", "user_id", "min_year", user_id))
    max_year = str(await select_db("params", "user_id", "max_year", user_id))

    # количество фильмов
    kol = 2000
    num = str(random.randint(1, kol))

    id = num + "$" + genre + "$" + min_year + "$" + max_year

    url = str(await select_db("links", "id", "link", id))

    await dp.bot.send_message(user_id, f"{url}")






async def get_films(dp: Dispatcher):
    # количество фильмов
    kol = 2000

    genre_names = ["Боевик", "Мелодрама", "Комедия", "Драма", "Мультфильм", "Триллер", "Ужасы", "Фантастика", "Фэнтези"]
    genre_numbers = [3, 7, 6, 8, 14, 4, 1, 2, 5]
    years_min = [2010, 2000, 1990, 1980, 1970, 1960]
    years_max = [2020, 2010, 2000, 1990, 1980, 1970]
    for g in range(len(genre_numbers)):
        genre = str(genre_numbers[g])

        for y in range(len(years_min)):
            await dp.bot.send_message(admin_id, f"Начинается загрузка жанра: {str(genre_names[g])} - {str(genre_numbers[g])}")
            await dp.bot.send_message(admin_id, f"Временной интервал: {str(years_min[y])} - {str(years_max[y])}")

            n = 1
            p = 1
            min_year = str(years_min[y])
            max_year = str(years_max[y])

            while n <= kol:
                url = f"https://www.kinopoisk.ru/s/type/film/list/1/order/rating/m_act[from_year]/{min_year}/m_act[to_year]/{max_year}/m_act[genre][0]/{genre}/m_act[genre_and]/on/page/{str(p)}/"

                headers = {
                    "accept": "*/*",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275",
                }

                req = requests.get(url, headers=headers)
                src = req.text

                soup = BeautifulSoup(src, "lxml")

                all_info = soup.find_all("div", class_="info")

                for info in all_info:
                    text = info.find("p", class_="name").find("a").text
                    link = str(info.find("p", class_="name").find("a").get("href"))
                    link = link[:len(link)-6]
                    link = "https://www.kinopoisk.ru" + link
                    check_film = text.find("сериал")
                    if check_film == -1 and n <= kol:
                        id = str(n) + "$" + genre + "$" + min_year + "$" + max_year
                        await insert_db("links", "id", id)
                        await update_db("links", "id", "genre", id, genre)
                        await update_db("links", "id", "min_year", id, min_year)
                        await update_db("links", "id", "max_year", id, max_year)
                        await update_db("links", "id", "link", id, link)
                        n += 1
                await dp.bot.send_message(admin_id, f"Страница: {str(p)}/20")
                p += 1

        await dp.bot.send_message(admin_id, f"Загрузка жанра окончена: {str(genre_names[g])} - {str(genre_numbers[g])}")
