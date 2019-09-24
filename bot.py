from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler, Updater

import config
import constants as const
import message_filters as filters
import states as state
from functional_modules import casino, home, info, markets, sell_goods, side_job, utility

fHome = filters.MessageFilter(button=const.HOME_BUTTON)
fMarkets = filters.MessageFilter(button=const.MARKETS_BUTTON)
fSellGoods = filters.MessageFilter(button=const.SELL_GOODS_BUTTON)
fCasino = filters.MessageFilter(button=const.CASINO_BUTTON)
fSideJob = filters.MessageFilter(button=const.SIDE_JOB_BUTTON)
fInfo = filters.MessageFilter(button=const.INFO_BUTTON)
fFarm = filters.MessageFilter(button=const.FARM_BUTTON)
fStock = filters.MessageFilter(button=const.STOCK_BUTTON)
fRating = filters.MessageFilter(button=const.RATING_BUTTON)
fHighGrowing = filters.MessageFilter(button=const.HIGH_GROWING_BUTTON)
fAgent = filters.MessageFilter(button=const.AGENT_BUTTON)
fStreet = filters.MessageFilter(button=const.STREET_BUTTON)
fDice = filters.MessageFilter(button=const.DICE_BUTTON)
fInvite = filters.MessageFilter(button=const.INVITE_BUTTON)
fFAQ = filters.MessageFilter(button=const.FAQ_BUTTON)
fCommunity = filters.MessageFilter(button=const.COMMUNITY_BUTTON)
fLetter = filters.MessageFilter(button=const.LETTER_BUTTON)
fVersion = filters.MessageFilter(button=const.VERSION_BUTTON)
fBack = filters.MessageFilter(button=const.BACK_BUTTON)

updater = Updater(token=config.TOKEN, use_context=True)

conversation = ConversationHandler(
    entry_points=[CommandHandler(command="start", callback=utility.start),
                  MessageHandler(filters=Filters.text, callback=utility.reload)],
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
            state.CASINO: [MessageHandler(filters=fDice, callback=casino.bones),
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
