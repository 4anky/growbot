import menu_bot as menu
import states as state


def home(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Вы нажали кнопку '🏠Дом'",
                             reply_markup=menu.show(buttons=menu.main))
    return state.MAIN
