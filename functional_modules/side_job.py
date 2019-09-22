import menu_bot as menu
import states as state


def side_job(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы нажали кнопку 'Подработка'",
                             reply_markup=menu.show(buttons=menu.main))
    return state.MAIN
