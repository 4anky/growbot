from datetime import datetime, timedelta
import sqlite3

import config
import text


DB_PATH = "data/data.db"
NEW_TABLE_PATH = "materials/new_table.txt"

REG_USERS = "INSERT OR IGNORE INTO users VALUES (?, ?)"
REG_BALANCE = "INSERT OR IGNORE INTO balance VALUES (?, ?, ?, ?, ?)"
REG_FARM = "INSERT OR IGNORE INTO farm VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
REG_FARM_AMENDMENTS = "INSERT OR IGNORE INTO farm_amendments VALUES (?, ?, ?, ?, ?, ?, ?)"
ADD_REFERRAL = "INSERT OR IGNORE INTO ref_system VALUES (?, ?, ?)"
BUYING_LOTTERY_TICKET = "INSERT INTO lottery VALUES (?, ?, ?, ?)"

GET_ALL_TABLE_NAMES = "SELECT tbl_name FROM sqlite_master WHERE type = 'table'"
GET_BALANCE = "SELECT money, high, chip FROM balance WHERE id = ?"
GET_ALL_FARM = ("SELECT f.XS, f.S, f.M, f.L, f.XL, f.XXL, fa.XS, fa.S, fa.M, fa.L, fa.XL, fa.XXL, f.last_collect "
                + "FROM farm AS f JOIN farm_amendments AS fa ON f.id = fa.id WHERE f.id = ?")
GET_FROM_TABLE = "SELECT {field} FROM {table} WHERE id = ?"
GET_RATING = ("SELECT users.nick, balance.{param} FROM users JOIN balance ON users.id = balance.id "
              + "WHERE harvest_sum > 0 ORDER BY {param} DESC LIMIT 15")
IS_REG = "SELECT * FROM users WHERE id = ?"
GET_DEV_ID = "SELECT * FROM dev"
GET_USERS_TABLE = "SELECT * FROM users"
GET_PLAYERS_NUMBER = "SELECT COUNT(id) FROM users"
GET_COMPLETED_REFERRALS = ("SELECT referral, nick "
                           + "FROM ref_system AS ref "
                           + "JOIN balance AS b ON ref.referral = b.id "
                           + "JOIN users ON ref.referral = users.id "
                           + "WHERE ref.referrer = ? AND ref.task = 0 AND b.harvest_sum > 0")
GET_SAFER_STREET_END = "SELECT safer_street FROM paid WHERE id = ?"
GET_PLAYERS_FOR_TRANSLATION = ("SELECT u.nick, l.id, l.buy_time, l.type, l.status FROM users AS u JOIN lottery AS l "
                               + "ON u.id = l.id WHERE l.buy_time > ? AND l.type = ?")
GET_LOTTERY_PLAYERS = ("SELECT u.nick, l.id, l.buy_time, l.type, l.status FROM users AS u JOIN lottery AS l"
                       + " ON u.id = l.id WHERE l.buy_time > ? ORDER BY l.type")
CHECK_LOTTERY_TICKETS = "SELECT * FROM lottery WHERE id  = ? AND buy_time >= ? AND type = ? AND status = 0"

UPDATE_NICK = "UPDATE users SET nick = ? WHERE id = ?"
TO_ZERO_FARM_AMENDMENTS = "UPDATE farm_amendments SET XS = 0, S = 0, M = 0, L = 0, XL = 0, XXL = 0 WHERE id = ?"
UPDATE_FARM_AMENDMENTS = "UPDATE farm_amendments SET {size} = {size} + {value} WHERE id = ?"
BUYING_GROW_BOX = "UPDATE farm SET {name} = {name} + 1 WHERE id = ?"
PAYING_MONEY = "UPDATE balance SET money = money - {price} WHERE id = ?"
HIGH_TO_BALANCE = "UPDATE balance SET high = high + {high}, harvest_sum = harvest_sum + {high} WHERE id = ?"
HIGH_TO_BALANCE_CLEAR_FARM = "UPDATE farm SET last_collect = ? WHERE id = ?"
HIGH_TO_MONEY = "UPDATE balance SET high = high - ?, money = money + ? WHERE id = ?"
ESCAPE = "UPDATE balance SET money = money - ? WHERE id = ?"
BRIBE = "UPDATE balance SET money = money - ?, high = high - ? WHERE id = ?"
UPDATE_REF_SYSTEM = "UPDATE ref_system SET task = 1 WHERE referral = ?"
REFERRAL_TO_MONEY = "UPDATE balance SET money = money + ? WHERE id = ?"
MONEY_TO_CHIP = "UPDATE balance SET money = money - ?, chip = chip + ? WHERE id = ?"
CHIP_TO_MONEY = "UPDATE balance SET chip = chip - ?, money = money + ? WHERE id = ?"
SAFER_STREET = "UPDATE paid SET safer_street = ? WHERE id = ?"
SAVE_WINNER = "UPDATE lottery SET status = ? WHERE id = ? AND buy_time = ?"
GET_PRIZE = "UPDATE balance SET money = money + ? WHERE id = ?"


