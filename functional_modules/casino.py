import config
import menu_bot as menu
import states as state


def casino(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы перешли в меню 'Казино'",
                             reply_markup=menu.show(menu=config.CASINO))
    return state.CASINO


def dice(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы нажали кнопку 'Кости'",
                             reply_markup=menu.show(menu=config.CASINO))
    return state.CASINO
