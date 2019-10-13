import config
import menu_bot as menu
import states as state


def side_job(update, _):
    update.message.reply_markdown(text=config.SIDE_JOB_DESC, reply_markup=menu.show(menu=config.SIDE_JOB))
    return state.SIDE_JOB


def invite(update, _):
    update.message.reply_markdown(text=config.INVITE_DESC, reply_markup=menu.show(menu=config.SIDE_JOB))
    return state.SIDE_JOB
