import constants as const
import menu_bot as menu
import states as state


def home(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Вы перешли в меню 'Дом'",
                             reply_markup=menu.show(menu=const.HOME))
    return state.HOME


def farm(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Вы нажали кнопку 'Ферма'",
                             reply_markup=menu.show(menu=const.HOME))
    return state.HOME


def stock(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Вы нажали кнопку 'Склад'",
                             reply_markup=menu.show(menu=const.HOME))
    return state.HOME


def rating(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Вы нажали кнопку 'Рейтинг'",
                             reply_markup=menu.show(menu=const.HOME))
    return state.HOME
