import sqlite3

import config

connect = sqlite3.connect(database=config.DB_PATH)
cursor = connect.cursor()
cursor.execute("SELECT * FROM sqlite_master")
print(cursor.fetchall())
