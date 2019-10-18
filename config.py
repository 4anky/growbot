# Bot

TOKEN_PATH = "materials/token.txt"
TOKEN = open(file=TOKEN_PATH, mode='r').read()
VERSION_NUMBER = "v0.1.8."
VERSION = ("🌳*Weed Grow*🌳\n_{n}_\n\n"
           + "• Снижены цены в 🐲HighGrowing.").format(n=VERSION_NUMBER)

# Train

TRAIN_DESC_1_TEXT = ("*⚠Главное⚠*\n\nВ этой игре Вы развиваете своё дело по выращиванию и продаже 🌳 шишек - "
                     + "здоровых и полезных соцветий лучшего растения мира. Созревшие 🌳 можно продавать через"
                     + " 👳🏻‍♂ *Дилера* или самостоятельно на 🌃*Улице*, зарабатывая при этом некислые 💰 бабки.\n\n"
                     + "Но не всё так просто. Вы можете просадить весь капитал в 🎰 *Casino*, при продаже Вас может "
                     + "поймать *полицейский 🚔 патруль*. В самом худшем случае к Вам домой с обыском может заявиться"
                     + " *майор 👮🏽‍♂ Крепилов*, тогда придётся действовать быстро и без раздумий.\n\nВ общем, нет "
                     + "времени объяснять! Жми на 🐲 и покупай свою первую установку для выращивания!")
TRAIN_DESC_2_TEXT = ("*🤙Успешно*\n\nПоздравляю, Вы приобрели свой первый Grow-box. Вы уже в деле! У Вас дома "
                     + "оборудована *🌱Ферма*, там можете отслеживать количество созревших 🌳 шишек и собирать "
                     + "урожай для продажи.")
TRAIN_NICK_TEXT = ("*📝 Название компании*\n\nВаша 🏭*Компания* пока никак не называется. Вы можете придумать для "
                   + "нее абсолютно любое название, состоящее из латинских букв и цифр.\n\n📌 Список требований к "
                   + "названию:\n1. Латинский алфавит: *A-Z, a-z;*\n2. Цифры: *0-9*;\n3. Длина названия: от *5* до "
                   + "*19* символов включительно.\n\n❗*Запрещено в названии располагать 📺 рекламу и использовать "
                   + "нецензурные 🤬 слова*❗")
TRAIN_NICK_VALID_TEXT = "✅Всё *ОК*. Приятной игры!✅"
TRAIN_NICK_ERROR_TEXT = ("🚫*Вы ввели некорректное имя*🚫\n\nНазвание компании должно состоять из латинских букв или"
                         + " цифр длиной от 5 до 19 символов. Повторите попытку:")
TRAIN_NICK_NOT_VALID_TEXT = "🔺*Введённое имя занято*🔺\n\nПожалуйста, введите другое имя:"

# dev

PLAYERS_NUMBER_TEXT = "_В игре зарегистрировано {n} игроков_"

# Menu and Menu buttons

MENU_DESC = "*Главное Меню*"
MENU_RELOAD = "Версия Игры обновилась.\nВы в *Главном Меню*"
BACK_TO_MENU_DESC = "*Главное Меню*"
ERROR_MESSAGE = "Возвращаемся в *Главное Меню*"

LEFT = 0
RIGHT = 1

BACK_BUTTON = "◀Назад"
EMPTY_BUTTON = ""

HOME_BUTTON = "🏡Дом"
MARKETS_BUTTON = "🏬Магазины"
SELL_GOODS_BUTTON = "💰Продать товар"
CASINO_BUTTON = "🎰Casino"
SIDE_JOB_BUTTON = "💶Подработка"
INFO_BUTTON = "📣Информация"

FARM_BUTTON = "🌱Ферма"
BALANCE_BUTTON = "💵Баланс"
RATING_BUTTON = "🏆Рейтинг"

RATING_MONEY_BUTTON = "🏅Богачи💰"
RATING_HARVEST_BUTTON = "🏅Добытчики🌳"

