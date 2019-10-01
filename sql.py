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


def is_developer(db_path):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(config.WAIT_GET_USERS)
    except sqlite3.Error as Error:
        print(Error)
    ids = cursor.fetchall()
    connection.close()
    return ids


def add_to_waiting_users(db_path, telegram_id):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(config.WAIT_ADD, (telegram_id,))
    except sqlite3.Error as Error:
        print(Error)
    connection.commit()
    connection.close()


def is_wait_user(db_path, telegram_id):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(config.WAIT_IS_ADD, (telegram_id,))
    except sqlite3.Error as Error:
        print(Error)
    result = cursor.fetchone()
    connection.commit()
    connection.close()
    return result


def reg(db_path, telegram_id, first_name, username):
    connection = create_connection(db_path=db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(config.REG_USERS, (telegram_id, first_name, username))
        cursor.execute(config.REG_FARM,
                       (telegram_id, config.START_XS_GROW_BOX, config.START_GROW_BOX, config.START_GROW_BOX,
                        config.START_GROW_BOX, config.START_GROW_BOX, config.START_GROW_BOX, datetime.utcnow()))
        cursor.execute(config.REG_BALANCE, (telegram_id, config.START_MONEY, config.START_HIGH))
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
