import sql


def safer_street_3d(update, _):
    date = sql.safer_street(telegram_id=update.message.chat.id, duration=3)
    update.message.reply_markdown(text=(f'*Сделка 🤝 состоялась!*\n\nДо {date:%d-%m-%Y %H:%M:%S} *полицейский 🚔 '
                                        f'патруль* будет реже обращать на Вас 👀 внимание'))


def safer_street_10d(update, _):
    date = sql.safer_street(telegram_id=update.message.chat.id, duration=10)
    update.message.reply_markdown(text=(f'*Сделка 🤝 состоялась!*\n\nДо {date:%d-%m-%Y %H:%M:%S} *полицейский 🚔 '
                                        f'патруль* будет реже обращать на Вас 👀 внимание'))


def safer_street_30d(update, _):
    date = sql.safer_street(telegram_id=update.message.chat.id, duration=30)
    update.message.reply_markdown(text=(f'*Сделка 🤝 состоялась!*\n\nДо {date:%d-%m-%Y %H:%M:%S} *полицейский 🚔 '
                                        f'патруль* будет реже обращать на Вас 👀 внимание'))