HIGH_GROWING_BUTTON = "🐲HighGrowing"

DEALER_BUTTON = "👳🏻‍♂Дилер"
STREET_BUTTON = "🌃Улица"
CENTRE_BUTTON = "🏛Центр"
OUTSKIRTS_BUTTON = "🏚Окраина"
BRIBE_BUTTON = "😑Договориться"
ESCAPE_BUTTON = "🏃🏿‍♂Сбежать"

BLACKJACK_BUTTON = "♥Blackjack♠"
DICE_BUTTON = "🎲Dice"
EXCHANGE_BUTTON = "🔄Касса"

TO_CHIP_BUTTON = "Обменять 💰"
TO_MONEY_BUTTON = "Обменять 🔴"

INVITE_BUTTON = "👥Пригласи друзей"
PAYMENT_BUTTON = "💲Получить оплату"

FAQ_BUTTON = "❓FAQ"
COMMUNITY_BUTTON = "💬Сообщество"
LETTER_BUTTON = "✉Письмо авторам"
VERSION_BUTTON = "✅Версия игры"

HARVEST_INLINE = "🌳Собрать урожай"

TRAIN_DESC_1_BUTTON = "🐲"
TRAIN_MARKET_BUTTON = "💵Купить"
TRAIN_DESC_2_BUTTON = "Далее▶️"

MAIN = ((HOME_BUTTON, MARKETS_BUTTON),
        (SELL_GOODS_BUTTON, CASINO_BUTTON),
        (SIDE_JOB_BUTTON, INFO_BUTTON))
HOME = ((FARM_BUTTON, BALANCE_BUTTON),
        (RATING_BUTTON, BACK_BUTTON))
RATING = ((RATING_MONEY_BUTTON, RATING_HARVEST_BUTTON),
          (BACK_BUTTON, EMPTY_BUTTON))
MARKETS = ((HIGH_GROWING_BUTTON, BACK_BUTTON),)
SELL_GOODS = ((DEALER_BUTTON, STREET_BUTTON),
              (BACK_BUTTON, EMPTY_BUTTON))
STREET_PLACES = ((OUTSKIRTS_BUTTON, CENTRE_BUTTON),
                 (BACK_BUTTON, EMPTY_BUTTON))
DETENTION = ((BRIBE_BUTTON, ESCAPE_BUTTON),)
RETENTION = ((BRIBE_BUTTON, EMPTY_BUTTON),)
CASINO = ((BLACKJACK_BUTTON, DICE_BUTTON),
          (EXCHANGE_BUTTON, BACK_BUTTON))
EXCHANGE = ((TO_CHIP_BUTTON, TO_MONEY_BUTTON),
            (BACK_BUTTON, EMPTY_BUTTON))
SIDE_JOB = ((INVITE_BUTTON, BACK_BUTTON),)
PAYMENT = ((PAYMENT_BUTTON, BACK_BUTTON),)
INFO = ((FAQ_BUTTON, COMMUNITY_BUTTON),
        (LETTER_BUTTON, VERSION_BUTTON),
        (BACK_BUTTON, EMPTY_BUTTON))
BACK = ((BACK_BUTTON, EMPTY_BUTTON),)

TRAIN_DESC_1 = ((TRAIN_DESC_1_BUTTON, EMPTY_BUTTON),)
TRAIN_MARKET = ((TRAIN_MARKET_BUTTON, EMPTY_BUTTON),)
TRAIN_DESC_2 = ((TRAIN_DESC_2_BUTTON, EMPTY_BUTTON),)

# Home

HOME_DESC = ("*{home}* родной. Здесь Вы можете контролировать свои дела: проверить *{balance}*, "
             + "собрать урожай на 🌱*Ферме* и оценить шансы попадания "
             + "в *{rating}* игроков").format(home=HOME_BUTTON, balance=BALANCE_BUTTON, rating=RATING_BUTTON)

