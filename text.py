import config


def three_digits(n):
    return "{0:,}".format(n).replace(",", " ")


# Bot

VERSION_NUMBER = "v0.1.17."
VERSION = ("🌳*Weed Grow*🌳\n_{n}_\n\n"
           + "• Исправлена ошибка ввода ставки в игре Двадцать одно").format(n=VERSION_NUMBER)

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
FARM_ARGUMENT_ERROR_TEXT = "Неверное число аргументов.\nПример команды: /farm 123456789"
FARM_INCORRECT_ID_TEXT = "Некорректный id пользователя\nПример команды: /farm 123456789"
FARM_ID_DOES_NOT_EXIST_TEXT = "Игрока с введённым id не существует"
ACCESS_DENIED_TEXT = "_Данная команда доступна только разработчикам_"
USERS_HEADING_TEXT = "Данные всех игроков:\n\n"
USERS_TEXT = "• {id} {nick}\n"

# Menu and Menu buttons

MENU_DESC = "*Главное Меню*"
MENU_RELOAD = "Версия Игры обновилась.\nВы в *Главном Меню*"
BACK_TO_MENU_DESC = "*Главное Меню*"
ERROR_MESSAGE = "Возвращаемся в *Главное Меню*"

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

LOTTERY_BUTTON = "🎱JahLottery"
BABYLON_BUTTON = "🧱Падение Вавилона"
BOB_MARLEY_BUTTON = "🎶Концерт Боба Марли"
ZION_BUTTON = "🏔Возвращение в Зион"
JAH_BUTTON = "🇪🇹Беседа с Джа"
BUY_TICKET_BUTTON = "🎟Купить билет"
TRANSLATION_BUTTON = "🏵Трансляция тиража"

TWENTY_ONE_BUTTON = "♥Двадцать одно♠"
TO_ENTRY_BUTTON = "🚪Войти в игру"
TO_RULES_BUTTON = "📚Правила"
TO_MY_STATS_BUTTON = "📊Моя статистика"
MORE_BUTTON = "🧐Ещё"
YOURSELF_BUTTON = "✋🏻Хватит"
BLIND_BUTTON = "🌚Втёмную"
FINISH_BUTTON = "❌Завершить игру"
MAIN_RULES_BUTTON = "📗Общее"
GAME_PROGRESS_BUTTON = "📕Ход Игры"
BLIND_RULES_BUTTON = "📘Игра Втёмную"
POINTS_BUTTON = "🧮Очки и Комбинации"
ALL_OK_BUTTON = "☀Всё понятно!"
GAMES_NUMBER_BUTTON = "🏅Количество Игр🕹"
WIN_PERCENT_BUTTON = "🏅Процент Побед🧠"
MAX_WIN_BUTTON = "🏅MAX Выигрыш💎"
MAX_LOSE_BUTTON = "🏅MAX Проигрыш🧻"

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
TRAIN_DESC_2_BUTTON = "Далее▶"

MAIN = ((HOME_BUTTON, MARKETS_BUTTON), (SELL_GOODS_BUTTON, CASINO_BUTTON), (SIDE_JOB_BUTTON, INFO_BUTTON))
HOME = ((FARM_BUTTON, BALANCE_BUTTON), (RATING_BUTTON, BACK_BUTTON))
RATING = ((RATING_MONEY_BUTTON, RATING_HARVEST_BUTTON), (BACK_BUTTON, EMPTY_BUTTON))
MARKETS = ((HIGH_GROWING_BUTTON, BACK_BUTTON),)
SELL_GOODS = ((DEALER_BUTTON, STREET_BUTTON), (BACK_BUTTON, EMPTY_BUTTON))
STREET_PLACES = ((OUTSKIRTS_BUTTON, CENTRE_BUTTON), (BACK_BUTTON, EMPTY_BUTTON))
DETENTION = ((BRIBE_BUTTON, ESCAPE_BUTTON),)
RETENTION = ((BRIBE_BUTTON, EMPTY_BUTTON),)
CASINO = ((LOTTERY_BUTTON, TWENTY_ONE_BUTTON), (EXCHANGE_BUTTON, BACK_BUTTON))
LOTTERY = ((BABYLON_BUTTON, BOB_MARLEY_BUTTON), (ZION_BUTTON, JAH_BUTTON), (BACK_BUTTON, EMPTY_BUTTON))
BUY_AND_WATCH = ((BUY_TICKET_BUTTON, TRANSLATION_BUTTON), (BACK_BUTTON, EMPTY_BUTTON))
TWENTY_ONE = ((TO_ENTRY_BUTTON, TO_RULES_BUTTON), (RATING_BUTTON, TO_MY_STATS_BUTTON), (BACK_BUTTON, EMPTY_BUTTON))
TWENTY_ONE_RATING = ((GAMES_NUMBER_BUTTON, WIN_PERCENT_BUTTON),
                     (MAX_WIN_BUTTON, MAX_LOSE_BUTTON),
                     (BACK_BUTTON, EMPTY_BUTTON))
