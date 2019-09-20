from telegram.ext import Filters, MessageHandler, Updater

import config


updater = Updater(token=config.TOKEN, use_context=True)


def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=update.message.text)


echo_handler = MessageHandler(filters=Filters.text, callback=echo)
updater.dispatcher.add_handler(handler=echo_handler)
updater.start_polling(read_latency=0)