# Markets

MARKETS_DESC = ("Сегодня работает лишь один магазин: *{market}*. В нём Вы можете приобрести *Grow box*"
                + " любого размера для выращивания душистых 🌳.").format(market=HIGH_GROWING_BUTTON)

# HighGrowing Market

BUY_BUTTON = "Купить"

HIGH_GROWING_CAPTION = "🔹 *{about}*\nСорт: *{name}*\nДобывает: *{mining}* 🌳 в час\nЦена: *{price}* 💰"
HIGH_GROWING_PURCHASE = ("👍 *Успешно!*\n\n*{desc}* установлена и посажена, теперь вам нужно лишь заходить на 🌱 "
                         + "*Ферму* и собирать созревшие 🌳 шишки. Вы можете установить сколько угодно гровбоксов!")
PURCHASE_ERROR = "⛔*Недостаточно средств!*⛔"
XS = {"SIZE": "XS", "PATH": "materials/XS.jpg", "DESC": "Grow-box на 2 растения",
      "NAME": "Belladonna", "MINING": 16, "PRICE": 101}
S = {"SIZE": "S", "PATH": "materials/S.jpg", "DESC": "Grow-box на 4 растения",
     "NAME": "Skunk+", "MINING": 80, "PRICE": 400}
M = {"SIZE": "M", "PATH": "materials/M.jpg", "DESC": "Grow-box на 8 растений",
     "NAME": "Sour Diesel", "MINING": 360, "PRICE": 1600}
L = {"SIZE": "L", "PATH": "materials/L.jpg", "DESC": "Grow-box на 24 растения",
     "NAME": "🇷🇺White Russian", "MINING": 1980, "PRICE": 8000}
XL = {"SIZE": "XL", "PATH": "materials/XL.jpg", "DESC": "Grow-room на 50 растений",
      "NAME": "🖤Black Water", "MINING": 12870, "PRICE": 48000}
XXL = {"SIZE": "XXL", "PATH": "materials/XXL.jpg", "DESC": "Grow-room на 100 растений",
       "NAME": "🦍Original Gorilla Glue 4 S1", "MINING": 109400, "PRICE": 380000}

SIZES = [XS, S, M, L, XL, XXL]

# SQL

DB_PATH = "data/data.db"

REG_USERS = "INSERT OR IGNORE INTO users VALUES (?, ?)"
REG_BALANCE = "INSERT OR IGNORE INTO balance VALUES (?, ?, ?, ?, ?)"
REG_FARM = "INSERT OR IGNORE INTO farm VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
REG_FARM_AMENDMENTS = "INSERT OR IGNORE INTO farm_amendments VALUES (?, ?, ?, ?, ?, ?, ?)"
ADD_REFERRAL = "INSERT OR IGNORE INTO ref_system VALUES (?, ?, ?)"

GET_BALANCE = "SELECT money, high, chip FROM balance WHERE id = ?"
GET_FROM_TABLE = "SELECT {field} FROM {table} WHERE id = ?"
GET_FARM = "SELECT XS, S, M, L, XL, XXL, last_collect FROM farm WHERE id = ?"
GET_FARM_AMENDMENTS = "SELECT XS, S, M, L, XL, XXL FROM farm_amendments WHERE id = ?"
GET_RATING = ("SELECT users.nick, balance.{param} FROM users JOIN balance ON users.id = balance.id "
              + "ORDER BY {param} DESC LIMIT 10")
IS_REG = "SELECT * FROM users WHERE id = ?"
GET_DEV_ID = "SELECT * FROM dev"
GET_PLAYERS_NUMBER = "SELECT COUNT(id) FROM users"
GET_COMPLETED_REFERRALS = ("SELECT referral, nick FROM ref_system JOIN balance ON ref_system.referral = balance.id "
                           + "JOIN users ON ref_system.referral = users.id WHERE ref_system.referrer = ? AND "
                           + "ref_system.task = 0 AND balance.harvest_sum > 0")