EXCHANGE = ((TO_CHIP_BUTTON, TO_MONEY_BUTTON), (BACK_BUTTON, EMPTY_BUTTON))
SIDE_JOB = ((INVITE_BUTTON, BACK_BUTTON),)
PAYMENT = ((PAYMENT_BUTTON, BACK_BUTTON),)
INFO = ((FAQ_BUTTON, COMMUNITY_BUTTON), (LETTER_BUTTON, VERSION_BUTTON), (BACK_BUTTON, EMPTY_BUTTON))
BACK = ((BACK_BUTTON, EMPTY_BUTTON),)

TRAIN_DESC_1 = ((TRAIN_DESC_1_BUTTON, EMPTY_BUTTON),)
TRAIN_MARKET = ((TRAIN_MARKET_BUTTON, EMPTY_BUTTON),)
TRAIN_DESC_2 = ((TRAIN_DESC_2_BUTTON, EMPTY_BUTTON),)

INLINE_MAIN = ((MORE_BUTTON, YOURSELF_BUTTON),
               (FINISH_BUTTON, EMPTY_BUTTON))
INLINE_BLIND = ((MORE_BUTTON, YOURSELF_BUTTON),
                (BLIND_BUTTON, FINISH_BUTTON))
INLINE_RULES = ((MAIN_RULES_BUTTON, GAME_PROGRESS_BUTTON),
                (BLIND_RULES_BUTTON, POINTS_BUTTON),
                (ALL_OK_BUTTON, EMPTY_BUTTON))
MAIN_PATTERNS = ((config.MORE_PATTERN, config.YOURSELF_PATTERN),
                 (config.FINISH_PATTERN, config.EMPTY_PATTERN))
BLIND_PATTERNS = ((config.MORE_PATTERN, config.YOURSELF_PATTERN),
                  (config.BLIND_PATTERN, config.FINISH_PATTERN))
RULES_PATTERNS = ((config.MAIN_RULES_PATTERN, config.FOR_WIN_PATTERN),
                  (config.BLIND_RULES_PATTERN, config.POINTS_PATTERN),
                  (config.ALL_OK_PATTERN, config.EMPTY_PATTERN))

TICKETS_NAME = (BABYLON_BUTTON, BOB_MARLEY_BUTTON, ZION_BUTTON, JAH_BUTTON)

# Home

HOME_DESC = (f"*{HOME_BUTTON}* родной. Здесь Вы можете контролировать свои дела: проверить *{BALANCE_BUTTON}*, "
             + f"собрать урожай на 🌱*Ферме* и оценить шансы попадания в *{RATING_BUTTON}* игроков")

# Markets

MARKETS_DESC = (f"Сегодня работает лишь один магазин: *{HIGH_GROWING_BUTTON}*. В нём Вы можете приобрести *Grow box*"
                + " любого размера для выращивания душистых 🌳.")

# HighGrowing Market

BUY_BUTTON = "Купить"

HIGH_GROWING_CAPTION = "🔹 *{about}*\nСорт: *{name}*\nДобывает: до *{mining}* 🌳 в час\nЦена: *{price}* 💰"
HIGH_GROWING_PURCHASE = ("👍 *Успешно!*\n\n*{desc}* установлена и посажена, теперь вам нужно лишь заходить на 🌱 "
                         + "*Ферму* и собирать созревшие 🌳 шишки. Вы можете установить сколько угодно гровбоксов!")

# HighGrowing Market

