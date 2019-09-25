from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import constants as const


def show(menu):
    keyboard = [[KeyboardButton(text=column[const.LEFT]),
                 KeyboardButton(text=column[const.RIGHT])]
                for column in menu]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def high_growing_buy_button(text, name):
    keyboard = [[InlineKeyboardButton(text=text, callback_data=name)]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
