sql_create_user_table = """
        CREATE TABLE IF NOT EXISTS telegram_users
        (id INTEGER PRIMARY KEY,
        telegram_id INTEGER,
        username CHAR(50),
        firstname CHAR(50),
        lastname CHAR(50)
        )
"""


start_insert_user_query = """INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)"""