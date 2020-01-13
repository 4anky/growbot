from datetime import datetime, timedelta
from random import uniform

from functional_modules import train
import config
import menu_bot as menu
import states as state
import sql


def ripening_number_score(last_collect):
    utc_time = datetime.utcnow()
    [last_ripening] = [utc_time.replace(minute=config.RIPENING["MINUTE"], second=0, microsecond=0)
                       if utc_time.minute >= config.RIPENING["MINUTE"] else
                       utc_time.replace(
                           hour=utc_time.hour - 1, minute=config.RIPENING["MINUTE"], second=0, microsecond=0
                       )
                       ]
    ripening_number = int((last_ripening - last_collect + timedelta(hours=1)).total_seconds() // 3600)
    return (1 - config.REDUCTION_FACTOR ** ripening_number) / (1 - config.REDUCTION_FACTOR)


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


def farm_stats(telegram_id):
    boxes, amendments, last_collect = sql.get_all_farm(db_path=config.DB_PATH, telegram_id=telegram_id)
    number = ripening_number_score(last_collect=last_collect)
    return number, boxes, [int(number * box * size["MINING"] - amendment)
                           for box, size, amendment in zip(boxes, config.SIZES, amendments)]


def street_exchange(high, price):
    return (high // (config.MIN_HIGH_FOR_STREET // 5) * 100,
            high % (config.MIN_HIGH_FOR_STREET // 5),
            high // (config.MIN_HIGH_FOR_STREET // 5) * (price // 10))


def money_for_escape(money):
    return int(money * uniform(a=1, b=10) // 100)


def money_retention(money):
    return int(money * 1.03)


def start(update, _):
    if sql.is_reg(db_path=config.DB_PATH, telegram_id=update.message.from_user.id) is None:
        sql.reg(db_path=config.DB_PATH, telegram_id=update.message.from_user.id)
        if len(update.message.text) > len("/start"):
            try:
                referrer = int(update.message.text.split()[-1])
            except ValueError:
                pass
            else:
                if sql.get_from_table(db_path=config.DB_PATH, telegram_id=referrer, table="users", field="nick"):
                    sql.add_referral(db_path=config.DB_PATH, referrer=referrer, referral=update.message.chat.id)
        train.to_desc_1(update, _)
        return state.TRAIN_DESC_1
    elif not update.message.from_user.is_bot:
        update.message.reply_markdown(text=config.MENU_DESC, reply_markup=menu.show(menu=config.MAIN))
        return state.MAIN


def reload(update, _):
    update.message.reply_markdown(text=config.MENU_RELOAD, reply_markup=menu.show(menu=config.MAIN))
    return state.MAIN


def default(update, _):
    update.message.reply_markdown(text=config.ERROR_MESSAGE, reply_markup=menu.show(menu=config.MAIN))
    return state.MAIN


def back_to_main(update, _):
    update.message.reply_markdown(text=config.BACK_TO_MENU_DESC, reply_markup=menu.show(menu=config.MAIN))
    return state.MAIN