PURCHASE_ERROR = "⛔*Недостаточно средств!*⛔"

# Balance

BALANCE = (f"*{BALANCE_BUTTON}*\n\n" + "Наличные: *{money}*💰\nШишки на складе: *{high}*🌳\nФишки Casino: *{chip}*🔴️")
HIGH_ON_STOCK = "Шишек на складе: *{high}*🌳"
MONEY_ON_STOCK = "Наличные: *{money}*💰"

# Farm

FARM_DESC_START = ("\n\nЗдесь установлены купленные вами *Grow-box*. В них созревают 🌳, которые Вам необходимо "
                   + "собирать и продавать. Ниже вы можете посмотреть сколько 🌳 выросло в Ваших *Grow-box* с "
                   + "момента последнего сбора, и собрать их для продажи.\n\n")
FARM_STATS = "🔹 *{name}*\nКол-во: *{number}*\nСозрело: *{mature}*🌳\n"
FARM_DESC_END = "\nВсего: *{all}*🌳"
FARM_HARVEST = ("👍 *Шишки собраны!*\n\nВы собрали: *{number}*🌳\n\n"
                + "Собранный урожай вы можете продать за 💰 своему 👳🏻‍♂Агенту")

HARVEST_ERROR = "❗*Урожай ещё не созрел*❗"

# Dealer

BIDS_TEXT = "\n".join(
    [f"*{three_digits(n=BID['HIGH'])}*🌳 = *{three_digits(n=BID['PAY'])}*💰" for BID in config.BIDS]
)
DEALER_DESC = (f"👳🏻‍♂*Дилер* готов купить Ваш товар. Вот его условия:\n\n{BIDS_TEXT}\n\n{HIGH_ON_STOCK}\n\n"
               f"Введите количество 🌳, которое хотите продать. Учтите, что *Дилер не заплатит* Вам более *"
               f"{three_digits(n=config.MONEY_MAX)}*💰 за раз и *не вернёт* остатки шишек.")
HIGH_EXCHANGE = "👍 *Успешно!*\n\nПродано: *{high}*🌳\nПолучено: *{money}*💰"
BAD_HIGH_EXCHANGE = "👎 *Неудача!*\n\n👳🏻‍♂*Дилер* оставил Вас с носом👃\n\nПродано: *{high}*🌳\nПолучено: *{money}*💰"
NOT_POSITIVE_NUMBER = "Ожидается *целое число больше 0*. Введите его:"
NOT_ENOUGH_HIGH = "У Вас есть только *{high}*🌳. Введите число не более *{high}*:"

# Casino

EXCHANGE_DESC = (f"Здесь производится *обмен* между 🔴 и 💰.\n\n*Курс* обмена: *1*💰 = "
                 + f"*{config.CHIPS_FOR_CURRENCY_UNIT}*🔴\n*Комиссия* за перевод: *{config.COMMISSION}*🔴")
CASINO_DESC = (f"*{CASINO_BUTTON}* открылось!\n\nУчаствуйте в ежедневной лотерее *{LOTTERY_BUTTON}* и побеждайте!\n"
               f"Обыгрывайте 👨🏻‍💼*Банкира* в {TWENTY_ONE_BUTTON} и покоряйте вершины Рейтингов!\n")
MONEY_TO_CHIP_TEXT = ("*Обмен:* 💰➡🔴\n\nНаличные: *{money}*💰\nФишки Casino: *{chip}*🔴️\n\nВведите количество 💰 "
                      + "для обмена:")
CHIP_TO_MONEY_TEXT = ("*Обмен:* 🔴➡💰\n\nНаличные: *{money}*💰\nФишки Casino: *{chip}*🔴️\n\nВведите количество 🔴 "
                      + "для обмена:\n*Внимание!* Во вводимую сумму закладывайте размер комиссии")
