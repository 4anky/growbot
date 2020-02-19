from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler, Filters, MessageHandler,\
    PicklePersistence, Updater

import config
import dev
import message_filters as filters
import paid
import states as state
import text
from functional_modules import casino, home, info, markets, sell_goods, side_job, train, twenty_one, utility


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
fTwentyOne = filters.MessageFilter(button=text.TWENTY_ONE_BUTTON)
fTOEntry = filters.MessageFilter(button=text.TO_ENTRY_BUTTON)
fTORules = filters.MessageFilter(button=text.TO_RULES_BUTTON)
fTORatingGamesNumber = filters.MessageFilter(button=text.GAMES_NUMBER_BUTTON)
fTORatingWinPercent = filters.MessageFilter(button=text.WIN_PERCENT_BUTTON)
fTORatingMaxWin = filters.MessageFilter(button=text.MAX_WIN_BUTTON)
fTORatingMaxLose = filters.MessageFilter(button=text.MAX_LOSE_BUTTON)
fTOMyStats = filters.MessageFilter(button=text.TO_MY_STATS_BUTTON)
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

bot_persistence = PicklePersistence(filename="materials/persistence_file")
updater = Updater(token=config.TOKEN, persistence=bot_persistence, use_context=True)
job_queue = updater.job_queue

conversation = ConversationHandler(
    entry_points=[CommandHandler(command="start", callback=utility.start),
                  MessageHandler(filters=Filters.text, callback=utility.reload)],
    states={
        state.TRAIN_DESC_1: [MessageHandler(filters=fTrainDesc1, callback=train.to_market),
                             CommandHandler(command="start", callback=train.to_market)],
        state.TRAIN_MARKET: [MessageHandler(filters=fTrainMarket, callback=train.to_desc_2),
                             CommandHandler(command="start", callback=train.to_desc_2)],
        state.TRAIN_DESC_2: [MessageHandler(filters=fTrainDesc2, callback=train.to_nick),
                             CommandHandler(command="start", callback=train.to_nick)],
        state.TRAIN_NICK: [MessageHandler(filters=Filters.text, callback=train.nick_valid),
                           CommandHandler(command="start", callback=train.nick_valid)],
        state.MAIN: [MessageHandler(filters=fHome, callback=home.home),
                     MessageHandler(filters=fMarkets, callback=markets.markets),
                     MessageHandler(filters=fSellGoods, callback=sell_goods.sell_goods),
                     MessageHandler(filters=fCasino, callback=casino.casino),
                     MessageHandler(filters=fInfo, callback=info.info),
                     MessageHandler(filters=fSideJob, callback=side_job.side_job),
                     CommandHandler(command="start", callback=utility.start)],
        state.HOME: [MessageHandler(filters=fFarm, callback=home.farm),
                     MessageHandler(filters=fBalance, callback=home.balance),
                     MessageHandler(filters=fRating, callback=home.rating),
                     MessageHandler(filters=fBack, callback=utility.back_to_main)],
        state.RATING: [MessageHandler(filters=fRatingMoney, callback=home.rating_money),
                       MessageHandler(filters=fRatingHarvest, callback=home.rating_harvest),
                       MessageHandler(filters=fBack, callback=home.home)],
        state.MARKETS: [MessageHandler(filters=fHighGrowing, callback=markets.high_growing),
                        MessageHandler(filters=fBack, callback=utility.back_to_main)],
        state.SELL_GOODS: [MessageHandler(filters=fDealer, callback=sell_goods.dealer),
                           MessageHandler(filters=fStreet, callback=sell_goods.street_enter_high),
                           MessageHandler(filters=fBack, callback=utility.back_to_main),
                           CommandHandler(command="start", callback=sell_goods.to_sell_goods)],
        state.DEALER: [MessageHandler(filters=(Filters.text & (~ fBack)), callback=sell_goods.dealer_result),
                       MessageHandler(filters=fBack, callback=sell_goods.sell_goods)],
        state.STREET_ENTER_HIGH: [MessageHandler(filters=(Filters.text & (~ fBack)),
                                                 callback=sell_goods.street_choice_place),
                                  MessageHandler(filters=fBack, callback=sell_goods.sell_goods)],
        state.STREET_CHOICE_PLACE: [MessageHandler(filters=(fCentre | fOutskirts), callback=sell_goods.street),
                                    MessageHandler(filters=fBack, callback=sell_goods.street_enter_high)],
        state.STREET_DETENTION: [MessageHandler(filters=fBribe, callback=sell_goods.bribe),
                                 MessageHandler(filters=fEscape, callback=sell_goods.escape),
                                 CommandHandler(command="start", callback=sell_goods.detention_notify)],
        state.STREET_RETENTION: [MessageHandler(filters=fBribe, callback=sell_goods.bribe_after_retention),
                                 CommandHandler(command="start", callback=sell_goods.retention_notify)],
        state.CASINO: [MessageHandler(filters=fTwentyOne, callback=casino.twenty_one),
                       MessageHandler(filters=fDice, callback=casino.dice),
                       MessageHandler(filters=fExchange, callback=casino.exchange),
                       MessageHandler(filters=fLottery, callback=casino.lottery_entrance),
                       MessageHandler(filters=fBack, callback=utility.back_to_main)],
        state.TWENTY_ONE: [MessageHandler(filters=fTOEntry, callback=twenty_one.entry),
                           MessageHandler(filters=fTORules, callback=twenty_one.rules),
                           MessageHandler(filters=fRating, callback=twenty_one.rating),
                           MessageHandler(filters=fTOMyStats, callback=twenty_one.my_stats),
                           MessageHandler(filters=fBack, callback=casino.casino),
                           CommandHandler(command="start", callback=twenty_one.stub)],
        state.TWENTY_ONE_ENTER_BET: [MessageHandler(filters=(Filters.text & (~ fBack)),
                                                    callback=twenty_one.game,
                                                    pass_job_queue=True),
                                     MessageHandler(filters=fBack, callback=casino.twenty_one),
                                     CommandHandler(command="start", callback=twenty_one.stub_enter_bet)],
        state.TWENTY_ONE_RATING: [MessageHandler(filters=fTORatingGamesNumber, callback=twenty_one.games_number_rating),
                                  MessageHandler(filters=fTORatingWinPercent, callback=twenty_one.win_percent_rating),
                                  MessageHandler(filters=fTORatingMaxWin, callback=twenty_one.max_win_rating),
                                  MessageHandler(filters=fTORatingMaxLose, callback=twenty_one.max_lose_rating),
                                  MessageHandler(filters=fBack, callback=casino.twenty_one)],
        state.EXCHANGE: [MessageHandler(filters=fMoney, callback=casino.enter_money),
                         MessageHandler(filters=fChip, callback=casino.enter_chip),
                         MessageHandler(filters=fBack, callback=casino.casino)],
        state.TO_CHIP: [MessageHandler(filters=(Filters.text & (~ fBack)), callback=casino.money_to_chips),
                        MessageHandler(filters=fBack, callback=casino.exchange)],
        state.TO_MONEY: [MessageHandler(filters=(Filters.text & (~ fBack)), callback=casino.chips_to_money),
                         MessageHandler(filters=fBack, callback=casino.exchange)],
        state.LOTTERY: [MessageHandler(filters=fTickets, callback=casino.buy_and_watch),
                        MessageHandler(filters=fBack, callback=casino.casino)],
        state.BUY_AND_WATCH: [MessageHandler(filters=fBuyTicket, callback=casino.buy_ticket),
                              MessageHandler(filters=fTranslation, callback=casino.watch_translation),
                              MessageHandler(filters=fBack, callback=casino.lottery_entrance)],
        state.SIDE_JOB: [MessageHandler(filters=fInvite, callback=side_job.invite),
                         MessageHandler(filters=fBack, callback=utility.back_to_main)],
        state.INVITE: [MessageHandler(filters=fPayment, callback=side_job.invite_payment),
                       MessageHandler(filters=fBack, callback=side_job.side_job)],
        state.INFO: [MessageHandler(filters=fFAQ, callback=info.faq),
                     MessageHandler(filters=fCommunity, callback=info.community),
                     MessageHandler(filters=fLetter, callback=info.letter),
                     MessageHandler(filters=fVersion, callback=info.version),
                     MessageHandler(filters=fBack, callback=utility.back_to_main)],
        state.LETTER: [MessageHandler(filters=((Filters.text | (~ Filters.text)) & (~ fBack)),
                                      callback=info.send_letter),
                       MessageHandler(filters=fBack, callback=info.info)],
            },
    fallbacks=[CommandHandler(command="start", callback=utility.default)],
    persistent=True, name="Weed Grow"
)

