from telegram import ParseMode

import constants as const
import menu_bot as menu
import states as state


def markets(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Вы перешли в меню 'Магазин'",
                             reply_markup=menu.show(menu=const.MARKETS))
    return state.MARKETS


def high_growing(update, context):
    [context.bot.send_photo(chat_id=update.message.chat.id,
                            photo=open(file=size["PATH"], mode='rb'),
                            caption=const.HIGH_GROWING_CAPTION.format(about=size["DESC"],
                                                                      name=size["NAME"],
                                                                      mining=size["MINING"],
                                                                      price=size["PRICE"]),
                            reply_markup=menu.high_growing_buy_button(size=size["SIZE"]),
                            parse_mode=ParseMode.MARKDOWN)
     for size in const.SIZES]
    return state.MARKETS
