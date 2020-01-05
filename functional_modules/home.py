import logging

from telegram import ParseMode

from functional_modules import utility
import config
import menu_bot as menu
import states as state
import sql

LOGS_PATH = __file__.replace(r"functional_modules\home.py", "logs/home.log")

logging.basicConfig(filename=LOGS_PATH, level=logging.INFO)


def home(update, _):
    update.message.reply_markdown(text=config.HOME_DESC, reply_markup=menu.show(menu=config.HOME))
    return state.HOME


def generate_farm_text(telegram_id):
    _, boxes, ripened_high = utility.farm_stats(telegram_id=telegram_id)
    return ("\n".join([config.FARM_STATS.format(name=sort["NAME"], number=number, mature=high)
                       for sort, number, high in zip(config.SIZES, boxes, ripened_high) if number]),
            ripened_high)


def farm(update, context):
    farm_text, ripened_high = generate_farm_text(telegram_id=update.message.from_user.id)
    context.bot.send_message(chat_id=update.message.from_user.id,
                             text=(config.FARM_BUTTON.join("**")
                                   + config.FARM_DESC_START
                                   + farm_text
                                   + config.FARM_DESC_END.format(all=sum(ripened_high))),
                             reply_markup=menu.inline_button(text=config.HARVEST_INLINE, data=config.PATTERN_HARVEST),
                             parse_mode=ParseMode.MARKDOWN)
    return state.HOME


def harvest(update, context):
    telegram_id = update.callback_query.message.chat.id
    ripening_number, _, ripened_high = utility.farm_stats(telegram_id=telegram_id)
    high_number = sum(ripened_high)

    if high_number and ripening_number:
        sql.high_to_balance(db_path=config.DB_PATH, telegram_id=telegram_id, high=high_number)
        sql.to_zero_farm_amendments(db_path=config.DB_PATH, telegram_id=telegram_id)
        context.bot.edit_message_text(text=config.FARM_HARVEST.format(number=high_number),
                                      chat_id=telegram_id,
                                      message_id=update.callback_query.message.message_id,
                                      parse_mode=ParseMode.MARKDOWN)
        return state.HOME
    else:
        context.bot.edit_message_text(text=config.HARVEST_ERROR,
                                      chat_id=telegram_id,
                                      message_id=update.callback_query.message.message_id,
                                      parse_mode=ParseMode.MARKDOWN)
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

ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/home/ec2-user/weed_bot/growbot/.venv/lib64/python3.6/site-packages/telegram/ext/dispatcher.py", line 372, in process_update
    handler.handle_update(update, self, check, context)
  File "/home/ec2-user/weed_bot/growbot/.venv/lib64/python3.6/site-packages/telegram/ext/handler.py", line 117, in handle_update
    return self.callback(update, context)
  File "/home/ec2-user/weed_bot/growbot/dev.py", line 58, in msg
    context.bot.send_message(chat_id=user_id, text=" ".join(context.args))
  File "/home/ec2-user/weed_bot/growbot/.venv/lib64/python3.6/site-packages/telegram/bot.py", line 66, in decorator
    result = func(self, *args, **kwargs)
  File "/home/ec2-user/weed_bot/growbot/.venv/lib64/python3.6/site-packages/telegram/bot.py", line 258, in send_message
    timeout=timeout, **kwargs)
  File "/home/ec2-user/weed_bot/growbot/.venv/lib64/python3.6/site-packages/telegram/bot.py", line 123, in _message
    result = self._request.post(url, data, timeout=timeout)
  File "/home/ec2-user/weed_bot/growbot/.venv/lib64/python3.6/site-packages/telegram/utils/request.py", line 327, in post
    **urlopen_kwargs)
  File "/home/ec2-user/weed_bot/growbot/.venv/lib64/python3.6/site-packages/telegram/utils/request.py", line 236, in _request_wrapper
    raise Unauthorized(message)
telegram.error.Unauthorized: Forbidden: bot was blocked by the user
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/home/ec2-user/weed_bot/growbot/.venv/lib64/python3.6/site-packages/telegram/ext/dispatcher.py", line 372, in process_update
    handler.handle_update(update, self, check, context)
  File "/home/ec2-user/weed_bot/growbot/.venv/lib64/python3.6/site-packages/telegram/ext/handler.py", line 117, in handle_update
    return self.callback(update, context)
  File "/home/ec2-user/weed_bot/growbot/dev.py", line 30, in farm
    if update.message.chat.id in sql.get_dev_id(db_path=config.DB_PATH):
AttributeError: 'NoneType' object has no attribute 'chat'