query_handlers = {
    "buy_grow_box": CallbackQueryHandler(callback=markets.buy_grow_box,
                                         pattern='|'.join([size["NAME"] for size in config.SIZES])),
    "harvest": CallbackQueryHandler(callback=home.harvest, pattern=config.PATTERN_HARVEST, pass_job_queue=True),

    "more": CallbackQueryHandler(callback=twenty_one.more, pattern=config.MORE_PATTERN, pass_job_queue=True),
    "enough": CallbackQueryHandler(callback=twenty_one.yourself, pattern=config.YOURSELF_PATTERN, pass_job_queue=True),
    "blind": CallbackQueryHandler(callback=twenty_one.blind, pattern=config.BLIND_PATTERN, pass_job_queue=True),
    "finish": CallbackQueryHandler(callback=twenty_one.finish, pattern=config.FINISH_PATTERN, pass_job_queue=True),
    "main_rules": CallbackQueryHandler(callback=twenty_one.main_rules, pattern=config.MAIN_RULES_PATTERN),
    "for_win": CallbackQueryHandler(callback=twenty_one.game_progress_rules, pattern=config.FOR_WIN_PATTERN),
    "blind_rules": CallbackQueryHandler(callback=twenty_one.blind_rules, pattern=config.BLIND_RULES_PATTERN),
    "points": CallbackQueryHandler(callback=twenty_one.points_rules, pattern=config.POINTS_PATTERN),
    "all_is_ok": CallbackQueryHandler(callback=twenty_one.all_is_ok, pattern=config.ALL_OK_PATTERN),
}
dev_commands = {
    "players": CommandHandler(command="players", callback=dev.players),
    "users": CommandHandler(command="users", callback=dev.users),
    "farm": CommandHandler(command="farm", callback=dev.farm, pass_args=True),
    "msg": CommandHandler(command="msg", callback=dev.msg, pass_args=True),
    "ss_3d": CommandHandler(command="ss_3d", callback=paid.safer_street_3d),
    "ss_10d": CommandHandler(command="ss_10d", callback=paid.safer_street_10d),
    "ss_30d": CommandHandler(command="ss_30d", callback=paid.safer_street_30d),
}

for handler in query_handlers.values():
    updater.dispatcher.add_handler(handler=handler)
for handler in dev_commands.values():
    updater.dispatcher.add_handler(handler=handler)
updater.dispatcher.add_handler(handler=conversation)

job_queue.run_daily(callback=casino.lottery, time=config.LOTTERY_TIME.time(), days=(0, 1, 2, 3, 4, 5, 6))
updater.start_polling(read_latency=0)
