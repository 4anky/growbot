from telegram import ParseMode

import config
import menu_bot as menu
import states as state


def side_job(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=config.SIDE_JOB_DESC,
                             reply_markup=menu.show(menu=config.SIDE_JOB),
                             parse_mode=ParseMode.MARKDOWN)
    return state.SIDE_JOB


def invite(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=config.INVITE_DESC,
                             reply_markup=menu.show(menu=config.SIDE_JOB),
                             parse_mode=ParseMode.MARKDOWN)
    return state.SIDE_JOB
