# Menu and Menu buttons

LEFT = 0
RIGHT = 1

BACK_BUTTON = "◀️Назад"
EMPTY_BUTTON = ""

HOME_BUTTON = "🏡Дом"
MARKETS_BUTTON = "🏬Магазины"
SELL_GOODS_BUTTON = "💰Продать товар"
CASINO_BUTTON = "🎰Казино"
SIDE_JOB_BUTTON = "💶Подработка"
INFO_BUTTON = "📣Информация"

FARM_BUTTON = "🌱Ферма"
STOCK_BUTTON = "📦Склад"
RATING_BUTTON = "🏆Рейтинг"

HIGH_GROWING_BUTTON = "🐲HighGrowing"

AGENT_BUTTON = "👳🏻‍♂️Агент"
STREET_BUTTON = "🔪Улица"

DICE_BUTTON = "🎲Кости"

INVITE_BUTTON = "🙋🏼‍♂️Пригласи друга"

FAQ_BUTTON = "❓FAQ"
COMMUNITY_BUTTON = "💬Сообщество"
LETTER_BUTTON = "✉️Письмо авторам"
VERSION_BUTTON = "✅Версия игры"

MAIN = ((HOME_BUTTON, MARKETS_BUTTON),
        (SELL_GOODS_BUTTON, CASINO_BUTTON),
        (SIDE_JOB_BUTTON, INFO_BUTTON))
HOME = ((FARM_BUTTON, STOCK_BUTTON),
        (RATING_BUTTON, BACK_BUTTON))
MARKETS = ((HIGH_GROWING_BUTTON, BACK_BUTTON), )
SELL_GOODS = ((AGENT_BUTTON, STREET_BUTTON),
              (BACK_BUTTON, EMPTY_BUTTON))
CASINO = ((DICE_BUTTON, BACK_BUTTON), )
SIDE_JOB = ((INVITE_BUTTON, BACK_BUTTON), )
INFO = ((FAQ_BUTTON, COMMUNITY_BUTTON),
        (LETTER_BUTTON, VERSION_BUTTON),
        (BACK_BUTTON, EMPTY_BUTTON))

# HighGrowing Market

BUY_BUTTON = "Купить"

HIGH_GROWING_CAPTION = "🔹 *{about}*\n" \
                       "Сорт: *{name}*\n" \
                       "Добывает: *{mining}* 🌳 в час\n" \
                       "Цена: *{price}* 💰"
XS = {"SIZE": "XS", "PATH": "materials/XS.jpg", "DESC": "Grow-box на 2 растения",
      "NAME": "Belladonna", "MINING": 16, "PRICE": 101}
S = {"SIZE": "S", "PATH": "materials/S.jpg", "DESC": "Grow-box на 4 растения",
     "NAME": "Skunk+", "MINING": 184, "PRICE": 1000}
M = {"SIZE": "M", "PATH": "materials/M.jpg", "DESC": "Grow-box на 8 растений",
     "NAME": "Sour Diesel", "MINING": 1249, "PRICE": 6500}
L = {"SIZE": "L", "PATH": "materials/L.jpg", "DESC": "Grow-box на 24 растения",
     "NAME": "White Russian", "MINING": 3463, "PRICE": 18000}
XL = {"SIZE": "XL", "PATH": "materials/XL.jpg", "DESC": "Grow-room на 50 растений",
      "NAME": "Black Water", "MINING": 13020, "PRICE": 65000}
XXL = {"SIZE": "XXL", "PATH": "materials/XXL.jpg", "DESC": "Grow-room на 100 растений",
       "NAME": "Original Gorilla Glue 4 S1", "MINING": 31250, "PRICE": 190000}

SIZES = [XS, S, M, L, XL, XXL]

# SQL

REG_QUERY = "INSERT OR IGNORE INTO users VALUES (?, ?, ?)"
