from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler, Filters, MessageHandler, Updater

import config
import message_filters as filters
import states as state
from functional_modules import casino, home, info, markets, sell_goods, side_job, utility

fHome = filters.MessageFilter(button=config.HOME_BUTTON)
fMarkets = filters.MessageFilter(button=config.MARKETS_BUTTON)
fSellGoods = filters.MessageFilter(button=config.SELL_GOODS_BUTTON)
fCasino = filters.MessageFilter(button=config.CASINO_BUTTON)
fSideJob = filters.MessageFilter(button=config.SIDE_JOB_BUTTON)
fInfo = filters.MessageFilter(button=config.INFO_BUTTON)
fFarm = filters.MessageFilter(button=config.FARM_BUTTON)
fBalance = filters.MessageFilter(button=config.BALANCE_BUTTON)
fRating = filters.MessageFilter(button=config.RATING_BUTTON)
fHighGrowing = filters.MessageFilter(button=config.HIGH_GROWING_BUTTON)
fAgent = filters.MessageFilter(button=config.AGENT_BUTTON)
fStreet = filters.MessageFilter(button=config.STREET_BUTTON)
fDice = filters.MessageFilter(button=config.DICE_BUTTON)
fInvite = filters.MessageFilter(button=config.INVITE_BUTTON)
fFAQ = filters.MessageFilter(button=config.FAQ_BUTTON)
fCommunity = filters.MessageFilter(button=config.COMMUNITY_BUTTON)
fLetter = filters.MessageFilter(button=config.LETTER_BUTTON)
fVersion = filters.MessageFilter(button=config.VERSION_BUTTON)
fBack = filters.MessageFilter(button=config.BACK_BUTTON)

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
                         MessageHandler(filters=fBalance, callback=home.balance),
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
            state.CASINO: [MessageHandler(filters=fDice, callback=casino.dice),
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

buy_grow_box_handler = CallbackQueryHandler(callback=markets.buy_grow_box,
                                            pattern='|'.join([size["NAME"] for size in config.SIZES]))

updater.dispatcher.add_handler(handler=buy_grow_box_handler)
updater.dispatcher.add_handler(handler=conversation)
updater.start_polling(read_latency=0.2)
