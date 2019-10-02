# Bot

TOKEN = "TOKEN"

# Menu and Menu buttons

MENU_DESC = "Вы перешли в Главное Меню."
MENU_RELOAD = "Версия Игры обновилась.\nВы в Главном Меню."
BACK_TO_MENU_DESC = "Вы вернулись в Главное Меню."
ERROR_MESSAGE = "Возвращаемся в Главное Меню."

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

DEALER_BUTTON = "👳🏻‍♂️Дилер"
STREET_BUTTON = "🌃Улица"

DICE_BUTTON = "🎲Кости"

INVITE_BUTTON = "🙋🏼‍♂️Пригласи друга"

FAQ_BUTTON = "❓FAQ"
COMMUNITY_BUTTON = "💬Сообщество"
LETTER_BUTTON = "✉️Письмо авторам"
VERSION_BUTTON = "✅Версия игры"

HARVEST_INLINE = "🌳Собрать урожай"

MAIN = ((HOME_BUTTON, MARKETS_BUTTON),
        (SELL_GOODS_BUTTON, CASINO_BUTTON),
        (SIDE_JOB_BUTTON, INFO_BUTTON))
HOME = ((FARM_BUTTON, BALANCE_BUTTON),
        (RATING_BUTTON, BACK_BUTTON))
MARKETS = ((HIGH_GROWING_BUTTON, BACK_BUTTON),)
SELL_GOODS = ((DEALER_BUTTON, STREET_BUTTON),
              (BACK_BUTTON, EMPTY_BUTTON))
CASINO = ((DICE_BUTTON, BACK_BUTTON),)
SIDE_JOB = ((INVITE_BUTTON, BACK_BUTTON),)
INFO = ((FAQ_BUTTON, COMMUNITY_BUTTON),
        (LETTER_BUTTON, VERSION_BUTTON),
        (BACK_BUTTON, EMPTY_BUTTON))
BACK = ((BACK_BUTTON, EMPTY_BUTTON),)

# Home

HOME_DESC = "Вы дома."

# Markets

MARKETS_DESC = "Вы перешли в меню 'Магазин'"

# HighGrowing Market

BUY_BUTTON = "Купить"

HIGH_GROWING_CAPTION = "🔹 *{about}*\n" \
                       "Сорт: *{name}*\n" \
                       "Добывает: *{mining}* 🌳 в час\n" \
                       "Цена: *{price}* 💰"
HIGH_GROWING_PURCHASE = "👍 *Успешно!*\n\n" \
                        "*{desc}* установлена и посажена, " \
                        "теперь вам нужно лишь заходить на ферму " \
                        "и собирать созревшие шишки🌳. " \
                        "Вы можете установить сколько угодно гровбоксов!"
PURCHASE_ERROR = "⛔*Недостаточно средств!*⛔"
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

HIGH_TO_BALANCE = "UPDATE balance SET high = high + {high} WHERE id=?"
HIGH_TO_BALANCE_CLEAR_FARM = "UPDATE farm SET last_collect=? WHERE id=?"

HIGH_TO_MONEY = "UPDATE balance SET high=high-?, money=money+? WHERE id=?"

# Start Properties

START_XS_GROW_BOX = 1
START_GROW_BOX = 0
START_MONEY = 101
START_HIGH = 0

# Balance

BALANCE = "*" + BALANCE_BUTTON + "*\n\nНаличные: *{money}*💰\nШишек на складе: *{high}*🌳"
HIGH_ON_STOCK = "Шишек на складе: *{high}*🌳"

# Farm

LAST_COLLECT = 6
RIPENING = {"MINUTE": 23}
FARM_DESC_START = "\n\nЗдесь установлены купленные вами гровбоксы. " \
                  "В них созревают 🌳, которые вам необходимо " \
                  "собирать и продавать. Ниже вы можете посмотреть" \
                  " сколько 🌳 выросло в Ваших гровбоксах с " \
                  "момента последнего сбора, и собрать их для продажи.\n\n"