def create_connection():
    connect = None
    try:
        connect = sqlite3.connect(database=DB_PATH, detect_types=sqlite3.PARSE_DECLTYPES)
    except sqlite3.Error as Error:
        print(Error)
    return connect


def reg(telegram_id):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(REG_USERS, (telegram_id, str(telegram_id)))
        cursor.execute(REG_BALANCE,
                       (telegram_id, config.START_MONEY, config.START_HIGH, config.START_CHIP, config.START_HARVEST_SUM)
                       )
        cursor.execute(REG_FARM,
                       (telegram_id, config.START_GROW_BOX, config.START_GROW_BOX, config.START_GROW_BOX,
                        config.START_GROW_BOX, config.START_GROW_BOX, config.START_GROW_BOX, datetime.utcnow()))
        cursor.execute(REG_FARM_AMENDMENTS,
                       (telegram_id, config.START_GROW_BOX, config.START_GROW_BOX, config.START_GROW_BOX,
                        config.START_GROW_BOX, config.START_GROW_BOX, config.START_GROW_BOX))
    except sqlite3.Error as Error:
        print(Error)
    finally:
        connection.commit()
        connection.close()


def is_reg(telegram_id):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(IS_REG, (telegram_id, ))
    except sqlite3.Error as Error:
        print(Error)
    result = cursor.fetchone()
    connection.close()
    return result


def update_nick(nick, telegram_id):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(UPDATE_NICK, (nick, telegram_id))
    except sqlite3.IntegrityError:
        result = False
    else:
        result = True
    finally:
        connection.commit()
        connection.close()
    return result


def get_balance(telegram_id):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(GET_BALANCE, (telegram_id,))
    except sqlite3.Error as Error:
        print(Error)
    result = cursor.fetchone()
    connection.close()
    return result


def get_from_table(telegram_id, table, field):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(GET_FROM_TABLE.format(field=field, table=table), (telegram_id,))
    except sqlite3.Error as Error:
        print(Error)
    answer = cursor.fetchone()
    [result] = [answer[0] if answer is not None else answer]
    connection.close()
    return result


def get_all_farm(telegram_id):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(GET_ALL_FARM, (telegram_id,))
    except sqlite3.Error as Error:
        print(Error)
    else:
        result = cursor.fetchone()
        if result:
            return result[:6], result[6:12], result[-1]
    finally:
        connection.close()


def to_zero_farm_amendments(telegram_id):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(TO_ZERO_FARM_AMENDMENTS, (telegram_id,))
    except sqlite3.Error as Error:
        print(Error)
    else:
        connection. commit()
    finally:
        connection.close()


def update_farm_amendments(telegram_id, size, value):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(UPDATE_FARM_AMENDMENTS.format(size=size, value=value), (telegram_id,))
    except sqlite3.Error as Error:
        print(Error)
    else:
        connection.commit()
    finally:
        connection.close()


def buying_grow_box(telegram_id, name, price):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(BUYING_GROW_BOX.format(name=name), (telegram_id, ))
        cursor.execute(PAYING_MONEY.format(price=price), (telegram_id, ))
    except sqlite3.Error as Error:
        print(Error)
    finally:
        connection.commit()
        connection.close()


def high_to_balance(telegram_id, high):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(HIGH_TO_BALANCE.format(high=high), (telegram_id, ))
        cursor.execute(HIGH_TO_BALANCE_CLEAR_FARM, (datetime.utcnow(), telegram_id))
    except sqlite3.Error as Error:
        print(Error)
    finally:
        connection.commit()
        connection.close()


def high_to_money(telegram_id, high, money):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(HIGH_TO_MONEY, (high, money, telegram_id))
    except sqlite3.Error as Error:
        print(Error)
    else:
        connection.commit()
    finally:
        connection.close()


def get_rating(param):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(GET_RATING.format(param=param))
    except sqlite3.Error as Error:
        print(Error)
    finally:
        result = cursor.fetchall()
        connection.close()
        return result


def bribe(telegram_id, money, high):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(BRIBE, (money, high, telegram_id))
    except sqlite3.Error as Error:
        print(Error)
    else:
        connection.commit()
    finally:
        connection.close()


def escape(telegram_id, money):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(ESCAPE, (money, telegram_id))
    except sqlite3.Error as Error:
        print(Error)
    else:
        connection.commit()
    finally:
        connection.close()


def get_dev_id():
    connection = create_connection()
    cursor = connection.cursor()
    result = []
    try:
        cursor.execute(GET_DEV_ID)
    except sqlite3.Error as Error:
        print(Error)
    else:
        for line in cursor.fetchall():
            result.append(line[0])
    finally:
        connection.close()
        return result


