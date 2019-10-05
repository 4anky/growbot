from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import config


def show(menu):
    keyboard = [[KeyboardButton(text=column[config.LEFT]),
                 KeyboardButton(text=column[config.RIGHT])]
                for column in menu]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def inline_button(text, data):
    keyboard = [[InlineKeyboardButton(text=text, callback_data=data)]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def no_menu():
    return ReplyKeyboardRemove()
