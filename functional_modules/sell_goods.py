from random import choices, randint

from telegram import ParseMode

import config
import menu_bot as menu
import states as state
import sql
from functional_modules import utility


def sell_goods(update, _):
    update.message.reply_markdown(text=config.SELL_GOODS_DESC, reply_markup=menu.show(menu=config.SELL_GOODS))
    return state.SELL_GOODS


def dealer(update, _):
    (_, high, _) = sql.get_balance(db_path=config.DB_PATH, telegram_id=update.message.from_user.id)
    update.message.reply_markdown(text=config.DEALER_DESC.format(high=high), reply_markup=menu.show(menu=config.BACK))
    return state.DEALER


def dealer_result(update, _):
    try:
        high = int(update.message.text)
    except ValueError:
        update.message.reply_markdown(text=config.NOT_POSITIVE_NUMBER, reply_markup=menu.show(menu=config.BACK))
        return state.DEALER
    else:
        if high <= 0:
            update.message.reply_markdown(text=config.NOT_POSITIVE_NUMBER, reply_markup=menu.show(menu=config.BACK))
            return state.DEALER
        else:
            high_in_balance = sql.get_from_table(
                db_path=config.DB_PATH, telegram_id=update.message.chat.id, table="balance", field="high")
            if high > high_in_balance:
                update.message.reply_markdown(text=config.NOT_ENOUGH_HIGH.format(high=high_in_balance),
                                              reply_markup=menu.show(menu=config.BACK))
                return state.DEALER
            elif config.HIGH_MIN <= high <= config.HIGH_MAX:
                money = utility.money_transfer(high=high)
                sql.high_to_money(
                    db_path=config.DB_PATH, telegram_id=update.message.chat.id, high=update.message.text, money=money)
                if high < config.BID_1["HIGH"]:
                    update.message.reply_markdown(
                        text=config.BAD_HIGH_EXCHANGE.format(high=update.message.text, money=money),
                        reply_markup=menu.show(menu=config.SELL_GOODS))
                else:
                    update.message.reply_markdown(
                        text=config.HIGH_EXCHANGE.format(high=update.message.text, money=money),
                        reply_markup=menu.show(menu=config.SELL_GOODS))
                return state.SELL_GOODS
            else:
                sql.high_to_money(db_path=config.DB_PATH,
                                  telegram_id=update.message.chat.id,
                                  high=update.message.text,
                                  money=config.MONEY_MAX)
                update.message.reply_markdown(
                    text=config.HIGH_EXCHANGE.format(high=update.message.text, money=config.MONEY_MAX),
                    reply_markup=menu.show(menu=config.SELL_GOODS))
                return state.SELL_GOODS


def detention_notify(update, _):
    update.message.reply_markdown(text=config.STREET_DETENTION_NOTIFY, reply_markup=menu.show(menu=config.DETENTION))
    return state.STREET_DETENTION


def retention_notify(update, _):
    update.message.reply_markdown(text=config.STREET_RETENTION_NOTIFY, reply_markup=menu.show(menu=config.RETENTION))
    return state.STREET_RETENTION


def to_sell_goods(update, _):
    update.message.reply_markdown(text="", reply_markup=menu.show(menu=config.SELL_GOODS))
    return state.SELL_GOODS


def waiting_3_sec(context):
    context.bot.send_message(
        chat_id=context.job.context, text="_3..._", reply_markup=menu.no_menu(), parse_mode=ParseMode.MARKDOWN)


def waiting_2_sec(context):
    context.bot.send_message(
        chat_id=context.job.context, text="_2.._", reply_markup=menu.no_menu(), parse_mode=ParseMode.MARKDOWN)


def waiting_1_sec(context):
    context.bot.send_message(
        chat_id=context.job.context, text="_1._", reply_markup=menu.no_menu(), parse_mode=ParseMode.MARKDOWN)


def street_enter_high(update, _):
    (money, high, _) = sql.get_balance(db_path=config.DB_PATH, telegram_id=update.message.from_user.id)
    update.message.reply_markdown(
        text=config.STREET_ENTER_HIGH_TEXT.format(money=money, high=high), reply_markup=menu.show(menu=config.BACK))
    return state.STREET_ENTER_HIGH


def street_choice_place(update, context):
    chat_id = update.message.chat.id
    try:
        high = int(update.message.text)
    except ValueError:
        update.message.reply_markdown(text=config.STREET_NOT_EXPECTED_NUMBER, reply_markup=menu.show(menu=config.BACK))
        return state.STREET_ENTER_HIGH
    else:
        if high < config.MIN_HIGH_FOR_STREET:
            update.message.reply_markdown(
                text=config.STREET_NOT_EXPECTED_NUMBER, reply_markup=menu.show(menu=config.BACK))
            return state.STREET_ENTER_HIGH
        else:
            high_in_balance = sql.get_from_table(
                db_path=config.DB_PATH, telegram_id=chat_id, table="balance", field="high")
            money_in_balance = sql.get_from_table(
                db_path=config.DB_PATH, telegram_id=chat_id, table="balance", field="money")
            if (high_in_balance < high) or (money_in_balance < config.MIN_MONEY_FOR_STREET):
                update.message.reply_markdown(text=config.INSUFFICIENT_FUNDS, reply_markup=menu.show(menu=config.BACK))
                return state.STREET_ENTER_HIGH
            else:
                context.user_data["high"] = high
                context.user_data["money_in_balance"] = money_in_balance
                update.message.reply_markdown(
                    text=config.STREET_CHOICE_PLACE, reply_markup=menu.show(menu=config.STREET_PLACES))
                return state.STREET_CHOICE_PLACE


