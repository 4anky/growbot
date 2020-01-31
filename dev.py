from telegram import error, ParseMode

from functional_modules.home import generate_farm_text
import sql
import text


def players(update, _):
    if update.message.chat.id in sql.get_dev_id():
        update.message.reply_markdown(
            text=text.PLAYERS_NUMBER_TEXT.format(n=sql.get_players_number())
        )
    else:
        update.message.reply_markdown(text=text.ACCESS_DENIED_TEXT)


def users(update, _):
    if update.message.chat.id in sql.get_dev_id():
        message = text.USERS_HEADING_TEXT
        for user_id, nick in sql.get_users_table():
            message += text.USERS_TEXT.format(id=user_id, nick=nick)
        update.message.reply_markdown(
            text=message
        )
    else:
        update.message.reply_markdown(text=text.ACCESS_DENIED_TEXT)


def farm(update, context):
    if update.message.chat.id in sql.get_dev_id():
        args = context.args
        if len(args) != 1:
            update.message.reply_text(text=text.FARM_ARGUMENT_ERROR_TEXT)
        else:
            try:
                user_id = int(args[0])
            except ValueError:
                update.message.reply_text(text=text.FARM_INCORRECT_ID_TEXT)
            else:
                try:
                    farm_text, ripened_high = generate_farm_text(telegram_id=user_id)
                except TypeError:
                    update.message.reply_text(text=text.FARM_ID_DOES_NOT_EXIST_TEXT)
                else:
                    update.message.reply_markdown(text=(text.FARM_BUTTON.join("**")
                                                        + text.FARM_DESC_START
                                                        + farm_text
                                                        + text.FARM_DESC_END.format(all=sum(ripened_high))))
    else:
        update.message.reply_markdown(text=text.ACCESS_DENIED_TEXT)


def msg(update, context):
    if update.message.chat.id in sql.get_dev_id():
        users_id = [user_data[0] for user_data in sql.get_users_table()]
        for user_id in users_id:
            try:
                context.bot.send_message(chat_id=user_id, text=" ".join(context.args), parse_mode=ParseMode.MARKDOWN)
            except error.BadRequest:
                pass
