# Bot

TOKEN = "TOKEN"

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
BALANCE_BUTTON = "💵Баланс"
RATING_BUTTON = "🏆Рейтинг"

HIGH_GROWING_BUTTON = "🐲HighGrowing"

AGENT_BUTTON = "👳🏻‍♂️Агент"
STREET_BUTTON = "🌃Улица"

DICE_BUTTON = "🎲Кости"

INVITE_BUTTON = "🙋🏼‍♂️Пригласи друга"

FAQ_BUTTON = "❓FAQ"
COMMUNITY_BUTTON = "💬Сообщество"
LETTER_BUTTON = "✉️Письмо авторам"
VERSION_BUTTON = "✅Версия игры"

MAIN = ((HOME_BUTTON, MARKETS_BUTTON),
        (SELL_GOODS_BUTTON, CASINO_BUTTON),
        (SIDE_JOB_BUTTON, INFO_BUTTON))
HOME = ((FARM_BUTTON, BALANCE_BUTTON),
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
     "NAME": "🇷🇺White Russian", "MINING": 3463, "PRICE": 18000}
XL = {"SIZE": "XL", "PATH": "materials/XL.jpg", "DESC": "Grow-room на 50 растений",
      "NAME": "🖤Black Water", "MINING": 13020, "PRICE": 65000}
XXL = {"SIZE": "XXL", "PATH": "materials/XXL.jpg", "DESC": "Grow-room на 100 растений",
       "NAME": "🦍Original Gorilla Glue 4 S1", "MINING": 31250, "PRICE": 190000}

SIZES = [XS, S, M, L, XL, XXL]

# SQL

DB_PATH = "data/data.db"

REG_USERS = "INSERT OR IGNORE INTO users VALUES (?, ?, ?)"
REG_FARM = "INSERT OR IGNORE INTO farm VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
REG_BALANCE = "INSERT OR IGNORE INTO balance VALUES (?, ?, ?)"

GET_BALANCE = "SELECT money, high FROM balance WHERE id=?"
GET_FROM_TABLE = "SELECT {field} FROM {table} WHERE id=?"
GET_FARM = "SELECT XS, S, M, L, XL, XXL, last_collect FROM farm WHERE id=?"

BUYING_GROW_BOX = "UPDATE farm SET {name} = {name} + 1 WHERE id=?"
PAYING_MONEY = "UPDATE balance SET money = money - {price} WHERE id=?"

WAIT_GET_USERS = "SELECT id FROM users"
WAIT_ADD = "INSERT INTO wait VALUES (?)"
WAIT_IS_ADD = "SELECT * FROM wait WHERE id=?"

# Start Properties

START_XS_GROW_BOX = 1
START_GROW_BOX = 0
START_MONEY = 110
START_HIGH = 0

# Balance

BALANCE = "*" + BALANCE_BUTTON + "*\n\nНаличные: *{money}*💰\nШишек на складе: *{high}*🌳"

# Farm

LAST_COLLECT = 6
FARM = "*" + FARM_BUTTON + "*\n\nЗдесь установлены купленные вами гровбоксы." \
       " Они производят 🌳, которые вам необходимо собирать и продав" \
       "ать. Ниже вы можете посмотреть, " \
       "сколько 🌳 выросло в Ваших гровб" \
       "оксах с момента последнего сбора, и собрать их" \
       " для продажи.\n" \
       "\n🔹 *" + XS["NAME"] + \
       "*\nКол-во: *{XS}*" \
       "\nСозрело: *{XS_high}*🌳\n" \
       "\n🔹 *" + S["NAME"] + \
       "*\nКол-во: *{S}*" \
       "\nСозрело: *{S_high}*🌳\n"\
       "\n🔹 *" + M["NAME"] + \
       "*\nКол-во: *{M}*" \
       "\nСозрело: *{M_high}*🌳\n"\
       "\n🔹 *" + L["NAME"] + \
       "*\nКол-во: *{L}*" \
       "\nСозрело: *{L_high}*🌳\n"\
       "\n🔹 *" + XL["NAME"] + \
       "*\nКол-во: *{XL}*" \
       "\nСозрело: *{XL_high}*🌳\n"\
       "\n🔹 *" + XXL["NAME"] + \
       "*\nКол-во: *{XXL}*" \
       "\nСозрело: *{XXL_high}*🌳\n" \
       "\nВсего: *{all_high}*🌳" \
       "\nДата последнего сбора: *{date} UTC*"

# Wait

WAIT_TEXT = "Игра ещё на стадии 🛠 разработки.\n" \
            "Не удаляйте этот чат. Когда всё " \
            "будет готово, мы обязательно сообщим."
