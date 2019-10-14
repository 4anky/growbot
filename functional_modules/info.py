from telegram import ParseMode, TelegramError

import config
import menu_bot as menu
import sql
import states as state


def info(update, _):
    update.message.reply_markdown(text=config.INFO_DESC, reply_markup=menu.show(menu=config.INFO))
    return state.INFO


def faq(update, _):
    update.message.reply_markdown(text=config.FAQ_DESC, reply_markup=menu.show(menu=config.INFO),)
    return state.INFO


def community(update, _):
    update.message.reply_text(text=config.COMMUNITY_DESC, reply_markup=menu.show(menu=config.INFO))
    return state.INFO


def letter(update, _):
    update.message.reply_markdown(text=config.LETTER_DESC, reply_markup=menu.show(menu=config.BACK))
    return state.LETTER


def send_letter(update, context):
    text = update.message.text
    if len(text) > config.LETTER_MAX_LEN:
        update.message.reply_markdown(text=config.ERROR_LETTER, reply_markup=menu.show(menu=config.BACK))
        return state.LETTER
    else:
        developers = sql.get_dev_id(db_path=config.DB_PATH)
        player_nick = sql.get_from_table(db_path=config.DB_PATH,
                                         telegram_id=update.message.chat.id,
                                         table="users",
                                         field="nick")
        for developer in developers:
            try:
                context.bot.send_message(chat_id=developer,
                                         text=(config.LETTER_HEADING
                                               + update.message.text).format(nick=player_nick),
                                         parse_mode=ParseMode.MARKDOWN)
            except TelegramError:
                continue
        update.message.reply_markdown(text=config.LETTER_SEND, reply_markup=menu.show(menu=config.INFO))
        return state.INFO


def version(update, _):
    update.message.reply_markdown(text=config.VERSION, reply_markup=menu.show(menu=config.INFO))
    return state.INFO
