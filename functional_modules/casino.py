from telegram import ParseMode

import config
import menu_bot as menu
import sql
import states as state


def casino(update, _):
    update.message.reply_photo(photo=open(file=config.CASINO_PIC_PATH, mode='rb'),
                               caption=config.CASINO_DESC,
                               reply_markup=menu.show(menu=config.CASINO),
                               parse_mode=ParseMode.MARKDOWN)
    return state.CASINO


def blackjack(update, _):
    update.message.reply_photo(photo=open(file=config.CASINO_PIC_PATH, mode='rb'),
                               caption=config.CASINO_DESC,
                               reply_markup=menu.show(menu=config.CASINO),
                               parse_mode=ParseMode.MARKDOWN)
    return state.CASINO


def dice(update, _):
    update.message.reply_photo(photo=open(file=config.CASINO_PIC_PATH, mode='rb'),
                               caption=config.CASINO_DESC,
                               reply_markup=menu.show(menu=config.CASINO),
                               parse_mode=ParseMode.MARKDOWN)
    return state.CASINO


def exchange(update, _):
    update.message.reply_markdown(text=config.EXCHANGE_DESC, reply_markup=menu.show(menu=config.EXCHANGE))
    return state.EXCHANGE


def enter_money(update, context):
    money, _, chip = sql.get_balance(db_path=config.DB_PATH, telegram_id=update.message.chat.id)
    context.user_data["money"] = money
    update.message.reply_markdown(
        text=config.MONEY_TO_CHIP_TEXT.format(money=money, chip=chip), reply_markup=menu.show(menu=config.BACK))
    return state.TO_CHIP


def money_to_chips(update, context):
    try:
        money_for_exchange = int(update.message.text)
    except ValueError:
        update.message.reply_markdown(text=config.NOT_POSITIVE_NUMBER, reply_markup=menu.show(menu=config.BACK))
        return state.TO_CHIP
    else:
        if money_for_exchange <= 0:
            update.message.reply_markdown(text=config.NOT_POSITIVE_NUMBER, reply_markup=menu.show(menu=config.BACK))
            return state.TO_CHIP
        elif money_for_exchange > context.user_data["money"]:
            update.message.reply_markdown(text=config.NOT_ENOUGH_MONEY.format(money=context.user_data["money"]))
            return state.TO_CHIP
        else:
            chips = money_for_exchange * config.CHIPS_FOR_CURRENCY_UNIT - config.COMMISSION
            sql.money_to_chips(
                db_path=config.DB_PATH,
                telegram_id=update.message.chat.id,
                money=money_for_exchange,
                chip=chips)
            money, _, chip = sql.get_balance(db_path=config.DB_PATH, telegram_id=update.message.chat.id)
            update.message.reply_markdown(
                text=config.BUY_CHIPS.format(new=chips, money=money, chip=chip),
                reply_markup=menu.show(menu=config.EXCHANGE))
            return state.EXCHANGE


def enter_chip(update, context):
    money, _, chip = sql.get_balance(db_path=config.DB_PATH, telegram_id=update.message.chat.id)
    context.user_data["chip"] = chip
    update.message.reply_markdown(
        text=config.CHIP_TO_MONEY_TEXT.format(money=money, chip=chip), reply_markup=menu.show(menu=config.BACK))
    return state.TO_MONEY


def chips_to_money(update, context):
    try:
        chips_for_exchange = int(update.message.text)
    except ValueError:
        update.message.reply_markdown(text=config.NOT_POSITIVE_NUMBER, reply_markup=menu.show(menu=config.BACK))
        return state.TO_MONEY
    else:
        if chips_for_exchange <= 0:
            update.message.reply_markdown(text=config.NOT_POSITIVE_NUMBER, reply_markup=menu.show(menu=config.BACK))
            return state.TO_MONEY
        elif chips_for_exchange > context.user_data["chip"]:
            update.message.reply_markdown(text=config.NOT_ENOUGH_CHIP.format(chip=context.user_data["chip"]))
            return state.TO_MONEY
        else:
            new_money = (chips_for_exchange - config.COMMISSION) // config.CHIPS_FOR_CURRENCY_UNIT
            unchanged_chips = (chips_for_exchange - config.COMMISSION) % config.CHIPS_FOR_CURRENCY_UNIT
            sql.chips_to_money(
                db_path=config.DB_PATH,
                telegram_id=update.message.chat.id,
                money=new_money,
                chip=context.user_data["chip"] - unchanged_chips)
            money, _, chip = sql.get_balance(db_path=config.DB_PATH, telegram_id=update.message.chat.id)
            update.message.reply_markdown(
                text=config.SELL_CHIPS.format(new=new_money, money=money, chip=chip),
                reply_markup=menu.show(menu=config.EXCHANGE))
            return state.EXCHANGE
