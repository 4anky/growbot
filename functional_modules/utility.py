from datetime import datetime, timedelta

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


def start(update, context):
    telegram_id = update.message.from_user.id
    all_id = [t_id[0] for t_id in sql.is_developer(db_path=config.DB_PATH)]
    if telegram_id not in all_id:
        sql.add_to_waiting_users(db_path=config.DB_PATH, telegram_id=update.message.chat.id)
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text=config.WAIT_TEXT)
        return state.WAIT
    else:
        if not update.message.from_user.is_bot:
            sql.reg(db_path=config.DB_PATH,
                    telegram_id=telegram_id,
                    first_name=update.message.from_user.first_name,
                    username=update.message.from_user.username)
            context.bot.send_message(chat_id=update.message.chat.id,
                                     text=config.MENU_DESC,
                                     reply_markup=menu.show(menu=config.MAIN))
        return state.MAIN


def reload(update, context):
    ids = [t_id[0] for t_id in sql.is_developer(db_path=config.DB_PATH)]
    if update.message.chat.id not in ids:
        sql.add_to_waiting_users(db_path=config.DB_PATH, telegram_id=update.message.chat.id)
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text=config.WAIT_TEXT)
        return state.WAIT
    else:
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text=config.MENU_RELOAD,
                                 reply_markup=menu.show(menu=config.MAIN))
        return state.MAIN


def default(update, context):
    if sql.is_wait_user(db_path=config.DB_PATH, telegram_id=update.message.chat.id) is not None:
        return state.WAIT
    else:
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text=config.ERROR_MESSAGE,
                                 reply_markup=menu.show(menu=config.MAIN))
        return state.MAIN


def back_to_main(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=config.BACK_TO_MENU_DESC,
                             reply_markup=menu.show(menu=config.MAIN))
    return state.MAIN
