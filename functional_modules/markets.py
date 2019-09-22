import menu_bot as menu
import states as state


def markets(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы перешли в меню 'Магазин'",
                             reply_markup=menu.show(buttons=menu.markets))
    return state.MARKETS


def high_growing(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Магазин '🐲HighGrowing' скоро откроется!",
                             reply_markup=menu.show(buttons=menu.markets))
    return state.MARKETS
