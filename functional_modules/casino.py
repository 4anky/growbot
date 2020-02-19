from datetime import datetime, timedelta
from random import choice, shuffle
from time import sleep

from telegram import ParseMode
from telegram.error import BadRequest

from functional_modules import utility
import config
import menu_bot as menu
import sql
import states as state
import text


def casino(update, context):
    if context.user_data["in_game_flag"] is not None:
        return state.TWENTY_ONE
    update.message.reply_markdown(text=text.CASINO_DESC, reply_markup=menu.show(menu=text.CASINO))
    return state.CASINO


def twenty_one(update, _):
    update.message.reply_markdown(text=text.TWENTY_ONE_DESC, reply_markup=menu.show(menu=text.TWENTY_ONE))
    return state.TWENTY_ONE


def dice(update, _):
    update.message.reply_markdown(text=text.CASINO_DESC, reply_markup=menu.show(menu=text.CASINO))
    return state.CASINO


def exchange(update, _):
    update.message.reply_markdown(text=text.EXCHANGE_DESC, reply_markup=menu.show(menu=text.EXCHANGE))
    return state.EXCHANGE


def enter_money(update, context):
    money, _, chip = sql.get_balance(telegram_id=update.message.chat.id)
    context.user_data["money"] = money
    update.message.reply_markdown(
        text=text.MONEY_TO_CHIP_TEXT.format(money=money, chip=chip), reply_markup=menu.show(menu=text.BACK))
    return state.TO_CHIP


def money_to_chips(update, context):
    try:
        money_for_exchange = int(update.message.text)
    except ValueError:
        update.message.reply_markdown(text=text.NOT_POSITIVE_NUMBER, reply_markup=menu.show(menu=text.BACK))
        return state.TO_CHIP
    else:
        if money_for_exchange <= 0:
            update.message.reply_markdown(text=text.NOT_POSITIVE_NUMBER, reply_markup=menu.show(menu=text.BACK))
            return state.TO_CHIP
        elif money_for_exchange > context.user_data["money"]:
            update.message.reply_markdown(text=text.NOT_ENOUGH_MONEY.format(money=context.user_data["money"]))
            return state.TO_CHIP
        else:
            chips = money_for_exchange * config.CHIPS_FOR_CURRENCY_UNIT - config.COMMISSION
            sql.money_to_chips(telegram_id=update.message.chat.id, money=money_for_exchange, chip=chips)
            money, _, chip = sql.get_balance(telegram_id=update.message.chat.id)
            update.message.reply_markdown(
                text=text.BUY_CHIPS.format(new=chips, money=money, chip=chip),
                reply_markup=menu.show(menu=text.EXCHANGE))
            return state.EXCHANGE


def enter_chip(update, context):
    money, _, chip = sql.get_balance(telegram_id=update.message.chat.id)
    context.user_data["chip"] = chip
    update.message.reply_markdown(
        text=text.CHIP_TO_MONEY_TEXT.format(money=money, chip=chip), reply_markup=menu.show(menu=text.BACK))
    return state.TO_MONEY


def chips_to_money(update, context):
    try:
        chips_for_exchange = int(update.message.text)
    except ValueError:
        update.message.reply_markdown(text=text.NOT_POSITIVE_NUMBER, reply_markup=menu.show(menu=text.BACK))
        return state.TO_MONEY
    else:
        if chips_for_exchange <= config.COMMISSION:
            update.message.reply_markdown(text=text.LESS_THAN_COMMISSION, reply_markup=menu.show(menu=text.BACK))
            return state.TO_MONEY
        elif chips_for_exchange > context.user_data["chip"]:
            update.message.reply_markdown(text=text.NOT_ENOUGH_CHIP.format(chip=context.user_data["chip"]))
            return state.TO_MONEY
        else:
            new_money = (chips_for_exchange - config.COMMISSION) // config.CHIPS_FOR_CURRENCY_UNIT
            changed_chips = new_money * config.CHIPS_FOR_CURRENCY_UNIT
            # unchanged_chips = (chips_for_exchange - config.COMMISSION) % config.CHIPS_FOR_CURRENCY_UNIT
            sql.chips_to_money(
                telegram_id=update.message.chat.id,
                money=new_money,
                chip=changed_chips + config.COMMISSION)
            money, _, chip = sql.get_balance(telegram_id=update.message.chat.id)
            update.message.reply_markdown(
                text=text.SELL_CHIPS.format(new=new_money, money=money, chip=chip),
                reply_markup=menu.show(menu=text.EXCHANGE))
            return state.EXCHANGE


