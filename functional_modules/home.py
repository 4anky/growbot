from telegram import ParseMode

from functional_modules import utility
import config
import menu_bot as menu
import states as state
import sql


def home(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=config.HOME_DESC,
                             reply_markup=menu.show(menu=config.HOME))
    return state.HOME


def farm(update, context):
    farm_data = sql.get_farm(db_path=config.DB_PATH, telegram_id=update.message.from_user.id)
    ripening_number = utility.ripening_number_score(last_collect=farm_data[config.LAST_COLLECT])
    high_stats = [ripening_number * high * size["MINING"] for high, size in zip(farm_data, config.SIZES)]
    farm_stats = "\n".join([config.FARM_STATS.format(name=sort["NAME"], number=number, mature=high)
                            for sort, number, high in zip(config.SIZES, farm_data, high_stats)
                            if number])
    context.bot.send_message(chat_id=update.message.from_user.id,
                             text=("*" + config.FARM_BUTTON + "*" +
                                   config.FARM_DESC_START +
                                   farm_stats +
                                   config.FARM_DESC_END.format(all=sum(high_stats), date=farm_data[6])),
                             reply_markup=menu.inline_button(text=config.HARVEST_INLINE, data=str(sum(high_stats))),
                             parse_mode=ParseMode.MARKDOWN)
    return state.HOME


def harvest(update, context):
    high_number = int(update.callback_query.data)
    telegram_id = update.callback_query.message.chat.id
    if high_number:
        sql.high_to_balance(db_path=config.DB_PATH,
                            telegram_id=telegram_id,
                            high=high_number)
        context.bot.send_message(chat_id=telegram_id,
                                 text=config.FARM_HARVEST.format(number=high_number),
                                 parse_mode=ParseMode.MARKDOWN)
        return state.HOME
    else:
        context.bot.send_message(chat_id=telegram_id,
                                 text=config.HARVEST_ERROR,
                                 parse_mode=ParseMode.MARKDOWN)
        return state.HOME


def balance(update, context):
    (money, high, chip) = sql.get_balance(db_path=config.DB_PATH, telegram_id=update.message.from_user.id)
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=config.BALANCE.format(money=money, high=high, chip=chip),
                             reply_markup=menu.show(menu=config.HOME),
                             parse_mode=ParseMode.MARKDOWN)
    return state.HOME


def rating(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=config.RATING_DESC,
                             reply_markup=menu.show(menu=config.HOME))
    return state.HOME
