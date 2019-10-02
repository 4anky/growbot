import config
import menu_bot as menu
import states as state


def info(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=config.INFO_DESC,
                             reply_markup=menu.show(menu=config.INFO))
    return state.INFO


def faq(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=config.FAQ_DESC,
                             reply_markup=menu.show(menu=config.INFO))
    return state.INFO


def community(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=config.COMMUNITY_DESC,
                             reply_markup=menu.show(menu=config.INFO))
    return state.INFO


def letter(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=config.LETTER_DESC,
                             reply_markup=menu.show(menu=config.INFO))
    return state.INFO


def version(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=config.VERSION_DESC,
                             reply_markup=menu.show(menu=config.INFO))
    return state.INFO