UPDATE_NICK = "UPDATE users SET nick = ? WHERE id = ?"
TO_ZERO_FARM_AMENDMENTS = "UPDATE farm_amendments SET XS = 0, S = 0, M = 0, L = 0, XL = 0, XXL = 0 WHERE id = ?"
UPDATE_FARM_AMENDMENTS = "UPDATE farm_amendments SET {size} = {size} + {value} WHERE id = ?"
BUYING_GROW_BOX = "UPDATE farm SET {name} = {name} + 1 WHERE id = ?"
PAYING_MONEY = "UPDATE balance SET money = money - {price} WHERE id = ?"
HIGH_TO_BALANCE = "UPDATE balance SET high = high + {high}, harvest_sum = harvest_sum + {high} WHERE id = ?"
HIGH_TO_BALANCE_CLEAR_FARM = "UPDATE farm SET last_collect = ? WHERE id = ?"
HIGH_TO_MONEY = "UPDATE balance SET high = high - ?, money = money + ? WHERE id = ?"
ESCAPE = "UPDATE balance SET money = money - ? WHERE id = ?"
BRIBE = "UPDATE balance SET money = money - ?, high = high - ? WHERE id = ?"
UPDATE_REF_SYSTEM = "UPDATE ref_system SET task = 1 WHERE referral = ?"
REFERRAL_TO_MONEY = "UPDATE balance SET money = money + ? WHERE id = ?"

# Start Properties

START_GROW_BOX = 0
START_MONEY = 202
START_HIGH = 0
START_CHIP = 0
START_HARVEST_SUM = 0

# Balance

BALANCE = (BALANCE_BUTTON.join("**")
           + "\n\nНаличные: *{money}*💰\nШишек на складе: *{high}*🌳\nФишек в Casino: *{chip}*🔴️")
HIGH_ON_STOCK = "Шишек на складе: *{high}*🌳"
MONEY_ON_STOCK = "Наличные: *{money}*💰"

# Farm

LAST_COLLECT = 6
RIPENING = {"MINUTE": 23}
FARM_DESC_START = ("\n\nЗдесь установлены купленные вами *Grow-box*. В них созревают 🌳, которые Вам необходимо "
                   + "собирать и продавать. Ниже вы можете посмотреть сколько 🌳 выросло в Ваших *Grow-box* с "
                   + "момента последнего сбора, и собрать их для продажи.\n\n")
FARM_STATS = "🔹 *{name}*\nКол-во: *{number}*\nСозрело: *{mature}*🌳\n"
FARM_DESC_END = "\nВсего: *{all}*🌳"
FARM_HARVEST = ("👍 *Шишки собраны!*\n\nВы собрали: *{number}*🌳\n\n"
                + "Собранный урожай вы можете продать за 💰 своему 👳🏻‍♂Агенту")

HARVEST_ERROR = "❗*Урожай ещё не созрел*❗"

# Patterns

PATTERN_HARVEST = r'[+]?\d+'
PATTERN_NICK = '[A-Za-z0-9]'

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
DEALER_DESC = ("👳🏻‍♂*Дилер* готов купить Ваш товар. Вот его условия:\n\n{bids}\n\n{high}\n\nВведите количество 🌳, "
               + "которое хотите продать. Учтите, что *Дилер не заплатит* Вам более *{money_max}*💰 за раз и *не "
               + "вернёт* остатки шишек.").format(bids=BIDS_TEXT, high=HIGH_ON_STOCK, money_max=MONEY_MAX)
HIGH_EXCHANGE = "👍 *Успешно!*\n\nПродано: *{high}*🌳\nПолучено: *{money}*💰"
BAD_HIGH_EXCHANGE = "👎 *Неудача!*\n\n👳🏻‍♂*Дилер* оставил Вас с носом👃\n\nПродано: *{high}*🌳\nПолучено: *{money}*💰"
NOT_POSITIVE_NUMBER = "Ожидается *целое число больше 0*. Введите его:"
NOT_ENOUGH_HIGH = "У Вас есть только *{high}*🌳. Введите число не более *{high}*:"

