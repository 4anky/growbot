from telegram import ParseMode

import config
import sql


def players_number(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text=config.PLAYERS_NUMBER_TEXT.format(n=sql.get_players_number(db_path=config.DB_PATH)),
                             parse_mode=ParseMode.MARKDOWN)