LESS_THAN_COMMISSION = f"Ожидается *целое число больше {config.COMMISSION}*. Введите его:"
NOT_ENOUGH_MONEY = "У Вас есть только *{money}*💰. Введите число не более *{money}*:"
NOT_ENOUGH_CHIP = "У Вас есть только *{chip}*🔴. Введите число не более *{chip}*:"
BUY_CHIPS = "Вы купили *{new}*🔴.\n\nНаличные: *{money}*💰\nФишки Casino: *{chip}*🔴"
SELL_CHIPS = "Вы получили *{new}*💰.\n\nНаличные: *{money}*💰\nФишки Casino: *{chip}*🔴"
LOTTERY_DESC = (f"Добро пожаловать в лотерею *{LOTTERY_BUTTON}*!\n"
                + f"Розыгрыш призов производится *каждый день в {config.MOSCOW_LOTTERY_TIME} по МСК*.\n"
                + f"\nВ наличии имеются 4 лотерейных билета различной стоимости:\n"
                + f" • *{BABYLON_BUTTON}*\n"
                + f" • *{BOB_MARLEY_BUTTON}*\n"
                + f" • *{ZION_BUTTON}*\n"
                + f" • *{JAH_BUTTON}*\n\n"
                + f"Приобритайте билеты и следите за списком участников!")
BUY_AND_WATCH_TEXT = ("Билет: *{name}*.\nСтоимость: *{price}*💰\n\n"
                      + f"Для покупки нажмите *{BUY_TICKET_BUTTON}*.\n"
                      + f"*{TRANSLATION_BUTTON}* доступна после покупки билета.")
AROUND_LOTTERY_TEXT = ("⭕Покупка билетов запрещена в период *двух минут до розыгрыша и после него.*⭕\n"
                       + "Повторите попытку через несколько минут.")
ALREADY_PURCHASED = "❕Вы уже приобрели данный билет на ближайший тираж.❕"
BUYING_TICKET = "♨Вы купили билет *{name}* за *{price}*💰!"
NULL_PLAYERS = ("Билет *{name}* пока никто не приобрёл.\nСтаньте 🥇 первым участником!\n\n"
                + "Дата и время розыгрыша: *{next_time} по МСК*")
PLAYERS_LIST = ("*{name}*\n\n👥Количество участников: *{number}*\n*{players}*\n\n🏦Призовой фонд: *{prize}*💰\n"
                + "📆Дата и время розыгрыша: *{next_time} по МСК*")
LOSERS_MESSAGE = "Победителем лотереи *{name}* стал *{winner}*!\n\nВыигрыш составил *{prize}*💰"
WINNER_MESSAGE = "🎯*Поздравляем!*🎉\nВаш лотерейный билет *{name}* победил в розыгрыше!\n\nВыигрыш: *{prize}*💰"

# Casino - Twenty One

TO_ENTER_BET = "Введите ставку - целое число 🔴 фишек:"
TWENTY_ONE_DESC = "_Hо не очко, обычно, губит, а к одиннадцати — туз..._"
POINTS_RULES_TEXT = ("♥*Очки*♠\n• Карты от *6* до *10* дают очки *по номиналу*;\n• *Валет J* - *2* очка;\n"
                     + "• *Дама Q* - *3* очка;\n• *Король K* - *4* очка;\n• *Туз A* - *всегда 11* очков.\n\n"
                     + "♥*Особые комбинации*♠\n• *Натуральное 21* - это набор из двух карт достоинством 10 и A.\n"
                     + "_Пример:_ *A♣ 10♦*;\n"
                     + "• *Золотое 21* - это набор из двух Тузов. Несмотря на сумму в 22 очка, считается самой сильной"
                     + " выигрышной комбинацией.\n_Пример:_ *A♥ A♣*;\n"
                     + "• *Пять картинок* - это любой набор из пяти карт, имеющий только Валеты, Дамы и Короли. "
                     + "Несмотря на сумму от 11 до 19 очков, засчитывается за 21 очко.\n_Пример:_ *Q♦ J♥ K♣ K♥ J♠*;\n"
                     + "• *777* - это набор из трёх карт достоинством 7. Игрок, собравший данную комбинацию, получает"
                     + " выигрыш в размере двойной ставки.\n_Пример:_ *7♠ 7♥ 7♣*;\n"
                     + "• *678* - это любой набор из трёх карт достоинством 6, 7 и 8. Игрок, собравший данную "
                     + "комбинацию, получает выигрыш в размере двойной ставки.\n_Пример:_ *8♥ 6♠ 7♦*.\n")
