from datetime import datetime, timedelta

# Bot

TOKEN_PATH = "materials/token.txt"
TOKEN = open(file=TOKEN_PATH, mode='r').read()

# Menu and Menu Buttons:

LEFT = 0
RIGHT = 1

# HighGrowing Market

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

# Start Properties

START_GROW_BOX = 0
START_MONEY = 202
START_HIGH = 0
START_CHIP = 0
START_HARVEST_SUM = 0

# Farm

REDUCTION_FACTOR = 0.9
LAST_COLLECT = -1
RIPENING = {"MINUTE": 23}

# Patterns

PATTERN_HARVEST = 'harvest'
PATTERN_NICK = '[A-Za-z0-9]'

# Dealer (∀i: BID_i+1["HIGH"] > BID_i["HIGH"])

BID_1 = {"HIGH": 100, "PAY": 1}
BID_2 = {"HIGH": 270, "PAY": 3}
BID_3 = {"HIGH": 800, "PAY": 10}
BID_4 = {"HIGH": 2100, "PAY": 30}
BID_5 = {"HIGH": 6000, "PAY": 100}
BIDS = [BID_1, BID_2, BID_3, BID_4, BID_5]

HIGH_MIN = 1
MAX_CONST = 10
HIGH_MAX = MAX_CONST * BID_5["HIGH"]
MONEY_MAX = MAX_CONST * BID_5["PAY"]

# Casino

CASINO_PIC_PATH = "materials/Casino.jpg"
CHIPS_FOR_CURRENCY_UNIT = 100
COMMISSION = 20


# Twenty One

SUITS = ("♠", "♣", "♥", "♦")
DIGNITIES = ("6", "7", "8", "9", "10", "J", "Q", "K", "A")
POINTS = (6, 7, 8, 9, 10, 2, 3, 4, 11)
CARD_DECK = [f"{DIGNITY}{SUIT}" for DIGNITY in DIGNITIES for SUIT in SUITS]
CARDS_POINTS = {DIGNITY + SUIT: POINT for DIGNITY, POINT in zip(DIGNITIES, POINTS) for SUIT in SUITS}

MORE_PATTERN = "more"
YOURSELF_PATTERN = "yourself"
BLIND_PATTERN = "blind"
FINISH_PATTERN = "finish"
EMPTY_PATTERN = "empty"

MAIN_RULES_PATTERN = "main_rules"
FOR_WIN_PATTERN = "for_win"
BLIND_RULES_PATTERN = "mode_blind_rules"
POINTS_PATTERN = "points"
ALL_OK_PATTERN = "all_is_ok"

MIN_CHIPS_FOR_TWENTY_ONE = 1

# Street

OUTSKIRTS = {"PROB": [70, 30], "PRICE": 30, "ESCAPE": [9, 91]}
OUTSKIRTS_PAY = {"PROB": [90, 10], "PRICE": 50, "ESCAPE": [3, 25]}
CENTRE = {"PROB": [40, 60], "PRICE": 60, "ESCAPE": [29, 91]}
CENTRE_PAY = {"PROB": [80, 20], "PRICE": 100, "ESCAPE": [5, 27]}
PLACES = (OUTSKIRTS, CENTRE)
PLACES_PAY = (OUTSKIRTS_PAY, CENTRE_PAY)

FIRST_EVENT = ["sell", "detention"]
SECOND_EVENT = ["escape", "retention"]
EVENTS = (FIRST_EVENT, SECOND_EVENT)
MIN_MONEY_FOR_STREET = 25
MIN_HIGH_FOR_STREET = 500

# Letter

LETTER_MAX_LEN = 500

# Side job

PRICE_FOR_REFERRAL = 99

# Lottery

LOTTERY_TIME = datetime.strptime("05:30", "%H:%M")
MOSCOW_LOTTERY_TIME = (LOTTERY_TIME + timedelta(hours=3)).strftime('%H:%M')
LOTTERY_BREAK = 2

BABYLON = {"PRICE": 110}
BOB_MARLEY = {"PRICE": 1200}
ZION = {"PRICE": 15000}
JAH = {"PRICE": 1000000}
TICKETS = [BABYLON, BOB_MARLEY, ZION, JAH]