# Casino

CASINO_PIC_PATH = "materials/Casino.jpg"
COMMISSION = 2
EXCHANGE_DESC = ("Здесь Вы можете произвести *обмен* между 🔴 и 💰.\n\n*Курс обмена:* *1*💰 = *100*🔴\n\n*Комиссия* за "
                 + "перевод: *{chip}*🔴").format(chip=COMMISSION)
CASINO_DESC = CASINO_BUTTON.join("**") + " скоро откроется!\nЖдите 🕑, мы обязательно сообщим!"
DICE_DESC = CASINO_DESC

# Rating

RATING_DESC = RATING_BUTTON.join("**") + "\n\nЗдесь Вы можете увидеть Рейтинг игроков.\nВыберите категорию:"
RATING_MONEY_TEXT = "🥇🥈🥉\n*Рейтинг* игроков с самой *жирной котлетой* на кармане:\n\n"
RATING_MONEY_LINE = "👑 *{name}*: {number}💰"
RATING_HARVEST_SUM_TEXT = "🥇🥈🥉\n*Рейтинг* игроков с самой крупной *суммарной 🌳 добычей* за всю историю:\n\n"
RATING_HARVEST_SUM_LINE = "👑 *{name}*: {number}🌳"

# Sell goods

SELL_GOODS_DESC = ("*⚖Продажа*\n\nВы можете продать 🌳 двумя способами: через 👳🏻‍♂*Дилера-поср"
                   + "едника* и самостоятельно на 🌃*Улице*. Работа с *Дилером* имеет минимальные риски"
                   + ", но на *Улице* вы можете заработать гораздо больше💰!")

# Street

INSUFFICIENT_FUNDS = "📛*Недостаточно средств для торговли на Улице*📛"
OUTSKIRTS = {"NAME": OUTSKIRTS_BUTTON, "PROB": [70, 30], "PRICE": 30, "ESCAPE": [9, 91]}
CENTRE = {"NAME": CENTRE_BUTTON, "PROB": [40, 60], "PRICE": 60, "ESCAPE": [29, 91]}
PLACES = (OUTSKIRTS, CENTRE)
FIRST_EVENT = ["sell", "detention"]
SECOND_EVENT = ["escape", "retention"]
EVENTS = (FIRST_EVENT, SECOND_EVENT)
MIN_MONEY_FOR_STREET = 25
MIN_HIGH_FOR_STREET = 500
STREET_ENTER_HIGH_TEXT = ("На *Улицу* можно выходить, имея как *минимум {min_high}*🌳 и *{min_money}*💰.\n\n"
                          + "{money}\n{high}\n\nВведите количество 🌳,"
                          + " которое задумали продать подороже:").format(
    min_high=MIN_HIGH_FOR_STREET, min_money=MIN_MONEY_FOR_STREET, money=MONEY_ON_STOCK, high=HIGH_ON_STOCK
)
STREET_CHOICE_PLACE = (STREET_BUTTON.join("**")
                       + "\n\nПопытайте удачу и продайте готовый 🌳 урожай на улицах города. Будьте начеку: можно "
                       + "нарваться на *полицейский 🚔 патруль*.\n\nВыберите место для сбыта:\n"
                       + OUTSKIRTS_BUTTON.join("**")
                       + "   *30*💰 за *1000*🌳   шанс погореть *30%*\n"
                       + CENTRE_BUTTON.join("**")
                       + "         *60*💰 за *1000*🌳   шанс погореть *60%*\n\n"
                       + "_Совет:_  Если Вас словит *Патруль* - попробуйте от него 💸 откупиться.")
STREET_NOT_EXPECTED_NUMBER = ("Ожидается *целое число не менее {min_high}*. "
                              + "Введите его:").format(min_high=MIN_HIGH_FOR_STREET)
