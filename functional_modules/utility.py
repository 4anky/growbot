from datetime import datetime, timedelta
from random import uniform

from telegram import ParseMode

from functional_modules import train
import config
import menu_bot as menu
import states as state
import sql


def ripening_number_score(last_collect):
    utc_time = datetime.utcnow()
    [last_ripening] = [utc_time.replace(minute=config.RIPENING["MINUTE"], second=0, microsecond=0)
                       if utc_time.minute >= config.RIPENING["MINUTE"] else
                       utc_time.replace(hour=utc_time.hour - 1,
                                        minute=config.RIPENING["MINUTE"],
                                        second=0, microsecond=0)
                       ]
    return int((last_ripening - last_collect + timedelta(hours=1)).total_seconds() // 3600)


def money_transfer(high):
    packs = list()
    packs.append(high // config.BID_5["HIGH"])
    packs.append(high % config.BID_5["HIGH"] // config.BID_4["HIGH"])
    packs.append(high % config.BID_5["HIGH"] % config.BID_4["HIGH"] // config.BID_3["HIGH"])
    packs.append(high % config.BID_5["HIGH"] % config.BID_4["HIGH"] % config.BID_3["HIGH"]
                 // config.BID_2["HIGH"])
    packs.append(high % config.BID_5["HIGH"] % config.BID_4["HIGH"] % config.BID_3["HIGH"]
                 % config.BID_2["HIGH"] // config.BID_1["HIGH"])

    return sum(pack * bid["PAY"] for pack, bid in zip(packs, config.BIDS[::-1]))


def street_exchange(high, price):
    return (high // (config.MIN_HIGH_FOR_STREET // 10) * 100,
            high % (config.MIN_HIGH_FOR_STREET // 10),
            high // (config.MIN_HIGH_FOR_STREET // 10) * (price // 10))


def money_for_escape(money):
    return int(money * uniform(a=1, b=10) // 100)


def money_retention(money):
    return int(money * 1.03)


def start(update, context):
    if sql.is_reg(db_path=config.DB_PATH, telegram_id=update.message.from_user.id) is None:
        sql.reg(db_path=config.DB_PATH, telegram_id=update.message.from_user.id)
        train.to_desc_1(update, context)
        return state.TRAIN_DESC_1
    elif not update.message.from_user.is_bot:
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text=config.MENU_DESC,
                                 reply_markup=menu.show(menu=config.MAIN),
                                 parse_mode=ParseMode.MARKDOWN)
        return state.MAIN


def reload(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=config.MENU_RELOAD,
                             reply_markup=menu.show(menu=config.MAIN),
                             parse_mode=ParseMode.MARKDOWN)
    return state.MAIN


def default(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=config.ERROR_MESSAGE,
                             reply_markup=menu.show(menu=config.MAIN),
                             parse_mode=ParseMode.MARKDOWN)
    return state.MAIN


def back_to_main(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=config.BACK_TO_MENU_DESC,
                             reply_markup=menu.show(menu=config.MAIN),
                             parse_mode=ParseMode.MARKDOWN)
    return state.MAIN
