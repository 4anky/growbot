from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler, Filters, MessageHandler, Updater

import config
import dev
import message_filters as filters
import paid
import states as state
import text
from functional_modules import casino, home, info, markets, sell_goods, side_job, train, utility


fTrainDesc1 = filters.MessageFilter(button=text.TRAIN_DESC_1_BUTTON)
fTrainMarket = filters.MessageFilter(button=text.TRAIN_MARKET_BUTTON)
fTrainDesc2 = filters.MessageFilter(button=text.TRAIN_DESC_2_BUTTON)

fHome = filters.MessageFilter(button=text.HOME_BUTTON)
fMarkets = filters.MessageFilter(button=text.MARKETS_BUTTON)
fSellGoods = filters.MessageFilter(button=text.SELL_GOODS_BUTTON)
fCasino = filters.MessageFilter(button=text.CASINO_BUTTON)
fSideJob = filters.MessageFilter(button=text.SIDE_JOB_BUTTON)
fInfo = filters.MessageFilter(button=text.INFO_BUTTON)
fFarm = filters.MessageFilter(button=text.FARM_BUTTON)
fBalance = filters.MessageFilter(button=text.BALANCE_BUTTON)
fRating = filters.MessageFilter(button=text.RATING_BUTTON)
fRatingMoney = filters.MessageFilter(button=text.RATING_MONEY_BUTTON)
fRatingHarvest = filters.MessageFilter(button=text.RATING_HARVEST_BUTTON)
fHighGrowing = filters.MessageFilter(button=text.HIGH_GROWING_BUTTON)
fDealer = filters.MessageFilter(button=text.DEALER_BUTTON)
fStreet = filters.MessageFilter(button=text.STREET_BUTTON)
fCentre = filters.MessageFilter(button=text.CENTRE_BUTTON)
fOutskirts = filters.MessageFilter(button=text.OUTSKIRTS_BUTTON)
fBribe = filters.MessageFilter(button=text.BRIBE_BUTTON)
fEscape = filters.MessageFilter(button=text.ESCAPE_BUTTON)
fBlackjack = filters.MessageFilter(button=text.BLACKJACK_BUTTON)
fDice = filters.MessageFilter(button=text.DICE_BUTTON)
fLottery = filters.MessageFilter(button=text.LOTTERY_BUTTON)
fTickets = filters.MessageFilter(button=text.TICKETS_NAME)
fBuyTicket = filters.MessageFilter(button=text.BUY_TICKET_BUTTON)
fTranslation = filters.MessageFilter(button=text.TRANSLATION_BUTTON)
fExchange = filters.MessageFilter(button=text.EXCHANGE_BUTTON)
fChip = filters.MessageFilter(button=text.TO_MONEY_BUTTON)
fMoney = filters.MessageFilter(button=text.TO_CHIP_BUTTON)
fInvite = filters.MessageFilter(button=text.INVITE_BUTTON)
fPayment = filters.MessageFilter(button=text.PAYMENT_BUTTON)
fFAQ = filters.MessageFilter(button=text.FAQ_BUTTON)
fCommunity = filters.MessageFilter(button=text.COMMUNITY_BUTTON)
fLetter = filters.MessageFilter(button=text.LETTER_BUTTON)
fVersion = filters.MessageFilter(button=text.VERSION_BUTTON)
fBack = filters.MessageFilter(button=text.BACK_BUTTON)


updater = Updater(token=config.TOKEN, use_context=True)
job_queue = updater.job_queue
Message, Command = MessageHandler, CommandHandler