FARM_STATS = "🔹 *{name}*\nКол-во: *{number}*\nСозрело: *{mature}*🌳\n"
FARM_DESC_END = "\nВсего: *{all}*🌳\nПоследний сбор: *{date} UTC*"
FARM_HARVEST = "👍 *Шишки собраны!*\n\n" \
               "Вы собрали: *{number}*🌳\n\n" \
               "Собранный урожай вы можете" \
               " продать за 💰 своему 👳🏻‍♂Агенту"

HARVEST_ERROR = "❗*Нового урожая нет*❗"

# Wait

WAIT_TEXT = "Игра ещё на стадии 🛠 разработки.\n" \
            "Не удаляйте этот чат. Когда всё " \
            "будет готово, мы обязательно сообщим."

# Patterns

PATTERN_HARVEST = r'[+]?\d+'

# Dealer (∀i: BID_i+1["HIGH"] > BID_i["HIGH"])

BID_1 = {"HIGH": 150, "PAY": 1}
BID_2 = {"HIGH": 350, "PAY": 3}
BID_3 = {"HIGH": 1000, "PAY": 10}
BID_4 = {"HIGH": 2600, "PAY": 30}
BID_5 = {"HIGH": 7000, "PAY": 100}
BIDS = [BID_1, BID_2, BID_3, BID_4, BID_5]

HIGH_MIN = 1
MAX_CONST = 10
HIGH_MAX = MAX_CONST * BID_5["HIGH"]
MONEY_MAX = MAX_CONST * BID_5["PAY"]

BIDS_TEXT = "\n".join(["*{high}*🌳 = *{pay}*💰".format(high=BID["HIGH"], pay=BID["PAY"]) for BID in BIDS])
DEALER_DESC = "*Дилер* готов купить Ваш товар. " \
              "Вот его условия:\n\n" \
              "{bids}\n\n" \
              "{high}\n\n" \
              "Введите количество 🌳, которое хотите продать. " \
              "Учтите, что дилер не заплатит Вам" \
              " более *{money_max}*💰 за раз и не " \
              "вернёт остатки шишек.".format(bids=BIDS_TEXT, high=HIGH_ON_STOCK, money_max=MONEY_MAX)
HIGH_EXCHANGE = "👍 *Успешно!*\n\nПродано: *{high}*🌳\nПолучено: *{money}*💰"
BAD_HIGH_EXCHANGE = "👎 *Неудача!*\n\nДилер оставил Вас с носом👃\n" \
                    "\nПродано: *{high}*🌳\nПолучено: *{money}*💰"
NOT_POSITIVE_NUMBER = "Ожидается *целое положительное число*. Введите его:"
NOT_ENOUGH_HIGH = "У вас есть только *{high}*🌳. " \
                  "Введите число не более *{high}*:"

# Casino

CASINO_DESC = "Вы перешли в меню 'Казино'"
DICE_DESC = "Вы нажали кнопку 'Кости'"

# Rating

RATING_DESC = "В эту игру ещё никто не играет."

# See goods

SELL_GOODS_DESC = "*⚖️Продажа*\n\nВы можете продать 🌳" \
                  " двумя способами: через 👳🏻‍♂*дилера-поср" \
                  "едника* и самостоятельно на 🌃*Улице*. Ра" \
                  "бота с дилером имеет минимальные риски" \
                  ", но на Улице вы можете заработать гора" \
                  "здо больше💰!"

# Street

STREET_DESC = "Вы нажали кнопку 'Улица'"

# Info

INFO_DESC = "Вы перешли в меню 'Информация'"
FAQ_DESC = "Вы нажали кнопку 'FAQ'"
COMMUNITY_DESC = "Вы нажали кнопку 'Сообщество'"
LETTER_DESC = "Вы нажали кнопку 'Письмо авторам'"
VERSION_DESC = "Вы нажали кнопку 'Версия игры'"

# Side job

SIDE_JOB_DESC = "Вы перешли в меню 'Подработка'"
INVITE_DESC = "Вы нажали кнопку 'Пригласи друга'"
