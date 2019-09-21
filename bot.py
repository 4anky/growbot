from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler, Updater

import config
import message_filters as filters

HOME = 0

fMarket = filters.Market()
fSell = filters.Sell()
fBones = filters.Bones()
fInfo = filters.Info()

updater = Updater(token=config.TOKEN, use_context=True)

def home_keyboard():
    keyboard = [[KeyboardButton(text="📦Магазин"), KeyboardButton(text="🌳Продать шишки")],
                [KeyboardButton(text="🎲Кости"), KeyboardButton(text="📢Информация")]]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы перешли в 'Главное Меню'",
                             reply_markup=home_keyboard())
    return HOME


def market(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы нажали кнопку 'Магазин'",
                             reply_markup=home_keyboard())
    return HOME


def sell(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы нажали кнопку 'Продать шишки'",
                             reply_markup=home_keyboard())
    return HOME


def bones(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы нажали кнопку 'Кости'",
                             reply_markup=home_keyboard())
    return HOME


def info(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Вы нажали кнопку 'Информация'",
                             reply_markup=home_keyboard())
    return HOME


def default(context, update):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Что-то пошло не так.\n"
                                  "Возвращаемся в 'Главное Меню'",
                             reply_markup=home_keyboard())
    return HOME


conversation = ConversationHandler(
    entry_points=[CommandHandler(command="start", callback=start)],
    states={HOME: [MessageHandler(filters=fMarket, callback=market),
                   MessageHandler(filters=fSell, callback=sell),
                   MessageHandler(filters=fBones, callback=bones),
                   MessageHandler(filters=fInfo, callback=info)]
    },
    fallbacks=[MessageHandler(filters=Filters.text, callback=default)]
)

updater.dispatcher.add_handler(handler=conversation)
updater.start_polling(read_latency=0)
