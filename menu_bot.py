from telegram import KeyboardButton, ReplyKeyboardMarkup

main = (("🏠Дом", "🏬Магазины"),
        ("💰Продать товар", "🎰Казино"),
        ("💸Подработка", "📢Информация"))
home = (("🌱", "📦"), ("🏆", "◀️"))


def show(buttons):
    keyboard = [[KeyboardButton(text=column[0]),
                 KeyboardButton(text=column[1])]
                for column in buttons]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
