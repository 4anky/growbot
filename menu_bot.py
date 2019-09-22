from telegram import KeyboardButton, ReplyKeyboardMarkup

back_button = "◀️Назад"
main = (("🏠Дом", "🏬Магазины"),
        ("💰Продать товар", "🎰Казино"),
        ("💸Подработка", "📢Информация"))
home = (("🌱Ферма", "📦Склад"),
        ("🏆Рейтинг", back_button))
markets = (("🐲HighGrowing", back_button), )
sell_goods = (("👳🏻‍♂️Агент", "🔪Улица"),
              (back_button, ""))
casino = (("🎲Кости", back_button), )
side_job = (("🙋🏼‍♂️Пригласи друга", back_button), )
info = (("❓FAQ", "💬Сообщество"),
        ("✉️Письмо авторам", "✅Версия игры"),
        (back_button, ""))


def show(buttons):
    keyboard = [[KeyboardButton(text=column[0]),
                 KeyboardButton(text=column[1])]
                for column in buttons]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
