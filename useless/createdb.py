from data.config import userc, passc, hostc

import psycopg2.extras


async def create_db():
    conn = psycopg2.connect(dbname="postgres", user=userc, password=passc, host=hostc)

    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            try:
                cur.execute("CREATE TABLE params (user_id varchar primary key, genre integer default 0, min_year integer default 0, max_year integer default 0);")
            except:
                pass
            try:
                cur.execute("CREATE TABLE links (id varchar primary key, genre integer default 0, min_year integer default 0, max_year integer default 0, link varchar default 0);")
            except:
                pass

    conn.close()
