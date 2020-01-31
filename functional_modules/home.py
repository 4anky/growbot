from telegram import ParseMode

from functional_modules import utility as ut
import config
import menu_bot as menu
import states as state
import sql
import text


def home(update, _):
    update.message.reply_markdown(text=text.HOME_DESC, reply_markup=menu.show(menu=text.HOME))
    return state.HOME


def generate_farm_text(telegram_id):
    _, boxes, ripened_high = ut.farm_stats(telegram_id=telegram_id)
    return ("\n".join([text.FARM_STATS.format(name=sort["NAME"],
                                              number=text.three_digits(n=number),
                                              mature=text.three_digits(n=high))
                       for sort, number, high in zip(config.SIZES, boxes, ripened_high) if number]),
            ripened_high)


def farm(update, context):
    farm_text, ripened_high = generate_farm_text(telegram_id=update.message.from_user.id)
    context.bot.send_message(chat_id=update.message.from_user.id,
                             text=(text.FARM_BUTTON.join("**")
                                   + text.FARM_DESC_START
                                   + farm_text
                                   + text.FARM_DESC_END.format(all=text.three_digits(n=sum(ripened_high)))),
                             reply_markup=menu.inline_button(text=text.HARVEST_INLINE, data=config.PATTERN_HARVEST),
                             parse_mode=ParseMode.MARKDOWN)
    return state.HOME


def harvest(update, context):
    telegram_id = update.callback_query.message.chat.id
    ripening_number, _, ripened_high = ut.farm_stats(telegram_id=telegram_id)
    high_number = sum(ripened_high)

    if high_number and ripening_number:
        sql.high_to_balance(telegram_id=telegram_id, high=high_number)
        sql.to_zero_farm_amendments(telegram_id=telegram_id)
        context.bot.edit_message_text(text=text.FARM_HARVEST.format(number=text.three_digits(n=high_number)),
                                      chat_id=telegram_id,
                                      message_id=update.callback_query.message.message_id,
                                      parse_mode=ParseMode.MARKDOWN)
        return state.HOME
    else:
        context.bot.edit_message_text(text=text.HARVEST_ERROR,
                                      chat_id=telegram_id,
                                      message_id=update.callback_query.message.message_id,
                                      parse_mode=ParseMode.MARKDOWN)
        return state.HOME


def balance(update, _):
    (money, high, chip) = sql.get_balance(telegram_id=update.message.from_user.id)
    update.message.reply_markdown(
        text=text.BALANCE.format(money=text.three_digits(n=money),
                                 high=text.three_digits(n=high),
                                 chip=text.three_digits(n=chip)),
        reply_markup=menu.show(menu=text.HOME))
    return state.HOME


def rating(update, _):
    update.message.reply_markdown(text=text.RATING_DESC, reply_markup=menu.show(menu=text.RATING))
    return state.RATING


def rating_money(update, _):
    top = sql.get_rating(param="money")
    update.message.reply_markdown(
        text=(text.RATING_MONEY_TEXT
              + "\n".join(text.RATING_MONEY_LINE.format(name=nick, number=text.three_digits(n=money))
                          for (nick, money) in top)),
        reply_markup=menu.show(menu=text.RATING))
    return state.RATING


def rating_harvest(update, _):
    top = sql.get_rating(param="harvest_sum")
    update.message.reply_markdown(
        text=(text.RATING_HARVEST_SUM_TEXT
              + "\n".join(text.RATING_HARVEST_SUM_LINE.format(name=nick, number=text.three_digits(n=harvest_sum))
                          for (nick, harvest_sum) in top)),
        reply_markup=menu.show(menu=text.RATING))
    return state.RATING