MAIN_RULES_TEXT = ("♥*Двадцать одно (Очко)*♠ - карточная игра, в которой используется колода из 36 карт (от *6* до "
                   + "*А*). В данной игре *Вы* играете против 👨🏻‍💼*Банкира*. 🎯*Цель игры* - набрать 🔸очков больше, чем "
                   + "у 👨🏻‍💼Банкира. Если Вы первым набираете *21 очко* - это автоматический 🎉выигрыш. Если Вы первым "
                   + "набираете *больше 21 очка* - это *Перебор*, то есть автоматический 🏳️проигрыш. Также проигрышем "
                   + "считается равенство 🔸очков.\n")
GAME_PROGRESS_TEXT = ("1️⃣ Игра начинается с раздачи одной карты *Вам* и 👨🏻‍💼*Банкиру*. Снизу колоды достаётся *Нижняя"
                      + " карта*. Все *3* карты Вам видны. Справа от карт показаны 🔸*очки*. Вы делаете любую ставку "
                      + "(минимум *1*🔴).\n_Примечание:_ Если Вы не желаете продолжать игру, Вам необходимо ввести "
                      + f"ставку, после чего нажать на кнопку *{FINISH_BUTTON}*.\n\n"
                      + f"2️⃣ После принятия ставки Вам необходимо набрать *21 🔸очко* или максимально близкое к нему."
                      + f" При нажатии на кнопку *{MORE_BUTTON}* Вы получаете новую карту и Ваши очки увеличиваются "
                      + f"соответственно её стоимости (см. *{POINTS_BUTTON}*). Вы можете получить несколько карт, но "
                      + f"будьте осторожны: *Перебор* ведёт к автоматическому 🏳️проигрышу.\n\n"
                      + f"3️⃣ Если имеющихся у Вас карт достаточно, жмите кнопку *{YOURSELF_BUTTON}*. Тогда *Банкир*"
                      + f" начнёт брать карты себе. Вы выиграете игру, если у *Банкира* случится *Перебор* или он "
                      + f"наберёт *меньше 🔸очков*, чем Вы.\n_Примечание:_ *Банкир* обязан брать новую карту пока у "
                      + f"него *меньше 17 очков*.\n\n"
                      + f"4️⃣ В конце игры *Банкир* обновляет Вашу статистику. В случае 🎉*Выигрыша* он выплачивает "
                      + f"сумму, равную величине ставки, а иногда - величине двойной ставки (см. *{POINTS_BUTTON}*). В "
                      + f"случае 🏳️*Проигрыша* - забирает Вашу ставку себе.\n\n*Конец*🔚")
BLIND_RULES_TEXT = (f"Если первой картой выпала *6*, вы имеете право сыграть *{BLIND_BUTTON}*. В этом случае *6* "
                    + f"полностью принимается за Туза. Вы получаете ещё одну карту, но не видите её. *Банкир* набирает"
                    + f" себе карты, после чего вскрывается Ваша _'Тёмная'_ карта. Полученные 🔸*очки* сравниваются.")
ENTRY_MESSAGE = ("*Банкир: {b_cards}    ({b_points}🔸)*\n"
                 + "         *Вы: {you_cards}    ({you_points}🔸)*\n\n"
                 + "*Нижняя карта: {bottom}*\n\n"
                 + "Баланс: *{balance}🔴*\n")
FIRST_CARD_MESSAGE = ("Игра *№{n}*\n"
                      + "Ставка: *{bet}*🔴\n"
                      + "\n"
                      + "*Банкир: {b_cards}    ({b_points}🔸)*\n"
                      + "         *Вы: {you_cards}    ({you_points}🔸)*\n\n"
                      + "*Нижняя карта: {bottom}*")
GAME_MESSAGE = ("Игра *№{n}*\nСтавка: *{bet}*🔴\n\n"
                + "*Банкир: {b_cards}    ({b_points}🔸)*\n"
                + "         *Вы: {you_cards}    ({you_points}🔸)*\n\n"
                + "*Нижняя карта: {bottom}*")
BLIND_GAME_MESSAGE = ("Игра *№{n}  {mode}*\nСтавка: *{bet}*🔴\n\n"
                      + "*Банкир: {b_cards}    ({b_points}🔸)*\n"
                      + "         *Вы: {you_cards}    ({you_points}🔸)*\n\n"
                      + "*Нижняя карта: {bottom}*")
