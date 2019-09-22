from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler, Updater

import config
import message_filters as filters
import states as state
from functional_modules import casino, home, info, markets, sell_goods, side_job, utility


fHome = filters.Home()
fMarkets = filters.Markets()
fSellGoods = filters.SellGoods()
fCasino = filters.Casino()
fSideJob = filters.SideJob()
fInfo = filters.Info()

updater = Updater(token=config.TOKEN, use_context=True)

conversation = ConversationHandler(
    entry_points=[CommandHandler(command="start", callback=utility.start)],
    states={state.MAIN: [MessageHandler(filters=fHome, callback=home.home),
                         MessageHandler(filters=fMarkets, callback=markets.markets),
                         MessageHandler(filters=fSellGoods, callback=sell_goods.sell_goods),
                         MessageHandler(filters=fCasino, callback=casino.casino),
                         MessageHandler(filters=fInfo, callback=info.info),
                         MessageHandler(filters=fSideJob, callback=side_job.side_job)
                         ]
            },
    fallbacks=[MessageHandler(filters=Filters.text, callback=utility.default)]
)

updater.dispatcher.add_handler(handler=conversation)
updater.start_polling(read_latency=0)
