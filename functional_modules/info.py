from telegram import ParseMode, TelegramError

import config
import menu_bot as menu
import sql
import states as state
import text


def info(update, _):
    update.message.reply_markdown(text=text.INFO_DESC, reply_markup=menu.show(menu=text.INFO))
    return state.INFO


def faq(update, _):
    update.message.reply_markdown(text=text.FAQ_DESC, reply_markup=menu.show(menu=text.INFO),)
    return state.INFO


def community(update, _):
    update.message.reply_markdown(text=text.COMMUNITY_DESC, reply_markup=menu.show(menu=text.INFO))
    return state.INFO


def letter(update, _):
    update.message.reply_markdown(text=text.LETTER_DESC, reply_markup=menu.show(menu=text.BACK))
    return state.LETTER


def send_letter(update, context):
    if len(update.message.text) > config.LETTER_MAX_LEN:
        update.message.reply_markdown(text=text.ERROR_LETTER, reply_markup=menu.show(menu=text.BACK))
        return state.LETTER
    else:
        developers = sql.get_dev_id()
        player_nick = sql.get_from_table(telegram_id=update.message.chat.id, table="users", field="nick")
        for developer in developers:
            try:
                context.bot.send_message(chat_id=developer,
                                         text=(text.LETTER_HEADING
                                               + update.message.text).format(nick=player_nick),
                                         parse_mode=ParseMode.MARKDOWN)
            except TelegramError:
                continue
        update.message.reply_markdown(text=text.LETTER_SEND, reply_markup=menu.show(menu=text.INFO))
        return state.INFO


def version(update, _):
    update.message.reply_markdown(text=text.VERSION, reply_markup=menu.show(menu=text.INFO))
    return state.INFO
