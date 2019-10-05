from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler, Filters, MessageHandler, Updater

import config
import message_filters as filters
import states as state
from functional_modules import casino, home, info, markets, sell_goods, side_job, train, utility

fTrainDesc1 = filters.MessageFilter(button=config.TRAIN_DESC_1_BUTTON)
fTrainMarket = filters.MessageFilter(button=config.TRAIN_MARKET_BUTTON)
fTrainDesc2 = filters.MessageFilter(button=config.TRAIN_DESC_2_BUTTON)

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
fDealer = filters.MessageFilter(button=config.DEALER_BUTTON)
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
                  MessageHandler(filters=Filters.text, callback=utility.reload)
                  ],
    states={state.TRAIN_DESC_1: [MessageHandler(filters=fTrainDesc1, callback=train.to_market),
                                 CommandHandler(command="start", callback=train.to_market)
                                 ],
            state.TRAIN_MARKET: [MessageHandler(filters=fTrainMarket, callback=train.to_desc_2),
                                 CommandHandler(command="start", callback=train.to_desc_2)
                                 ],
            state.TRAIN_DESC_2: [MessageHandler(filters=fTrainDesc2, callback=train.to_nick),
                                 CommandHandler(command="start", callback=train.to_nick)
                                 ],
            state.TRAIN_NICK: [MessageHandler(filters=Filters.text, callback=train.nick_valid),
                               CommandHandler(command="start", callback=train.nick_valid)
                               ],
            state.MAIN: [MessageHandler(filters=fHome, callback=home.home),
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
            state.SELL_GOODS: [MessageHandler(filters=fDealer, callback=sell_goods.dealer),
                               MessageHandler(filters=fStreet, callback=sell_goods.street),
                               MessageHandler(filters=fBack, callback=utility.back_to_main)
                               ],
            state.DEALER: [MessageHandler(filters=(Filters.text & (~ fBack)), callback=sell_goods.dealer_result),
                           MessageHandler(filters=fBack, callback=sell_goods.sell_goods)],
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
    fallbacks=[CommandHandler(command="start", callback=utility.default)]
)
query_handlers = {
    "buy_grow_box": CallbackQueryHandler(callback=markets.buy_grow_box,
                                         pattern='|'.join([size["NAME"] for size in config.SIZES])),
    "harvest": CallbackQueryHandler(callback=home.harvest, pattern=config.PATTERN_HARVEST)
}

for handler in query_handlers.values():
    updater.dispatcher.add_handler(handler=handler)
updater.dispatcher.add_handler(handler=conversation)
updater.start_polling(read_latency=0.2)
