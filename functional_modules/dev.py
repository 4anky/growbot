import config
import sql


def players_number(update, _):
    update.message.reply_markdown(
        text=config.PLAYERS_NUMBER_TEXT.format(n=sql.get_players_number(db_path=config.DB_PATH))
    )