INSUFFICIENT_CHIPS = f"На Вашем счёте нет *🔴Casino-фишек.* Чтобы их получить, загляните в *{EXCHANGE_BUTTON}*"
ENTER_ERROR_MESSAGE = "Ожидается *целое число не менее {min}*🔴.\nВведите его:"
FEW_CHIPS_FOR_BET = "*На балансе недостаточно 🔴 для совершения данной ставки*.\nВведите ставку поменьше:"
BET_IS_ACCEPTED = "Ваша ставка принята!"
RULES_START_MESSAGE = "*Правила игры*. Выберите параграф:"
GAMES_NUMBER_HEADING = "🥇🥈🥉\n*Рейтинг* игроков по *числу сыгранных партий*:\n\n"
WIN_PERCENT_HEADING = "🥇🥈🥉\n*Рейтинг* игроков по *проценту выигранных партий*:\n(рассчитывается от 20 партий)\n\n"
MAX_WIN_HEADING = "🥇🥈🥉\n*Рейтинг* игроков по *максимально выигранным ставкам*:\n\n"
MAX_LOSE_HEADING = "🥇🥈🥉\n*Рейтинг* игроков по *максимально проигранным ставкам*:\n\n"
GAMES_NUMBER_LINE = "*{sn}*🏆   *{nick}*   🕹 _{number} {end}_\n"
WIN_PERCENT_LINE = "*{sn}*🏆   *{nick}*   🧠 _{percent} %_\n"
MAX_WIN_LINE = "*{sn}*🏆   *{nick}*   💎 _{max_win}🔴_\n"
MAX_LOSE_LINE = "*{sn}*🏆   *{nick}*   🧻 _{max_lose}🔴_\n"
MY_STATS_TEXT = (f"*{TWENTY_ONE_BUTTON}*\n\n"
                 + "Игрок:  *{nick}*\n"
                 + "Баланс:  *{balance}🔴*\n\n"
                 + "1️⃣Всего игр:  *{games}*\n"
                 + "2️⃣Побед:  *{win}*\n"
                 + "3️⃣Из них:\n"
                 + "      • _Натуральное 21:_  *{nature_21}*\n"
                 + "      • _Золотое 21:_  *{golden_21}*\n"
                 + "      • _Пять картинок:_  *{five_pictures}*\n"
                 + '      • _"777":_  *{three_sevens}*\n'
                 + '      • _"678":_  *{six_seven_eight}*\n'
                 + "4️⃣Процент побед:  *{win_percent}%*\n"
                 + "5️⃣Поражений:  *{lose}*\n\n"
                 + "6️⃣Суммарный выигрыш:  *{total_win}*🔴\n"
                 + "7️⃣МАХ выигрыш:  *{max_win}🔴*\n"
                 + "8️⃣МАХ проигрыш:  *{max_lose}🔴*")

# Rating

RATING_DESC = f"*{RATING_BUTTON}*\n\nЗдесь Вы можете увидеть Рейтинг игроков.\nВыберите категорию:"
RATING_MONEY_TEXT = "🥇🥈🥉\n*Рейтинг* игроков с самой *жирной котлетой* на кармане:\n\n"
RATING_MONEY_LINE = "👑 *{name}*:  {number}💰"
RATING_HARVEST_SUM_TEXT = "🥇🥈🥉\n*Рейтинг* игроков с самой крупной *суммарной 🌳 добычей* за всю историю:\n\n"
RATING_HARVEST_SUM_LINE = "👑 *{name}*:  {number}🌳"

# Sell goods

SELL_GOODS_DESC = ("*⚖Продажа*\n\nВы можете продать 🌳 двумя способами: через 👳🏻‍♂*Дилера-поср"
                   + "едника* и самостоятельно на 🌃*Улице*. Работа с *Дилером* имеет минимальные риски"
                   + ", но на *Улице* вы можете заработать гораздо больше💰!")

# Street

INSUFFICIENT_FUNDS = "📛*Недостаточно средств для торговли на Улице*📛"