def street_first_event(context):
    if context.job.context[0] == "sell":
        (chat_id, sold_high, unsold_high, earned_money) = context.job.context[1::]
        context.bot.send_message(chat_id=chat_id,
                                 text=config.STREET_SELL_TEXT.format(
                                     money=earned_money, sold=sold_high, unsold=unsold_high
                                 ),
                                 reply_markup=menu.show(menu=config.SELL_GOODS),
                                 parse_mode=ParseMode.MARKDOWN)
    else:
        (chat_id, high, detention_chance, money_for_escape) = context.job.context[1::]
        context.bot.send_message(chat_id=chat_id,
                                 text=config.STREET_DETENTION_TEXT.format(
                                     high=high, money=money_for_escape, chance=detention_chance
                                 ),
                                 reply_markup=menu.show(menu=config.DETENTION),
                                 parse_mode=ParseMode.MARKDOWN)


def bribe(update, context):
    sql.bribe(db_path=config.DB_PATH,
              telegram_id=update.message.chat.id,
              money=context.user_data["money_for_escape"],
              high=context.user_data["high"])
    update.message.reply_markdown(text=config.STREET_BRIBE_TEXT, reply_markup=menu.show(menu=config.SELL_GOODS))
    return state.SELL_GOODS


def bribe_after_retention(update, context):
    sql.bribe(db_path=config.DB_PATH,
              telegram_id=update.message.chat.id,
              money=context.user_data["money_retention"],
              high=context.user_data["high"])
    update.message.reply_markdown(text=config.STREET_BRIBE_TEXT, reply_markup=menu.show(menu=config.SELL_GOODS))
    return state.SELL_GOODS


def street_second_event(context):
    if len(context.job.context) == 3:
        (chat_id, money_retention, high) = context.job.context
        context.bot.send_message(chat_id=chat_id,
                                 text=config.STREET_RETENTION_TEXT.format(
                                             high=high, money=money_retention),
                                 reply_markup=menu.show(menu=config.RETENTION),
                                 parse_mode=ParseMode.MARKDOWN)
    else:
        context.bot.send_message(chat_id=context.job.context[0],
                                 text=config.STREET_ESCAPE_TEXT,
                                 reply_markup=menu.show(menu=config.SELL_GOODS),
                                 parse_mode=ParseMode.MARKDOWN)


def street(update, context):
    update.message.reply_markdown(
        text=config.STREET_START_TEXT.format(high=context.user_data["high"]), reply_markup=menu.no_menu())

    context.job_queue.run_once(callback=waiting_3_sec, when=2, context=update.message.chat_id)
    context.job_queue.run_once(callback=waiting_2_sec, when=2.5, context=update.message.chat_id)
    context.job_queue.run_once(callback=waiting_1_sec, when=3.25, context=update.message.chat_id)

    weights, price, escape_weights = [], 0, []
    for place in config.PLACES:
        if place["NAME"] == update.message.text:
            weights, price, escape_weights = place["PROB"], place["PRICE"], place["ESCAPE"]

    if choices(population=config.FIRST_EVENT, weights=weights, k=1) == ["sell"]:
        sold_high, unsold_high, earned_money = utility.street_exchange(high=context.user_data["high"], price=price)
        sql.high_to_money(
            db_path=config.DB_PATH, telegram_id=update.message.chat.id, high=sold_high, money=earned_money)
        context.job_queue.run_once(
            callback=street_first_event,
            when=4.5,
            context=("sell", update.message.chat.id, sold_high, unsold_high, earned_money)
        )
        return state.SELL_GOODS
    else:
        detention_chance = randint(a=escape_weights[0], b=escape_weights[1])
        money_for_escape = utility.money_for_escape(money=context.user_data["money_in_balance"])
        context.user_data["detention_chance"] = detention_chance
        context.user_data["money_for_escape"] = money_for_escape
        context.job_queue.run_once(
            callback=street_first_event,
            when=4.5,
            context=("detention", update.message.chat.id, context.user_data["high"], detention_chance, money_for_escape)
        )
        return state.STREET_DETENTION


def escape(update, context):
    context.job_queue.run_once(callback=waiting_3_sec, when=0.5, context=update.message.chat_id)
    context.job_queue.run_once(callback=waiting_2_sec, when=1, context=update.message.chat_id)
    context.job_queue.run_once(callback=waiting_1_sec, when=1.25, context=update.message.chat_id)

    weights = [100 - context.user_data["detention_chance"], context.user_data["detention_chance"]]
    if choices(population=config.SECOND_EVENT, weights=weights, k=1) == ["escape"]:
        sql.escape(
            db_path=config.DB_PATH, telegram_id=update.message.chat.id, money=context.user_data["money_for_escape"])
        context.job_queue.run_once(callback=street_second_event, when=1.5, context=(update.message.chat_id,))
        return state.SELL_GOODS
    else:
        money_retention = utility.money_retention(money=context.user_data["money_for_escape"])
        context.user_data["money_retention"] = money_retention
        high = context.user_data["high"]
        context.job_queue.run_once(
            callback=street_second_event, when=1.5, context=(update.message.chat_id, money_retention, high))
        return state.STREET_RETENTION