def get_players_number():
    connection = create_connection()
    cursor = connection.cursor()
    result = 0
    try:
        cursor.execute(GET_PLAYERS_NUMBER)
    except sqlite3.Error as Error:
        print(Error)
    else:
        result = cursor.fetchone()[result]
    finally:
        connection.close()
        return result


def add_referral(referrer, referral):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(ADD_REFERRAL, (referrer, referral, 0))
    except sqlite3.Error as Error:
        print(Error)
    else:
        connection.commit()
    finally:
        connection.close()


def get_completed_referrals(referrer):
    connection = create_connection()
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(GET_COMPLETED_REFERRALS, (referrer,))
    except sqlite3.Error as Error:
        print(Error)
    else:
        result = cursor.fetchall()
    finally:
        connection.close()
    return result


def add_completed_referral(referrer, referral):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(UPDATE_REF_SYSTEM, (referral,))
        cursor.execute(REFERRAL_TO_MONEY, (config.PRICE_FOR_REFERRAL, referrer))
    except sqlite3.Error as Error:
        print(Error)
    else:
        connection.commit()
    finally:
        connection.close()


def money_to_chips(telegram_id, money, chip):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(MONEY_TO_CHIP, (money, chip, telegram_id))
    except sqlite3.Error as Error:
        print(Error)
    else:
        connection.commit()
    finally:
        connection.close()


def chips_to_money(telegram_id, money, chip):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(CHIP_TO_MONEY, (chip, money, telegram_id))
    except sqlite3.Error as Error:
        print(Error)
    else:
        connection.commit()
    finally:
        connection.close()


def get_users_table():
    connection = create_connection()
    cursor = connection.cursor()
    result = []
    try:
        cursor.execute(GET_USERS_TABLE)
    except sqlite3.Error as Error:
        print(Error)
    else:
        for user in cursor.fetchall():
            result.append(user)
    finally:
        connection.close()
    return result


def get_all_tables_name():
    connection = create_connection()
    cursor = connection.cursor()
    all_table_names = []
    try:
        cursor.execute(GET_ALL_TABLE_NAMES)
    except sqlite3.Error as Error:
        print(Error)
    else:
        all_table_names = [table[0] for table in cursor.fetchall()]
    finally:
        connection.close()
    return all_table_names


def create_new_table():
    create = open(file=NEW_TABLE_PATH, mode='r').read()
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(create)
    connection.commit()
    connection.close()


def safer_street(telegram_id, duration):
    connection = create_connection()
    cursor = connection.cursor()
    new_time_to_db = max(
        datetime.today(),
        get_from_table(telegram_id=telegram_id, table="paid", field="safer_street")
    ) + timedelta(days=duration)
    try:
        cursor.execute(SAFER_STREET, (new_time_to_db, telegram_id))
        connection.commit()
    finally:
        connection.close()
        return new_time_to_db


def check_lottery_ticket(telegram_id, name, time):
    connection = create_connection()
    cursor = connection.cursor()
    answer = bool
    try:
        cursor.execute(CHECK_LOTTERY_TICKETS, (telegram_id, time, name))
    except sqlite3.Error as Error:
        print(Error)
    else:
        answer = False if not cursor.fetchone() else True
    finally:
        connection.close()
    return answer


def buying_lottery_ticket(telegram_id, price, name):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(PAYING_MONEY.format(price=price), (telegram_id, ))
        cursor.execute(BUYING_LOTTERY_TICKET, (telegram_id, datetime.now(), name, 0))
    except sqlite3.Error as Error:
        print(Error)
    finally:
        connection.commit()
        connection.close()


def lottery_translation(time, name):
    connection = create_connection()
    cursor = connection.cursor()
    answer = []
    try:
        cursor.execute(GET_PLAYERS_FOR_TRANSLATION, (time, name))
    except sqlite3.Error as Error:
        print(Error)
    else:
        answer = [player for player in cursor.fetchall()]
    finally:
        connection.close()
    return answer


def lottery(time):
    connection = create_connection()
    cursor = connection.cursor()
    answer = {ticket_name: [] for ticket_name in text.TICKETS_NAME}
    try:
        cursor.execute(GET_LOTTERY_PLAYERS, (time,))
    except sqlite3.Error as Error:
        print(Error)
    else:
        for ticket in cursor.fetchall():
            answer[ticket[3]].append(ticket)
    finally:
        connection.close()
    return answer


def save_winner_and_get_prize(telegram_id, time, prize, status=1):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(SAVE_WINNER, (status, telegram_id, time))
        cursor.execute(GET_PRIZE, (prize, telegram_id))
    except sqlite3.Error as Error:
        print(Error)
    else:
        connection.commit()
    finally:
        connection.close()
