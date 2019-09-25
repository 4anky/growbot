from datetime import datetime, timedelta

from telegram import ParseMode

import config
import constants as const
import menu_bot as menu
import states as state
import sql


def ripening_number_score(last_collect):
    [last_ripening] = [datetime.utcnow().replace(minute=23, second=0, microsecond=0)
                       if datetime.utcnow().minute >= 23 else
                       datetime.utcnow().replace(hour=datetime.utcnow().hour - 1, minute=23, second=0, microsecond=0)
                       ]
    return int((last_ripening - last_collect + timedelta(hours=1)).total_seconds() // 3600)


def home(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Вы дома.",
                             reply_markup=menu.show(menu=const.HOME))
    return state.HOME


def farm(update, context):
    farm_data = sql.get_farm(db_path=config.DB_PATH, telegram_id=update.message.from_user.id)
    ripening_number = ripening_number_score(last_collect=farm_data[const.LAST_COLLECT])
    high_stats = [high * size["MINING"] * ripening_number for high, size in zip(farm_data, const.SIZES)]
    context.bot.send_message(chat_id=update.message.from_user.id,
                             text=const.FARM.format(XS=farm_data[0],
                                                    XS_high=high_stats[0],
                                                    S=farm_data[1],
                                                    S_high=high_stats[1],
                                                    M=farm_data[2],
                                                    M_high=high_stats[2],
                                                    L=farm_data[3],
                                                    L_high=high_stats[3],
                                                    XL=farm_data[4],
                                                    XL_high=high_stats[4],
                                                    XXL=farm_data[5],
                                                    XXL_high=high_stats[5],
                                                    all_high=sum(high_stats),
                                                    date=farm_data[6]
                                                    ),
                             reply_markup=menu.show(menu=const.HOME),
                             parse_mode=ParseMode.MARKDOWN)
    return state.HOME


def balance(update, context):
    (money, high) = sql.get_balance(db_path=config.DB_PATH, telegram_id=update.message.from_user.id)
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=const.BALANCE.format(money=money, high=high),
                             reply_markup=menu.show(menu=const.HOME),
                             parse_mode=ParseMode.MARKDOWN)
    return state.HOME


def rating(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="В эту игру ещё никто не играет.",
                             reply_markup=menu.show(menu=const.HOME))
    return state.HOME
