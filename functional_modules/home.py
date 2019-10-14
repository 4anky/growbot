from telegram import ParseMode

from functional_modules import utility
import config
import menu_bot as menu
import states as state
import sql


def home(update, _):
    update.message.reply_markdown(text=config.HOME_DESC, reply_markup=menu.show(menu=config.HOME))
    return state.HOME


def farm(update, context):
    farm_data = sql.get_farm(db_path=config.DB_PATH, telegram_id=update.message.from_user.id)
    farm_amendments_data = sql.get_farm_amendments(db_path=config.DB_PATH, telegram_id=update.message.from_user.id)
    ripening_number = utility.ripening_number_score(last_collect=farm_data[config.LAST_COLLECT])
    high_stats = [ripening_number * high * size["MINING"] - amendment
                  for high, size, amendment in zip(farm_data, config.SIZES, farm_amendments_data)]
    farm_stats = "\n".join([config.FARM_STATS.format(name=sort["NAME"], number=number, mature=high)
                            for sort, number, high in zip(config.SIZES, farm_data, high_stats)
                            if number])
    context.bot.send_message(chat_id=update.message.from_user.id,
                             text=(config.FARM_BUTTON.join("**")
                                   + config.FARM_DESC_START
                                   + farm_stats
                                   + config.FARM_DESC_END.format(all=sum(high_stats), date=farm_data[6])),
                             reply_markup=menu.inline_button(text=config.HARVEST_INLINE, data=str(sum(high_stats))),
                             parse_mode=ParseMode.MARKDOWN)
    return state.HOME


def harvest(update, context):
    high_number = int(update.callback_query.data)
    telegram_id = update.callback_query.message.chat.id
    message_id = update.callback_query.message.message_id
    if high_number:
        sql.high_to_balance(
            db_path=config.DB_PATH, telegram_id=telegram_id, high=high_number)
        sql.to_zero_farm_amendments(db_path=config.DB_PATH, telegram_id=telegram_id)
        context.bot.edit_message_text(text=config.FARM_HARVEST.format(number=high_number),
                                      chat_id=telegram_id,
                                      message_id=message_id,
                                      parse_mode=ParseMode.MARKDOWN)
        return state.HOME
    else:
        context.bot.edit_message_text(
            text=config.HARVEST_ERROR, chat_id=telegram_id, message_id=message_id, parse_mode=ParseMode.MARKDOWN)
        return state.HOME


def balance(update, _):
    (money, high, chip) = sql.get_balance(db_path=config.DB_PATH, telegram_id=update.message.from_user.id)
    update.message.reply_markdown(
        text=config.BALANCE.format(money=money, high=high, chip=chip), reply_markup=menu.show(menu=config.HOME))
    return state.HOME


def rating(update, _):
    update.message.reply_markdown(text=config.RATING_DESC, reply_markup=menu.show(menu=config.RATING))
    return state.RATING


def rating_money(update, _):
    top = sql.get_rating(db_path=config.DB_PATH, param="money")
    update.message.reply_markdown(
        text=(config.RATING_MONEY_TEXT
              + "\n".join(config.RATING_MONEY_LINE.format(name=nick, number=money) for (nick, money) in top)),
        reply_markup=menu.show(menu=config.RATING))
    return state.RATING


def rating_harvest(update, _):
    top = sql.get_rating(db_path=config.DB_PATH, param="harvest_sum")
    update.message.reply_markdown(
        text=(config.RATING_HARVEST_SUM_TEXT
              + "\n".join(config.RATING_HARVEST_SUM_LINE.format(name=nick, number=harvest_sum)
                          for (nick, harvest_sum) in top)),
        reply_markup=menu.show(menu=config.RATING))
    return state.RATING
