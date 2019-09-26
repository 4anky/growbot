import config
import menu_bot as menu
import states as state


def side_job(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы перешли в меню 'Подработка'",
                             reply_markup=menu.show(menu=config.SIDE_JOB))
    return state.SIDE_JOB


def invite(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы нажали кнопку 'Пригласи друга'",
                             reply_markup=menu.show(menu=config.SIDE_JOB))
    return state.SIDE_JOB
