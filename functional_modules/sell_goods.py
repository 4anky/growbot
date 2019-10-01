from telegram import ParseMode

import config
import menu_bot as menu
import states as state
import sql
from functional_modules import utility


def sell_goods(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="*⚖️Продажа*\n\nВы можете продать 🌳"
                                  " двумя способами: через 👳🏻‍♂*дилера-поср"
                                  "едника* и самостоятельно на 🌃*Улице*. Ра"
                                  "бота с дилером имеет минимальные риски"
                                  ", но на Улице вы можете заработать гора"
                                  "здо больше💰!",
                             reply_markup=menu.show(menu=config.SELL_GOODS),
                             parse_mode=ParseMode.MARKDOWN)
    return state.SELL_GOODS


def dealer(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=config.DEALER_DESC,
                             reply_markup=menu.show(menu=config.BACK),
                             parse_mode=ParseMode.MARKDOWN)
    return state.DEALER


def dealer_result(update, context):
    try:
        high = int(update.message.text)
    except ValueError:
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text="Ожидается *целое положительное число*. Введите его:",
                                 reply_markup=menu.show(menu=config.BACK),
                                 parse_mode=ParseMode.MARKDOWN)
        return state.DEALER
    else:
        if high <= 0:
            context.bot.send_message(chat_id=update.message.chat.id,
                                     text="Ожидается *целое положительное число*. Введите его:",
                                     reply_markup=menu.show(menu=config.BACK),
                                     parse_mode=ParseMode.MARKDOWN)
            return state.DEALER
        else:
            high_in_balance = sql.get_from_table(db_path=config.DB_PATH,
                                                 telegram_id=update.message.chat.id,
                                                 table="balance",
                                                 field="high")
            if high > high_in_balance:
                context.bot.send_message(chat_id=update.message.chat.id,
                                         text="У вас есть только *{high}* шишек. "
                                              "Введите число не более *{high}*:".format(high=high_in_balance),
                                         reply_markup=menu.show(menu=config.BACK),
                                         parse_mode=ParseMode.MARKDOWN)
                return state.DEALER
            elif config.HIGH_MIN <= high <= config.HIGH_MAX:
                money = utility.money_transfer(high=high)
                sql.high_to_money(db_path=config.DB_PATH,
                                  telegram_id=update.message.chat.id,
                                  high=update.message.text,
                                  money=money)
                if high < config.BID_1["HIGH"]:
                    context.bot.send_message(chat_id=update.message.chat.id,
                                             text=config.BAD_HIGH_EXCHANGE.format(high=update.message.text,
                                                                                  money=money),
                                             reply_markup=menu.show(menu=config.SELL_GOODS),
                                             parse_mode=ParseMode.MARKDOWN)
                else:
                    context.bot.send_message(chat_id=update.message.chat.id,
                                             text=config.HIGH_EXCHANGE.format(high=update.message.text,
                                                                              money=money),
                                             reply_markup=menu.show(menu=config.SELL_GOODS),
                                             parse_mode=ParseMode.MARKDOWN)
                return state.SELL_GOODS
            else:
                sql.high_to_money(db_path=config.DB_PATH,
                                  telegram_id=update.message.chat.id,
                                  high=update.message.text,
                                  money=config.MONEY_MAX)
                context.bot.send_message(chat_id=update.message.chat.id,
                                         text=config.HIGH_EXCHANGE.format(high=update.message.text,
                                                                          money=config.MONEY_MAX),
                                         reply_markup=menu.show(menu=config.SELL_GOODS),
                                         parse_mode=ParseMode.MARKDOWN)
                return state.SELL_GOODS


def street(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Вы нажали кнопку 'Улица'",
                             reply_markup=menu.show(menu=config.SELL_GOODS))
    return state.SELL_GOODS
