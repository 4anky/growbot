import menu_bot as menu
import states as state


def sell_goods(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы перешли в меню 'Продать товар'",
                             reply_markup=menu.show(buttons=menu.sell_goods))
    return state.SELL_GOODS


def agent(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Вы нажали кнопку 'Агент'",
                             reply_markup=menu.show(buttons=menu.sell_goods))
    return state.SELL_GOODS


def street(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Вы нажали кнопку 'Улица'",
                             reply_markup=menu.show(buttons=menu.sell_goods))
    return state.SELL_GOODS
