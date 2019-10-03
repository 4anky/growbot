from datetime import datetime
import sqlite3

import config


def create_connection(db_path):
    connect = None
    try:
        connect = sqlite3.connect(database=db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        return connect
    except sqlite3.Error as Error:
        print(Error)
        return connect


def reg(db_path, telegram_id):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(config.REG_USERS, (telegram_id, str(telegram_id)))
        cursor.execute(config.REG_BALANCE, (telegram_id, config.START_MONEY, config.START_HIGH, config.START_CHIP))
        cursor.execute(config.REG_FARM,
                       (telegram_id, config.START_GROW_BOX, config.START_GROW_BOX, config.START_GROW_BOX,
                        config.START_GROW_BOX, config.START_GROW_BOX, config.START_GROW_BOX, datetime.utcnow()))
    except sqlite3.Error as Error:
        print(Error)
    connection.commit()
    connection.close()


def is_reg(db_path, telegram_id):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE id = ?", (telegram_id, ))
    except sqlite3.Error as Error:
        print(Error)
    result = cursor.fetchone()
    connection.close()
    return result


def update_nick(db_path, telegram_id, nick):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE users SET nick = ? WHERE id = ?", (nick, telegram_id))
    except sqlite3.Error as Error:
        print(Error)
    connection.commit()
    connection.close()


def get_balance(db_path, telegram_id):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(config.GET_BALANCE, (telegram_id,))
    except sqlite3.Error as Error:
        print(Error)
    result = cursor.fetchone()
    connection.close()
    return result


def get_from_table(db_path, telegram_id, table, field):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(config.GET_FROM_TABLE.format(field=field, table=table), (telegram_id,))
    except sqlite3.Error as Error:
        print(Error)
    result = cursor.fetchone()[0]
    connection.close()
    return result


def get_farm(db_path, telegram_id):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(config.GET_FARM, (telegram_id,))
    except sqlite3.Error as Error:
        print(Error)
    result = cursor.fetchone()
    connection.close()
    return result


def buying_grow_box(db_path, telegram_id, name, price):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(config.BUYING_GROW_BOX.format(name=name), (telegram_id, ))
        cursor.execute(config.PAYING_MONEY.format(price=price), (telegram_id, ))
    except sqlite3.Error as Error:
        print(Error)
    connection.commit()
    connection.close()


def high_to_balance(db_path, telegram_id, high):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(config.HIGH_TO_BALANCE.format(high=high), (telegram_id, ))
        cursor.execute(config.HIGH_TO_BALANCE_CLEAR_FARM, (datetime.utcnow(), telegram_id))
    except sqlite3.Error as Error:
        print(Error)
    connection.commit()
    connection.close()


def high_to_money(db_path, telegram_id, high, money):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(config.HIGH_TO_MONEY, (high, money, telegram_id))
    except sqlite3.Error as Error:
        print(Error)
    connection.commit()
    connection.close()


# def delete_my_data_from_game(db_path, telegram_id):
#     connection = create_connection(db_path=db_path)
#     cursor = connection.cursor()
#     cursor.execute("DELETE FROM users WHERE id = {id}".format(id=telegram_id))
#     cursor.execute("DELETE FROM balance WHERE id = {id}".format(id=telegram_id))
#     cursor.execute("DELETE FROM farm WHERE id = {id}".format(id=telegram_id))
#     connection.commit()
#     connection.close()
