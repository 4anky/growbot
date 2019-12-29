from telegram import error

import config
from functional_modules import home
import sql


def players(update, _):
    if update.message.chat.id in sql.get_dev_id(db_path=config.DB_PATH):
        update.message.reply_markdown(
            text=config.PLAYERS_NUMBER_TEXT.format(n=sql.get_players_number(db_path=config.DB_PATH))
        )
    else:
        update.message.reply_markdown(text=config.ACCESS_DENIED_TEXT)


def users(update, _):
    if update.message.chat.id in sql.get_dev_id(db_path=config.DB_PATH):
        text = "Данные всех игроков:\n\n"
        for user_id, nick in sql.get_users_table(db_path=config.DB_PATH):
            text += "• {id} {nick}\n".format(id=user_id, nick=nick)
        update.message.reply_markdown(
            text=text
        )
    else:
        update.message.reply_markdown(text=config.ACCESS_DENIED_TEXT)


def farm(update, context):
    if update.message.chat.id in sql.get_dev_id(db_path=config.DB_PATH):
        args = context.args
        if len(args) != 1:
            update.message.reply_text(text=config.FARM_ARGUMENT_ERROR_TEXT)
        else:
            try:
                user_id = int(args[0])
            except ValueError:
                update.message.reply_text(text=config.FARM_INCORRECT_ID_TEXT)
            else:
                try:
                    farm_text, ripened_high = home.generate_farm_text(telegram_id=user_id)
                except TypeError:
                    update.message.reply_text(text=config.FARM_ID_DOES_NOT_EXIST_TEXT)
                else:
                    update.message.reply_markdown(text=(config.FARM_BUTTON.join("**")
                                                        + config.FARM_DESC_START
                                                        + farm_text
                                                        + config.FARM_DESC_END.format(all=sum(ripened_high))))
    else:
        update.message.reply_markdown(text=config.ACCESS_DENIED_TEXT)


def msg(update, context):
    if update.message.chat.id in sql.get_dev_id(db_path=config.DB_PATH):
        users_id = [user_data[0] for user_data in sql.get_users_table(db_path=config.DB_PATH)]
        for user_id in users_id:
            try:
                context.bot.send_message(chat_id=user_id, text=" ".join(context.args))
            except error.BadRequest:
                pass
