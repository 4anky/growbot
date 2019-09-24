import sqlite3


def create_connection(db_path):
    connect = None
    try:
        connect = sqlite3.connect(database=db_path)
        return connect
    except sqlite3.Error as Error:
        print(Error)
        return connect


def reg(db_path, telegram_id, first_name, username):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(sql="INSERT OR IGNORE INTO users VALUES (?, ?, ?)",
                       parameters=(telegram_id, first_name, username))
    except sqlite3.Error as Error:
        print(Error)
    connection.commit()
    connection.close()
