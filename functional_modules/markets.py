from telegram import ParseMode

from functional_modules import utility
import config
import menu_bot as menu
import sql
import states as state


def markets(update, _):
    update.message.reply_markdown(text=config.MARKETS_DESC, reply_markup=menu.show(menu=config.MARKETS))
    return state.MARKETS


def high_growing(update, _):
    [update.message.reply_photo(
        photo=open(file=size["PATH"], mode='rb'),
        caption=config.HIGH_GROWING_CAPTION.format(
            about=size["DESC"], name=size["NAME"], mining=size["MINING"], price=size["PRICE"]),
        reply_markup=menu.inline_button(text=config.BUY_BUTTON, data=size["NAME"]),
        parse_mode=ParseMode.MARKDOWN) for size in config.SIZES]
    return state.MARKETS


def buy_grow_box(update, context):
    money = sql.get_from_table(
        db_path=config.DB_PATH, telegram_id=update.callback_query.message.chat.id, table="balance", field="money")
    [grow_box] = [size for size in config.SIZES if size["NAME"] == update.callback_query.data]
    if money >= grow_box["PRICE"]:
        ripening_number = utility.ripening_number_score(
            last_collect=sql.get_from_table(db_path=config.DB_PATH,
                                            telegram_id=update.callback_query.message.chat.id,
                                            table="farm",
                                            field="last_collect")
        )
        sql.update_farm_amendments(db_path=config.DB_PATH,
                                   telegram_id=update.callback_query.message.chat.id,
                                   size=grow_box["SIZE"],
                                   value=ripening_number * grow_box["MINING"])
        sql.buying_grow_box(db_path=config.DB_PATH,
                            telegram_id=update.callback_query.message.chat.id,
                            name=grow_box["SIZE"],
                            price=str(grow_box["PRICE"]))
        context.bot.send_message(chat_id=update.callback_query.message.chat.id,
                                 text=config.HIGH_GROWING_PURCHASE.format(desc=grow_box["NAME"]),
                                 parse_mode=ParseMode.MARKDOWN)
    else:
        context.bot.send_message(chat_id=update.callback_query.message.chat.id,
                                 text=config.PURCHASE_ERROR,
                                 parse_mode=ParseMode.MARKDOWN)
    return state.MARKETS
