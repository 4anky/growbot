import menu_bot as menu
import states as state


def info(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы перешли в меню 'Информация'",
                             reply_markup=menu.show(buttons=menu.info))
    return state.INFO


def faq(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы нажали кнопку 'FAQ'",
                             reply_markup=menu.show(buttons=menu.info))
    return state.INFO


def community(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы нажали кнопку 'Сообщество'",
                             reply_markup=menu.show(buttons=menu.info))
    return state.INFO


def letter(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы нажали кнопку 'Письмо авторам'",
                             reply_markup=menu.show(buttons=menu.info))
    return state.INFO


def version(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы нажали кнопку 'Версия игры'",
                             reply_markup=menu.show(buttons=menu.info))
    return state.INFO
