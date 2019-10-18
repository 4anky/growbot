from telegram import ParseMode

import config
import menu_bot as menu
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
                               caption=config.DICE_DESC,
                               reply_markup=menu.show(menu=config.CASINO),
                               parse_mode=ParseMode.MARKDOWN)
    return state.CASINO


def exchange(update, _):
    update.message.reply_markdown(text=config.EXCHANGE_DESC, reply_markup=menu.show(menu=config.EXCHANGE))
    return state.EXCHANGE


def to_chip(update, _):
    update.message.reply_markdown(
        text="Обмен 💰 скоро заработает, 🕑 ждите", reply_markup=menu.show(menu=config.EXCHANGE))
    return state.EXCHANGE


def to_money(update, _):
    update.message.reply_markdown(
        text="Обмен 🔴 скоро заработает, 🕑 ждите", reply_markup=menu.show(menu=config.EXCHANGE))
    return state.EXCHANGE
