from telegram import ParseMode

from functional_modules import utility as ut
import config
import menu_bot as menu
import sql
import states as state
import text


def markets(update, _):
    update.message.reply_markdown(text=text.MARKETS_DESC, reply_markup=menu.show(menu=text.MARKETS))
    return state.MARKETS


def high_growing(update, _):
    [update.message.reply_photo(
        photo=open(file=size["PATH"], mode='rb'),
        caption=text.HIGH_GROWING_CAPTION.format(
            about=size["DESC"],
            name=size["NAME"],
            mining=text.three_digits(n=size["MINING"]),
            price=text.three_digits(n=size["PRICE"])),
        reply_markup=menu.inline_button(text=text.BUY_BUTTON, data=size["NAME"]),
        parse_mode=ParseMode.MARKDOWN) for size in config.SIZES]
    return state.MARKETS


def buy_grow_box(update, context):
    money = sql.get_from_table(telegram_id=update.callback_query.message.chat.id, table="balance", field="money")
    [grow_box] = [size for size in config.SIZES if size["NAME"] == update.callback_query.data]
    if money >= grow_box["PRICE"]:
        ripening_number = ut.ripening_number_score(
            last_collect=sql.get_from_table(telegram_id=update.callback_query.message.chat.id,
                                            table="farm",
                                            field="last_collect")
        )
        sql.update_farm_amendments(telegram_id=update.callback_query.message.chat.id,
                                   size=grow_box["SIZE"],
                                   value=int(ripening_number * grow_box["MINING"]))
        sql.buying_grow_box(telegram_id=update.callback_query.message.chat.id,
                            name=grow_box["SIZE"],
                            price=str(grow_box["PRICE"]))
        context.bot.send_message(chat_id=update.callback_query.message.chat.id,
                                 text=text.HIGH_GROWING_PURCHASE.format(desc=grow_box["NAME"]),
                                 parse_mode=ParseMode.MARKDOWN)
    else:
        context.bot.send_message(chat_id=update.callback_query.message.chat.id,
                                 text=text.PURCHASE_ERROR,
                                 parse_mode=ParseMode.MARKDOWN)
    return state.MARKETS