STREET_ENTER_HIGH_TEXT = (f"На *Улицу* можно выходить, имея как *минимум "
                          + f"{three_digits(n=config.MIN_HIGH_FOR_STREET)}*🌳 и *"
                          + f"{three_digits(n=config.MIN_MONEY_FOR_STREET)}*💰.\n\n"
                          + f"{MONEY_ON_STOCK}\n{HIGH_ON_STOCK}\n\nВведите количество 🌳, которое задумали продать:")

STREET_CHOICE_PLACE = (STREET_BUTTON.join("**")
                       + "\n\nПопытайте удачу и продайте готовый 🌳 урожай на улицах города. Будьте начеку: можно "
                       + "нарваться на *полицейский 🚔 патруль*.\n\nВыберите место для сбыта:\n"
                       + OUTSKIRTS_BUTTON.join("**")
                       + f"   *{config.OUTSKIRTS['PRICE']}*💰 за *{three_digits(n=1000)}*🌳   "
                         f"шанс погореть *{config.OUTSKIRTS['PROB'][1]}%*\n"
                       + CENTRE_BUTTON.join("**")
                       + f"         *{config.CENTRE['PRICE']}*💰 за *{three_digits(n=1000)}*🌳   "
                         f"шанс погореть *{config.CENTRE['PROB'][1]}%*\n\n"
                       + "_По блату за отдельную плату:_\n"
                       + " " * 21
                       + f"   *{config.OUTSKIRTS_PAY['PRICE']}*💰 за *{three_digits(n=1000)}*🌳   "
                         f"шанс погореть *{config.OUTSKIRTS_PAY['PROB'][1]}%*\n"
                       + " " * 17
                       + f"     *{config.CENTRE_PAY['PRICE']}*💰 за *{three_digits(n=1000)}*🌳   "
                         f"шанс погореть *{config.CENTRE_PAY['PROB'][1]}%*\n\n"
                       + "_Совет:_  Если Вас словит *Патруль* - попробуйте от него 💸 откупиться.")
STREET_NOT_EXPECTED_NUMBER = (f"Ожидается *целое число не менее {three_digits(n=config.MIN_MONEY_FOR_STREET)}*. "
                              + "Введите его:")
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

# Letter

LETTER_DESC = (LETTER_BUTTON.join("**")
               + "\n\nЗдесь Вы можете 📝 описать какую-либо ситуацию в игре, послать общие замечания или пожелания,"
               + " а разработчики 👨‍💻 *WeedGrowBot* это прочтут и примут к сведению.\n\n"
               + "Ваше ✉ сообщение должно содержать *только текст* длиной до *500* символов. Введите его:")
ERROR_LETTER = (f"🚫*Длина сообщения не должна превышать {config.LETTER_MAX_LEN} символов*🚫\n\n"
                + "Введите более короткий текст:")
LETTER_HEADING = "🔊*Сообщение от игрока {nick}*🔊:\n\n"
LETTER_SEND = "Ваше ✉ *Письмо* успешно отправлено!"

# FAQ

FAQ_DESC = "❗Уже есть какие-то вопросы? Пиши письмо авторам❗"

# Community

COMMUNITY_DESC = ("Чат игроков *WeedGrowBot*: [{link}]\n"
                  + "Здесь обсуждают 🗣 игру и делятся 🤯 впечатлениями!").format(link="t.me/wg_com")

SIDE_JOB_DESC = (SIDE_JOB_BUTTON.join("**")
                 + " - это способы разово выполнить какое-нибудь 📋 задание и получить за него достойную 💰 оплату.")
REFERRAL_LINK = "https://t.me/WeedGrowBot?start={id}"
INVITE_DESC = ("Это Ваша *ссылка* для привлечения в игру других 👥 игроков.\n\nИгроку нужно купить *1 Grow box* и *1 "
               + f"раз* собрать 🌳 урожай, за это вы заработаете *{config.PRICE_FOR_REFERRAL}*💰.\nКогда он это "
               + f"сделает, нажмите *{PAYMENT_BUTTON}*")
NO_COMPLETED_REFERRALS = "У Вас нет 👥 рефералов, которые выполнили 📋 задание, но за которых Вы не получили 💰 оплату."
SUCCESSFUL_REFERRAL = "🏭*{nick}* выполнил 📋 задание, оплата 💰 получена!"

# Info

INFO_DESC = f"Вы перешли в меню {INFO_BUTTON}"
