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

fFarm = filters.Farm()
fStock = filters.Stock()
fRating = filters.Rating()

fHighGrowing = filters.HighGrowing()

fAgent = filters.Agent()
fStreet = filters.Street()

fBones = filters.Bones()

fInvite = filters.Invite()

fFAQ = filters.FAQ()
fCommunity = filters.Community()
fLetter = filters.Letter()
fVersion = filters.Version()

fBack = filters.Back()

updater = Updater(token=config.TOKEN, use_context=True)

conversation = ConversationHandler(
    entry_points=[CommandHandler(command="start", callback=utility.start)],
    states={state.MAIN: [MessageHandler(filters=fHome, callback=home.home),
                         MessageHandler(filters=fMarkets, callback=markets.markets),
                         MessageHandler(filters=fSellGoods, callback=sell_goods.sell_goods),
                         MessageHandler(filters=fCasino, callback=casino.casino),
                         MessageHandler(filters=fInfo, callback=info.info),
                         MessageHandler(filters=fSideJob, callback=side_job.side_job)
                         ],
            state.HOME: [MessageHandler(filters=fFarm, callback=home.farm),
                         MessageHandler(filters=fStock, callback=home.stock),
                         MessageHandler(filters=fRating, callback=home.rating),
                         MessageHandler(filters=fBack, callback=utility.back_to_main)
                         ],
            state.MARKETS: [MessageHandler(filters=fHighGrowing, callback=markets.high_growing),
                            MessageHandler(filters=fBack, callback=utility.back_to_main)
                            ],
            state.SELL_GOODS: [MessageHandler(filters=fAgent, callback=sell_goods.agent),
                               MessageHandler(filters=fStreet, callback=sell_goods.street),
                               MessageHandler(filters=fBack, callback=utility.back_to_main)
                               ],
            state.CASINO: [MessageHandler(filters=fBones, callback=casino.bones),
                           MessageHandler(filters=fBack, callback=utility.back_to_main)
                           ],
            state.SIDE_JOB: [MessageHandler(filters=fInvite, callback=side_job.invite),
                             MessageHandler(filters=fBack, callback=utility.back_to_main)
                             ],
            state.INFO: [MessageHandler(filters=fFAQ, callback=info.faq),
                         MessageHandler(filters=fCommunity, callback=info.community),
                         MessageHandler(filters=fLetter, callback=info.letter),
                         MessageHandler(filters=fVersion, callback=info.version),
                         MessageHandler(filters=fBack, callback=utility.back_to_main)
                         ]
            },
    fallbacks=[MessageHandler(filters=Filters.text, callback=utility.default)]
)

updater.dispatcher.add_handler(handler=conversation)
updater.start_polling(read_latency=0.2)
