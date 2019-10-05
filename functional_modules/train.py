from re import findall
from telegram import ParseMode

import config
import menu_bot as menu
import sql
import states as state


def check_nick(nickname):
    return bool(len(nickname) in range(5, 20) and nickname == "".join(findall(pattern=config.PATTERN_NICK,
                                                                              string=nickname)))


def to_desc_1(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=config.TRAIN_DESC_1_TEXT,
                             reply_markup=menu.show(menu=config.TRAIN_DESC_1),
                             parse_mode=ParseMode.MARKDOWN)


def to_market(update, context):
    context.bot.send_photo(chat_id=update.message.chat.id,
                           photo=open(file=config.XS["PATH"], mode='rb'),
                           caption=config.HIGH_GROWING_CAPTION.format(about=config.XS["DESC"],
                                                                      name=config.XS["NAME"],
                                                                      mining=config.XS["MINING"],
                                                                      price=config.XS["PRICE"]),
                           reply_markup=menu.show(menu=config.TRAIN_MARKET),
                           parse_mode=ParseMode.MARKDOWN)
    return state.TRAIN_MARKET


def to_desc_2(update, context):
    sql.buying_grow_box(db_path=config.DB_PATH,
                        telegram_id=update.message.chat.id,
                        name=config.XS["SIZE"],
                        price=str(config.XS["PRICE"]))
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=config.TRAIN_DESC_2_TEXT,
                             reply_markup=menu.show(menu=config.TRAIN_DESC_2),
                             parse_mode=ParseMode.MARKDOWN)
    return state.TRAIN_DESC_2


def to_nick(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=config.TRAIN_NICK_TEXT,
                             reply_markup=menu.no_menu(),
                             parse_mode=ParseMode.MARKDOWN)
    return state.TRAIN_NICK


def nick_valid(update, context):
    if check_nick(nickname=update.message.text):
        if sql.update_nick(db_path=config.DB_PATH, nick=update.message.text, telegram_id=update.message.chat.id):
            context.bot.send_message(chat_id=update.message.chat.id,
                                     text=config.TRAIN_NICK_VALID_TEXT,
                                     reply_markup=menu.show(menu=config.MAIN),
                                     parse_mode=ParseMode.MARKDOWN)
            return state.MAIN
        else:
            context.bot.send_message(chat_id=update.message.chat.id,
                                     text=config.TRAIN_NICK_NOT_VALID_TEXT,
                                     reply_markup=menu.no_menu(),
                                     parse_mode=ParseMode.MARKDOWN)
            return state.TRAIN_NICK
    else:
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text=config.TRAIN_NICK_ERROR_TEXT,
                                 parse_mode=ParseMode.MARKDOWN)
        return state.TRAIN_NICK
