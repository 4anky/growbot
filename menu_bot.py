from telegram import KeyboardButton, ReplyKeyboardMarkup

import constants as const

main = ((const.HOME_BUTTON, const.MARKETS_BUTTON),
        (const.SELL_GOODS_BUTTON, const.CASINO_BUTTON),
        (const.SIDE_JOB_BUTTON, const.INFO_BUTTON))
home = ((const.FARM_BUTTON, const.STOCK_BUTTON),
        (const.RATING_BUTTON, const.BACK_BUTTON))
markets = ((const.HIGH_GROWING_BUTTON, const.BACK_BUTTON), )
sell_goods = ((const.AGENT_BUTTON, const.STREET_BUTTON),
              (const.BACK_BUTTON, const.EMPTY_BUTTON))
casino = ((const.DICE_BUTTON, const.BACK_BUTTON), )
side_job = ((const.INVITE_BUTTON, const.BACK_BUTTON), )
info = ((const.FAQ_BUTTON, const.COMMUNITY_BUTTON),
        (const.LETTER_BUTTON, const.VERSION_BUTTON),
        (const.BACK_BUTTON, const.EMPTY_BUTTON))


def show(buttons):
    keyboard = [[KeyboardButton(text=column[const.LEFT]),
                 KeyboardButton(text=column[const.RIGHT])]
                for column in buttons]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
