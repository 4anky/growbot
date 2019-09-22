import menu_bot as menu
import states as state


def info(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы нажали кнопку 'Информация'",
                             reply_markup=menu.show(buttons=menu.main))
    return state.MAIN
