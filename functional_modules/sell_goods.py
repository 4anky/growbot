from telegram import ParseMode

import config
import menu_bot as menu
import states as state
import sql
from functional_modules import utility


def sell_goods(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=config.SELL_GOODS_DESC,
                             reply_markup=menu.show(menu=config.SELL_GOODS),
                             parse_mode=ParseMode.MARKDOWN)
    return state.SELL_GOODS


def dealer(update, context):
    (_, high, _) = sql.get_balance(db_path=config.DB_PATH, telegram_id=update.message.from_user.id)
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=config.DEALER_DESC.format(high=high),
                             reply_markup=menu.show(menu=config.BACK),
                             parse_mode=ParseMode.MARKDOWN)
    return state.DEALER


def dealer_result(update, context):
    try:
        high = int(update.message.text)
    except ValueError:
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text=config.NOT_POSITIVE_NUMBER,
                                 reply_markup=menu.show(menu=config.BACK),
                                 parse_mode=ParseMode.MARKDOWN)
        return state.DEALER
    else:
        if high <= 0:
            context.bot.send_message(chat_id=update.message.chat.id,
                                     text=config.NOT_POSITIVE_NUMBER,
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
                                         text=config.NOT_ENOUGH_HIGH.format(high=high_in_balance),
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


def street_enter_high(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=config.STREET_ENTER_HIGH_TEXT,
                             reply_markup=menu.show(menu=config.BACK),
                             parse_mode=ParseMode.MARKDOWN)
    return state.STREET_ENTER_HIGH


def street_choice_place(update, context):
    try:
        high = int(update.message.text)
    except ValueError:
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text=config.STREET_NOT_EXPECTED_NUMBER,
                                 reply_markup=menu.show(menu=config.BACK),
                                 parse_mode=ParseMode.MARKDOWN)
        return state.STREET_ENTER_HIGH
    else:
        if high < config.MIN_HIGH_FOR_STREET:
            context.bot.send_message(chat_id=update.message.chat.id,
                                     text=config.STREET_NOT_EXPECTED_NUMBER,
                                     reply_markup=menu.show(menu=config.BACK),
                                     parse_mode=ParseMode.MARKDOWN)
            return state.STREET_ENTER_HIGH
        else:
            high_in_balance = sql.get_from_table(db_path=config.DB_PATH,
                                                 telegram_id=update.message.chat.id,
                                                 table="balance",
                                                 field="high")
            if high > high_in_balance:
                context.bot.send_message(chat_id=update.message.chat.id,
                                         text=config.NOT_ENOUGH_HIGH.format(high=high_in_balance),
                                         reply_markup=menu.show(menu=config.BACK),
                                         parse_mode=ParseMode.MARKDOWN)
                return state.STREET_ENTER_HIGH
            else:
                context.user_data[update.message.chat.id] = high
                context.bot.send_message(chat_id=update.message.chat.id,
                                         text=config.STREET_CHOICE_PLACE,
                                         reply_markup=menu.show(menu=config.STREET_PLACES),
                                         parse_mode=ParseMode.MARKDOWN)
                return state.STREET_CHOICE_PLACE


def street(update, context):
    high = context.user_data[update.message.chat.id]
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=("Вы выбрали {choice} "
                                   + "и на кармане у Вас {high}🌳").format(choice=update.message.text, high=high),
                             reply_markup=menu.show(menu=config.STREET_PLACES),
                             parse_mode=ParseMode.MARKDOWN)
    return state.STREET_CHOICE_PLACE