conversation = ConversationHandler(
    entry_points=[Command(command="start", callback=utility.start),
                  Message(filters=Filters.text, callback=utility.reload)],
    states={
        state.TRAIN_DESC_1: [Message(filters=fTrainDesc1, callback=train.to_market),
                             Command(command="start", callback=train.to_market)],
        state.TRAIN_MARKET: [Message(filters=fTrainMarket, callback=train.to_desc_2),
                             Command(command="start", callback=train.to_desc_2)],
        state.TRAIN_DESC_2: [Message(filters=fTrainDesc2, callback=train.to_nick),
                             Command(command="start", callback=train.to_nick)],
        state.TRAIN_NICK: [Message(filters=Filters.text, callback=train.nick_valid),
                           Command(command="start", callback=train.nick_valid)],
        state.MAIN: [Message(filters=fHome, callback=home.home),
                     Message(filters=fMarkets, callback=markets.markets),
                     Message(filters=fSellGoods, callback=sell_goods.sell_goods),
                     Message(filters=fCasino, callback=casino.casino),
                     Message(filters=fInfo, callback=info.info),
                     Message(filters=fSideJob, callback=side_job.side_job)],
        state.HOME: [Message(filters=fFarm, callback=home.farm),
                     Message(filters=fBalance, callback=home.balance),
                     Message(filters=fRating, callback=home.rating),
                     Message(filters=fBack, callback=utility.back_to_main)],
        state.RATING: [Message(filters=fRatingMoney, callback=home.rating_money),
                       Message(filters=fRatingHarvest, callback=home.rating_harvest),
                       Message(filters=fBack, callback=home.home)],
        state.MARKETS: [Message(filters=fHighGrowing, callback=markets.high_growing),
                        Message(filters=fBack, callback=utility.back_to_main)],
        state.SELL_GOODS: [Message(filters=fDealer, callback=sell_goods.dealer),
                           Message(filters=fStreet, callback=sell_goods.street_enter_high),
                           Message(filters=fBack, callback=utility.back_to_main),
                           Command(command="start", callback=sell_goods.to_sell_goods)],
        state.DEALER: [Message(filters=(Filters.text & (~ fBack)), callback=sell_goods.dealer_result),
                       Message(filters=fBack, callback=sell_goods.sell_goods)],
        state.STREET_ENTER_HIGH: [Message(filters=(Filters.text & (~ fBack)), callback=sell_goods.street_choice_place),
                                  Message(filters=fBack, callback=sell_goods.sell_goods)],
        state.STREET_CHOICE_PLACE: [Message(filters=(fCentre | fOutskirts), callback=sell_goods.street),
                                    Message(filters=fBack, callback=sell_goods.street_enter_high)],
        state.STREET_DETENTION: [Message(filters=fBribe, callback=sell_goods.bribe),
                                 Message(filters=fEscape, callback=sell_goods.escape),
                                 Command(command="start", callback=sell_goods.detention_notify)],
        state.STREET_RETENTION: [Message(filters=fBribe, callback=sell_goods.bribe_after_retention),
                                 Command(command="start", callback=sell_goods.retention_notify)],
        state.CASINO: [Message(filters=fBlackjack, callback=casino.blackjack),
                       Message(filters=fDice, callback=casino.dice),
                       Message(filters=fExchange, callback=casino.exchange),
                       Message(filters=fLottery, callback=casino.lottery_entrance),
                       Message(filters=fBack, callback=utility.back_to_main)],
        state.BJ_BET: [Message(filters=(Filters.text & (~ fBack)), callback=casino.blackjack),
                       Message(filters=fBack, callback=casino.casino)],
        state.EXCHANGE: [Message(filters=fMoney, callback=casino.enter_money),
                         Message(filters=fChip, callback=casino.enter_chip),
                         Message(filters=fBack, callback=casino.casino)],
        state.TO_CHIP: [Message(filters=(Filters.text & (~ fBack)), callback=casino.money_to_chips),
                        Message(filters=fBack, callback=casino.exchange)],
        state.TO_MONEY: [Message(filters=(Filters.text & (~ fBack)), callback=casino.chips_to_money),
                         Message(filters=fBack, callback=casino.exchange)],
        state.LOTTERY: [Message(filters=fTickets, callback=casino.buy_and_watch),
                        Message(filters=fBack, callback=casino.casino)],
        state.BUY_AND_WATCH: [Message(filters=fBuyTicket, callback=casino.buy_ticket),
                              Message(filters=fTranslation, callback=casino.watch_translation),
                              Message(filters=fBack, callback=casino.lottery_entrance)],
        state.SIDE_JOB: [Message(filters=fInvite, callback=side_job.invite),
                         Message(filters=fBack, callback=utility.back_to_main)],
        state.INVITE: [Message(filters=fPayment, callback=side_job.invite_payment),
                       Message(filters=fBack, callback=side_job.side_job)],
        state.INFO: [Message(filters=fFAQ, callback=info.faq),
                     Message(filters=fCommunity, callback=info.community),
                     Message(filters=fLetter, callback=info.letter),
                     Message(filters=fVersion, callback=info.version),
                     Message(filters=fBack, callback=utility.back_to_main)],
        state.LETTER: [Message(filters=((Filters.text | (~ Filters.text)) & (~ fBack)), callback=info.send_letter),
                       Message(filters=fBack, callback=info.info)],
            },
    fallbacks=[Command(command="start", callback=utility.default)]
)


query_handlers = {
    "buy_grow_box": CallbackQueryHandler(callback=markets.buy_grow_box,
                                         pattern='|'.join([size["NAME"] for size in config.SIZES])),
    "harvest": CallbackQueryHandler(callback=home.harvest, pattern=config.PATTERN_HARVEST)
}

dev_commands = {
    "players": Command(command="players", callback=dev.players),
    "users": Command(command="users", callback=dev.users),
    "farm": Command(command="farm", callback=dev.farm, pass_args=True),
    "msg": Command(command="msg", callback=dev.msg, pass_args=True),
    "ss_3d": Command(command="ss_3d", callback=paid.safer_street_3d),
    "ss_10d": Command(command="ss_10d", callback=paid.safer_street_10d),
    "ss_30d": Command(command="ss_30d", callback=paid.safer_street_30d),
}

for handler in query_handlers.values():
    updater.dispatcher.add_handler(handler=handler)
for handler in dev_commands.values():
    updater.dispatcher.add_handler(handler=handler)
updater.dispatcher.add_handler(handler=conversation)

job_queue.run_daily(callback=casino.lottery, time=config.LOTTERY_TIME.time(), days=(0, 1, 2, 3, 4, 5, 6))
updater.start_polling(read_latency=0)
