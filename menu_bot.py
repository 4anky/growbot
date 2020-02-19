from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import config


def show(menu):
    keyboard = [[KeyboardButton(text=column[config.LEFT]), KeyboardButton(text=column[config.RIGHT])]
                for column in menu]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def inline_show(menu, patterns):
    keyboard = [[InlineKeyboardButton(text=column[config.LEFT], callback_data=pattern[config.LEFT]),
                 InlineKeyboardButton(text=column[config.RIGHT], callback_data=pattern[config.RIGHT])]
                for column, pattern in zip(menu, patterns)]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def inline_button(text, data):
    keyboard = [[InlineKeyboardButton(text=text, callback_data=data)]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def no_menu():
    return ReplyKeyboardRemove()
