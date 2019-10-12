from telegram import ParseMode

import config
import menu_bot as menu
import states as state


def casino(update, context):
    context.bot.send_photo(chat_id=update.message.chat.id,
                           photo=open(file=config.CASINO_PIC_PATH, mode='rb'),
                           caption=config.CASINO_DESC,
                           reply_markup=menu.show(menu=config.CASINO),
                           parse_mode=ParseMode.MARKDOWN)
    return state.CASINO


def dice(update, context):
    context.bot.send_photo(chat_id=update.message.chat.id,
                           photo=open(file=config.CASINO_PIC_PATH, mode='rb'),
                           caption=config.DICE_DESC,
                           reply_markup=menu.show(menu=config.CASINO),
                           parse_mode=ParseMode.MARKDOWN)
    return state.CASINO
