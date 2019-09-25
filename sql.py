from datetime import datetime
import sqlite3

import constants as const


def create_connection(db_path):
    connect = None
    try:
        connect = sqlite3.connect(database=db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        return connect
    except sqlite3.Error as Error:
        print(Error)
        return connect


def reg(db_path, telegram_id, first_name, username):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(const.REG_USERS, (telegram_id, first_name, username))
        cursor.execute(const.REG_FARM,
                       (telegram_id, const.START_GROW_BOX, const.START_GROW_BOX, const.START_GROW_BOX,
                        const.START_GROW_BOX, const.START_GROW_BOX, const.START_GROW_BOX, datetime.utcnow()))
        cursor.execute(const.REG_BALANCE, (telegram_id, const.START_MONEY, const.START_HIGH))
    except sqlite3.Error as Error:
        print(Error)
    connection.commit()
    connection.close()


def get_balance(db_path, telegram_id):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(const.GET_BALANCE, (telegram_id,))
    except sqlite3.Error as Error:
        print(Error)
    result = cursor.fetchone()
    connection.close()
    return result


def get_farm(db_path, telegram_id):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(const.GET_FARM, (telegram_id,))
    except sqlite3.Error as Error:
        print(Error)
    result = cursor.fetchone()
    connection.close()
    return result
