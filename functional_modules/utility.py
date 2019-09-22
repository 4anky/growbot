import menu_bot as menu
import states as state


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Вы перешли в 'Главное Меню'",
                             reply_markup=menu.show(buttons=menu.main))
    return state.MAIN


def default(context, update):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Что-то пошло не так.\n"
                                  "Возвращаемся в 'Главное Меню'",
                             reply_markup=menu.show(buttons=menu.main))
    return state.MAIN


def back_to_main(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Вы вернулись в 'Главное Меню'",
                             reply_markup=menu.show(buttons=menu.main))
    return state.MAIN