STREET_START_TEXT = "*Вы вышли на Улицу*\n\nНа руках у Вас *{high}*🌳, самое время их продать😈"
STREET_SELL_TEXT = "*👍Успех*\n\nЗаработано: *{money}*💰\nПродано:  *{sold}*🌳\nОсталось с продажи: *{unsold}*🌳"
STREET_DETENTION_TEXT = ("*🚨Стоять, полиция!🚨*\n\nВас принял *полицейский 🚔 патруль*. Договоритесь с ним "
                         + "или сбежите, не оставив им шанса?\n\n*Договориться: {high}*🌳 и *{money}*💰\n"
                         + "*Сбежать:*  *{money}*💰, шанс поимки *{chance}%*")
STREET_ESCAPE_TEXT = "Отлично, 🚔 *Патруль* Вас не догнал. Вы 🕺 свободны."
STREET_BRIBE_TEXT = "🚔 *Патруль* озолотился и отпустил Вас."
STREET_RETENTION_TEXT = ("*🚨Потрачено〽🚨\n\n* Вас словили, но вы можете договориться с 🚓 полицией.\n\n"
                         + "*Договориться: {high}*🌳 и *{money}*💰")
STREET_DETENTION_NOTIFY = "🚨Вас поймал *полицейский 🚔 патруль*🚨\n\n*Решайте*: 😑договариваться или 🏃🏿‍♂текать"
STREET_RETENTION_NOTIFY = "🚔 *Патруль* словил Вас снова. Нужно 😑 заплатить"

# Info

INFO_DESC = "Вы перешли в меню " + INFO_BUTTON

# Letter

LETTER_DESC = (LETTER_BUTTON.join("**")
               + "\n\nЗдесь Вы можете 📝 описать какую-либо ситуацию в игре, послать общие замечания или пожелания,"
               + " а разработчики 👨‍💻 *WeedGrowBot* это прочтут и примут к сведению.\n\n"
               + "Ваше ✉ сообщение должно содержать *только текст* длиной до *500* символов. Введите его:")
LETTER_MAX_LEN = 500
ERROR_LETTER = ("🚫*Длина сообщения не должна превышать {n} символов*🚫\n\n"
                + "Введите более короткий текст:").format(n=LETTER_MAX_LEN)
LETTER_HEADING = "🔊*Сообщение от игрока {nick}*🔊:\n\n"
LETTER_SEND = "Ваше ✉ *Письмо* успешно отправлено!"

# FAQ

FAQ_DESC = "❗Уже есть какие-то вопросы? Пиши письмо авторам❗"

# Community

COMMUNITY_DESC = ("Чат игроков *WeedGrowBot*: [{link}]\n"
                  + "Здесь обсуждают 🗣 игру и делятся 🤯 впечатлениями!").format(link="t.me/wg_com")

# Side job

PRICE_FOR_REFERRAL = 99
SIDE_JOB_DESC = (SIDE_JOB_BUTTON.join("**")
                 + " - это способы разово выполнить какое-нибудь 📋 задание и получить за него достойную 💰 оплату.")
REFERRAL_LINK = "https://t.me/WeedGrowBot?start={id}"
INVITE_DESC = ("Это Ваша *ссылка* для привлечения в игру других 👥 игроков.\n\nИгроку нужно купить *1 Grow box* и "
               "*1 раз* собрать 🌳 урожай, за это вы заработаете *{price}*💰.\nКогда он это сделает, нажмите "
               + PAYMENT_BUTTON.join("**")).format(price=PRICE_FOR_REFERRAL)
NO_COMPLETED_REFERRALS = "У Вас нет 👥 рефералов, которые выполнили 📋 задание, но за которых Вы не получили 💰 оплату."
SUCCESSFUL_REFERRAL = "🏭*{nick}* выполнил 📋 задание, оплата 💰 получена!"
