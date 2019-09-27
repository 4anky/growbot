import config
import menu_bot as menu
import states as state
import sql


def start(update, context):
    telegram_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    username = update.message.from_user.username
    is_bot = update.message.from_user.is_bot
    ids = [t_id[0] for t_id in sql.is_developer(db_path=config.DB_PATH)]
    if telegram_id not in ids:
        sql.add_to_waiting_users(db_path=config.DB_PATH, telegram_id=update.message.chat.id)
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text=config.WAIT_TEXT)
        return state.WAIT
    else:
        if not is_bot:
            sql.reg(db_path=config.DB_PATH, telegram_id=telegram_id, first_name=first_name, username=username)
            context.bot.send_message(chat_id=update.message.chat.id,
                                     text="Вы перешли в Главное Меню.",
                                     reply_markup=menu.show(menu=config.MAIN))
        return state.MAIN


def reload(update, context):
    ids = [t_id[0] for t_id in sql.is_developer(db_path=config.DB_PATH)]
    if update.message.chat.id not in ids:
        sql.add_to_waiting_users(db_path=config.DB_PATH, telegram_id=update.message.chat.id)
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text=config.WAIT_TEXT)
        return state.WAIT
    else:
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text="Версия Игры обновилась.\nВы в Главном Меню.",
                                 reply_markup=menu.show(menu=config.MAIN))
        return state.MAIN


def default(update, context):
    if sql.is_wait_user(db_path=config.DB_PATH, telegram_id=update.message.chat.id) is not None:
        return state.WAIT
    else:
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text="Возвращаемся в Главное Меню.",
                                 reply_markup=menu.show(menu=config.MAIN))
        return state.MAIN


def back_to_main(update, context):
    context.bot.send_message(chat_id=update.message.chat.id,
                             text="Вы вернулись в Главное Меню.",
                             reply_markup=menu.show(menu=config.MAIN))
    return state.MAIN