def lottery_entrance(update, _):
    update.message.reply_markdown(text=text.LOTTERY_DESC, reply_markup=menu.show(menu=text.LOTTERY))
    return state.LOTTERY


def buy_and_watch(update, context):
    context.user_data["TICKET_NAME"] = update.message.text
    for i, ticket in enumerate(config.TICKETS):
        ticket["NAME"] = text.TICKETS_NAME[i]
        if ticket["NAME"] == update.message.text:
            context.user_data["TICKET_PRICE"] = ticket['PRICE']
            update.message.reply_markdown(
                text=text.BUY_AND_WATCH_TEXT.format(name=ticket['NAME'], price=text.three_digits(n=ticket['PRICE'])),
                reply_markup=menu.show(menu=text.BUY_AND_WATCH))
            break
    return state.BUY_AND_WATCH


def buy_ticket(update, context):
    name, price = context.user_data['TICKET_NAME'], context.user_data['TICKET_PRICE']

    if (datetime.now().hour == config.LOTTERY_TIME.hour) \
            and (abs(datetime.now().minute - config.LOTTERY_TIME.minute) < config.LOTTERY_BREAK):
        update.message.reply_markdown(text=text.AROUND_LOTTERY_TEXT)
        return state.BUY_AND_WATCH
    money_in_balance = sql.get_from_table(telegram_id=update.message.chat.id, table="balance", field="money")
    if money_in_balance < price:
        update.message.reply_markdown(text=text.PURCHASE_ERROR)
        return state.BUY_AND_WATCH
    if sql.check_lottery_ticket(telegram_id=update.message.chat.id, name=name, time=utility.get_last_lottery_time()):
        update.message.reply_markdown(text=text.ALREADY_PURCHASED)
        return state.BUY_AND_WATCH

    sql.buying_lottery_ticket(telegram_id=update.message.chat.id, price=price, name=name)
    update.message.reply_markdown(text=text.BUYING_TICKET.format(name=name, price=text.three_digits(n=price)))
    return state.BUY_AND_WATCH


def watch_translation(update, context):
    name, price = context.user_data['TICKET_NAME'], context.user_data['TICKET_PRICE']
    next_lottery_time = (utility.get_last_lottery_time() + timedelta(days=1, hours=3)).strftime('%d.%m.%Y %H:%M')
    players = [player[0] for player in sql.lottery_translation(time=utility.get_last_lottery_time(), name=name)]
    if not players:
        update.message.reply_markdown(text=text.NULL_PLAYERS.format(name=name, next_time=next_lottery_time))
    else:
        players_list = '\n'.join([f'       • {player}' for player in players])
        update.message.reply_markdown(
            text=text.PLAYERS_LIST.format(name=name,
                                          number=text.three_digits(n=len(players)),
                                          players=players_list,
                                          prize=text.three_digits(n=len(players) * price),
                                          next_time=next_lottery_time)
        )
    return state.BUY_AND_WATCH


def lottery(context):
    (NICK, ID, TIME, _, _) = (0, 1, 2, 3, 4)
    tickets_data = {name: price_dict for name, price_dict in zip(text.TICKETS_NAME, config.TICKETS)}

    lottery_data = sql.lottery(time=utility.get_lottery_time_yesterday())
    for ticket_name in lottery_data.keys():
        if lottery_data[ticket_name]:
            shuffle(lottery_data[ticket_name])
            winner = choice(lottery_data[ticket_name])
            prize = len(lottery_data[ticket_name]) * tickets_data[ticket_name]['PRICE']
            sql.save_winner_and_get_prize(telegram_id=winner[ID], time=winner[TIME], prize=prize)
            for player in lottery_data[ticket_name]:
                message = (text.LOSERS_MESSAGE if player != winner else text.WINNER_MESSAGE).format(
                    name=ticket_name, winner=winner[NICK], prize=text.three_digits(n=prize))
                try:
                    context.bot.send_message(chat_id=player[ID], text=message, parse_mode=ParseMode.MARKDOWN)
                except BadRequest:
                    pass
        sleep(5)
