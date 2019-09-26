from telegram import ParseMode

import config
import menu_bot as menu
import sql
import states as state


def markets(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Вы перешли в меню 'Магазин'",
                             reply_markup=menu.show(menu=config.MARKETS))
    return state.MARKETS


def high_growing(update, context):
    [context.bot.send_photo(chat_id=update.message.chat.id,
                            photo=open(file=size["PATH"], mode='rb'),
                            caption=config.HIGH_GROWING_CAPTION.format(about=size["DESC"],
                                                                       name=size["NAME"],
                                                                       mining=size["MINING"],
                                                                       price=size["PRICE"]),
                            reply_markup=menu.high_growing_buy_button(text=config.BUY_BUTTON,
                                                                      name=size["NAME"]),
                            parse_mode=ParseMode.MARKDOWN)
     for size in config.SIZES]
    return state.MARKETS


def buy_grow_box(update, context):
    money = sql.get_from_table(db_path=config.DB_PATH,
                               telegram_id=update.callback_query.message.chat.id,
                               field="money",
                               table="balance")
    [grow_box] = [size for size in config.SIZES if size["NAME"] == update.callback_query.data]
    if money >= grow_box["PRICE"]:
        sql.buying_grow_box(db_path=config.DB_PATH,
                            telegram_id=update.callback_query.message.chat.id,
                            name=grow_box["SIZE"],
                            price=str(grow_box["PRICE"]))
        context.bot.send_message(chat_id=update.callback_query.message.chat.id,
                                 text="👍 *Успешно!*\n\n"
                                      "*{desc}* посажен, теперь вам нужно лишь заходить на ферму "
                                      "и собирать созревшие шишки🌳. Вы можете установить скольк"
                                      "о угодно гровбоксов!".format(desc=grow_box["NAME"]),
                                 parse_mode=ParseMode.MARKDOWN)
    else:
        context.bot.send_message(chat_id=update.callback_query.message.chat.id,
                                 text="⛔️*Недостаточно средств!*",
                                 parse_mode=ParseMode.MARKDOWN)
    return state.MARKETS
