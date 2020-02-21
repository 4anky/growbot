from copy import deepcopy
from random import shuffle

from telegram import ParseMode, TelegramError

import config
import menu_bot as menu
import sql
import states as state
import text


def stub_enter_bet(update, _):
    update.message.reply_markdown(text=text.TO_ENTER_BET)
    return state.TWENTY_ONE_ENTER_BET


def stub():
    return state.TWENTY_ONE


def calc_points(deck, number):
    return (sum(config.CARDS_POINTS[card] for card in deck[0:number]),
            max(config.CARDS_POINTS[card] for card in deck[0:number]),
            min(config.CARDS_POINTS[card] for card in deck[0:number]))


def job_first_cards_message(context):
    chat_id, game_n, bet, banker, you, bottom_card, entry_message_id = context.job.context
    context.bot.delete_message(chat_id=chat_id, message_id=entry_message_id)
    (keyboard, patterns) = \
        (text.INLINE_BLIND, text.BLIND_PATTERNS) if you['points'] == 6 else (text.INLINE_MAIN, text.MAIN_PATTERNS)
    context.bot.send_message(
        chat_id=chat_id,
        text=text.FIRST_CARD_MESSAGE.format(n=text.three_digits(n=game_n),
                                            bet=text.three_digits(n=bet),
                                            b_cards=banker['deck'][0],
                                            b_points=banker['points'],
                                            you_cards=you['deck'][0],
                                            you_points=you['points'],
                                            bottom=bottom_card),
        reply_markup=menu.inline_show(menu=keyboard, patterns=patterns),
        parse_mode=ParseMode.MARKDOWN)


def job_opening_banker_cards(context):
    telegram_id, game_message_id, banker_situations = context.job.context
    (situation, game_message) = banker_situations.pop(0)
    context.bot.edit_message_text(chat_id=telegram_id,
                                  message_id=game_message_id,
                                  text=game_message,
                                  reply_markup=None,
                                  parse_mode=ParseMode.MARKDOWN)
    if not len(banker_situations):
        context.job.schedule_removal()


def job_blind(context):
    telegram_id, game_message_id, blind_situations = context.job.context
    (situation, game_message) = blind_situations.pop(0)
    context.bot.edit_message_text(chat_id=telegram_id,
                                  message_id=game_message_id,
                                  text=game_message,
                                  reply_markup=None,
                                  parse_mode=ParseMode.MARKDOWN)
    if not len(blind_situations):
        context.job.schedule_removal()


def job_back_to_twenty_one_menu(context):
    context.bot.send_message(chat_id=context.job.context,
                             text=text.TWENTY_ONE_DESC,
                             reply_markup=menu.show(menu=text.TWENTY_ONE),
                             parse_mode=ParseMode.MARKDOWN)


def start_of_game():
    banker, you = {}, {}
    card_deck = deepcopy(config.CARD_DECK)
    shuffle(card_deck)
    bottom_card, banker["deck"], you["deck"] = card_deck[-1], card_deck[0:9], card_deck[9:18]
    banker["number_open_cards"], you["number_open_cards"] = 1, 1
    (banker["points"], _, _) = calc_points(deck=banker["deck"], number=banker["number_open_cards"])
    (you["points"], _, _) = calc_points(deck=you["deck"], number=you["number_open_cards"])
    return banker, you, bottom_card


def entry(update, context):
    if not sql.get_from_table(telegram_id=update.message.chat.id, table="balance", field="chip"):
        update.message.reply_markdown(text=text.INSUFFICIENT_CHIPS)
        return state.TWENTY_ONE
    context.user_data["data"] = sql.get_twenty_one_data(telegram_id=update.message.chat.id)
    context.user_data["data"][1] += 1
    context.user_data["BANKER"], context.user_data["YOU"], context.user_data["BOTTOM_CARD"] = start_of_game()
    banker, you, bottom_card = context.user_data["BANKER"], context.user_data["YOU"], context.user_data["BOTTOM_CARD"]
    update.message.reply_markdown(
        text=(text.ENTRY_MESSAGE.format(b_cards=banker['deck'][0],
                                        b_points=banker['points'],
                                        you_cards=you['deck'][0],
                                        you_points=you['points'],
                                        bottom=bottom_card,
                                        balance=text.three_digits(n=context.user_data['data'][12]))
              + text.TO_ENTER_BET),
        reply_markup=menu.no_menu())
    context.user_data["entry_message_id"] = update.message.message_id + 1
    return state.TWENTY_ONE_ENTER_BET


def do_continuation(context):
    data = context.user_data
    data['data'][2] = data['data'][2]


def do_five_pictures(context):
    data = context.user_data
    data['data'][2] += 1
    data['data'][4] = max(data['BET'], data['data'][4])
    data['data'][6] += data['BET']
    data['data'][8] += 1
    data['prize'] = data['BET']


def do_twenty_one(context):
    data = context.user_data
    data['data'][2] += 1
    data['data'][4] = max(data['BET'], data['data'][4])
    data['data'][6] += data['BET']
    data['prize'] = data['BET']


def do_nature_21(context):
    data = context.user_data
    data['data'][2] += 1
    data['data'][4] = max(data['BET'], data['data'][4])
    data['data'][6] += data['BET']
    data['data'][7] += 1
    data['prize'] = data['BET']


def do_777(context):
    data = context.user_data
    data['data'][2] += 1
    data['data'][4] = max(2 * data['BET'], data['data'][4])
    data['data'][6] += 2 * data['BET']
    data['data'][9] += 1
    data['prize'] = 2 * data['BET']


def do_678(context):
    data = context.user_data
    data['data'][2] += 1
    data['data'][4] = max(2 * data['BET'], data['data'][4])
    data['data'][6] += 2 * data['BET']
    data['data'][11] += 1
    data['prize'] = 2 * data['BET']


def do_golden(context):
    data = context.user_data
    data['data'][2] += 1
    data['data'][4] = max(data['BET'], data['data'][4])
    data['data'][6] += data['BET']
    data['data'][10] += 1
    data['prize'] = data['BET']


def do_exceeded(context):
    data = context.user_data
    data['data'][3] += 1
    data['data'][5] = max(data['BET'], data['data'][5])
    data['data'][6] -= data['BET']
    data['prize'] = -data['BET']


def more_situations(context):
    data = context.user_data
    banker, you = data['BANKER'], data['YOU']

    you['number_open_cards'] += 1
    you_number = you['number_open_cards']
    you['points'], max_point, min_point = calc_points(deck=you['deck'], number=you_number)

    game_message = text.GAME_MESSAGE.format(n=text.three_digits(n=data['data'][1]),
                                            bet=text.three_digits(n=data['BET']),
                                            b_cards=banker['deck'][0],
                                            b_points=banker['points'],
                                            you_cards=' '.join(you['deck'][0:you_number]),
                                            you_points=you['points'],
                                            bottom=data['BOTTOM_CARD'])

    return {"continuation": {"condition": you['points'] < 21 and (
                                               you_number == 5 and max_point > 4 or you_number != 5),
                             "do": do_continuation,
                             "game_message": game_message,
                             "reply_markup": menu.inline_show(menu=text.INLINE_MAIN,
                                                              patterns=text.MAIN_PATTERNS)},
            "exceeded": {"condition": (you['points'] > 22 or you['points'] == 22 and you_number > 2),
                         "do": do_exceeded,
                         "game_message": game_message + f"\n*Результат:* ☠Проигрыш _(Перебор)_",
                         "reply_markup": None},
            "twenty_one": {"condition": (you['points'] == 21 and not you_number == 2 and not min_point == 7
                                         and not (min_point == 6 and max_point == 8)),
                           "do": do_twenty_one,
                           "game_message": game_message + f"\n*Результат:* 🎉Выигрыш _(21 очко)_",
                           "reply_markup": None},
            "five_pictures": {"condition": you_number == 5 and max_point <= 4,
                              "do": do_five_pictures,
                              "game_message": game_message + f"\n*Результат:* 🎉Выигрыш _(5 картинок)_",
                              "reply_markup": None},
            "nature_21": {"condition": you['points'] == 21 and you_number == 2,
                          "do": do_nature_21,
                          "game_message": game_message + f"\n*Результат:* 🎉Выигрыш _(Натуральное 21)_",
                          "reply_markup": None},
            "777": {"condition": you['points'] == 21 and min_point == 7,
                    "do": do_777,
                    "game_message": game_message + f"\n*Результат:* 🎉🎉Выигрыш _(777) Двойной выигрыш!_",
                    "reply_markup": None},
            "678": {"condition": you['points'] == 21 and min_point == 6 and max_point == 8,
                    "do": do_678,
                    "game_message": game_message + f"\n*Результат:* 🎉🎉Выигрыш _(678) Двойной выигрыш!_",
                    "reply_markup": None},
            "golden": {"condition": you['points'] == 22 and you_number == 2,
                       "do": do_golden,
                       "game_message": game_message + f"\n*Результат:* 🎉Выигрыш _(Золотое 21)_",
                       "reply_markup": None}}


def more(update, context):
    telegram_id = update.callback_query.message.chat.id
    for situation in more_situations(context).values():
        if situation["condition"]:
            context.bot.edit_message_text(chat_id=telegram_id,
                                          message_id=update.callback_query.message.message_id,
                                          text=situation["game_message"],
                                          reply_markup=situation["reply_markup"],
                                          parse_mode=ParseMode.MARKDOWN)
            situation["do"](context)
            if situation["reply_markup"] is None:
                sql.update_twenty_one_data(data=context.user_data["data"][:-1], prize=context.user_data["prize"])
                context.job_queue.run_once(callback=job_back_to_twenty_one_menu, when=2, context=telegram_id)
                context.user_data["in_game_flag"] = False
            break


def b_continuation(context):
    data = context.user_data
    data['data'][2] = data['data'][2]


def b_five_pictures(context):
    data = context.user_data
    data['data'][3] += 1
    data['data'][5] = max(data['BET'], data['data'][5])
    data['data'][6] -= data['BET']
    data['prize'] = -data['BET']


def b_win(context):
    data = context.user_data
    data['data'][3] += 1
    data['data'][5] = max(data['BET'], data['data'][5])
    data['data'][6] -= data['BET']
    data['prize'] = -data['BET']


def b_lose(context):
    data = context.user_data
    data['data'][2] += 1
    data['data'][4] = max(data['BET'], data['data'][4])
    data['data'][6] += data['BET']
    data['prize'] = data['BET']


def b_exactly_win(context):
    data = context.user_data
    data['data'][3] += 1
    data['data'][5] = max(data['BET'], data['data'][5])
    data['data'][6] -= data['BET']
    data['prize'] = -data['BET']


def b_golden(context):
    data = context.user_data
    data['data'][3] += 1
    data['data'][5] = max(data['BET'], data['data'][5])
    data['data'][6] -= data['BET']
    data['prize'] = -data['BET']


def b_exactly_lose(context):
    data = context.user_data
    data['data'][2] += 1
    data['data'][4] = max(data['BET'], data['data'][4])
    data['data'][6] += data['BET']
    data['prize'] = data['BET']


def what_is_the_situation(data):
    b_points, b_max_point, b_min_point, b_number, you_points = data
    situations = {"b_continuation": {"condition": b_points <= 16 and (
             b_number == 5 and b_max_point > 4 or b_number != 5),
                                     "end_of_message_game": None,
                                     "do": b_continuation},
                  "b_five_pictures": {"condition": b_number == 5 and b_max_point <= 4,
                                      "end_of_message_game": "\n*Результат:* ☠Проигрыш _(5 картинок у Банкира)_",
                                      "do": b_five_pictures},
                  "b_win": {"condition": 17 <= b_points <= 20 and (
                          b_number != 5 or b_number == 5 and b_max_point > 4) and b_points >= you_points,
                            "end_of_message_game": "\n*Результат:* ☠Проигрыш _(по очкам)_",
                            "do": b_win},
                  "b_lose": {"condition": 17 <= b_points <= 20 and (
                          b_number != 5 or b_number == 5 and b_max_point > 4) and b_points < you_points,
                             "end_of_message_game": "\n*Результат:* 🎉Выигрыш _(по очкам)_",
                             "do": b_lose},
                  "b_exactly_win": {"condition": b_points == 21,
                                    "end_of_message_game": "\n*Результат:* ☠Проигрыш _(21 у Банкира)_",
                                    "do": b_exactly_win},
                  "b_golden": {"condition": b_points == 22 and b_number == 2,
                               "end_of_message_game": "\n*Результат:* ☠Проигрыш _(Золотое 21 у Банкира)_",
                               "do": b_golden},
                  "b_exactly_lose": {"condition": b_points == 22 and b_number > 2 or b_points > 22,
                                     "end_of_message_game": "\n*Результат:* 🎉Выигрыш _(Перебор у Банкира)_",
                                     "do": b_exactly_lose}}
    for situation, data in situations.items():
        if data["condition"]:
            return situation, data["end_of_message_game"], data["do"]


def yourself(update, context):
    user = context.user_data
    data, bet, banker, you, bottom_card = user['data'], user['BET'], user['BANKER'], user['YOU'], user['BOTTOM_CARD']
    telegram_id, game_message_id = update.callback_query.message.chat.id, update.callback_query.message.message_id
    banker_situations, game_message = [], None
    for ((b_points, b_max_point, b_min_point), b_number) in \
            [(calc_points(deck=banker['deck'], number=number), number) for number in range(1, len(banker['deck']) + 1)]:
        game_message = text.GAME_MESSAGE.format(n=text.three_digits(n=data[1]),
                                                bet=text.three_digits(n=bet),
                                                b_cards=' '.join(banker['deck'][0:b_number]),
                                                b_points=b_points,
                                                you_cards=' '.join(you['deck'][0:you['number_open_cards']]),
                                                you_points=you['points'],
                                                bottom=bottom_card)
        if b_points <= 16 and (b_number == 5 and b_max_point > 4 or b_number != 5):
            banker_situations.append(("b_continuation", game_message))
        else:
            situation, end, do_function = what_is_the_situation(
                data=(b_points, b_max_point, b_min_point, b_number, user['YOU']['points']))
            banker_situations.append((situation, game_message + end))
            do_function(context)
            sql.update_twenty_one_data(data=data[:-1], prize=user["prize"])
            break
    repeat = 1.5
    context.job_queue.run_repeating(callback=job_opening_banker_cards,
                                    first=0,
                                    interval=repeat,
                                    context=(telegram_id, game_message_id, banker_situations))
    context.job_queue.run_once(callback=job_back_to_twenty_one_menu,
                               when=repeat * len(banker_situations) + 1.5,
                               context=telegram_id)
    context.user_data["in_game_flag"] = False


def what_is_the_blind_situation(you_points, b_points, b_max, b_number):
    for situation, data in \
            {"blind_b_golden": {"condition": b_points == 22 and b_number == 2,
                                "do": b_golden,
                                "end_message": "\n*Результат:* ☠Проигрыш _(Золотое 21 у Банкира)_"},
             "blind_b_21_or_five_pictures": {"condition": b_points == 21 or (b_number == 5 and b_max <= 4),
                                             "do": b_exactly_win if b_points == 21 else b_five_pictures,
                                             "end_message": ("\n*Результат:* ☠Проигрыш _(21 очко у Банкира)_"
                                                             if b_points == 21 else
                                                             "\n*Результат:* ☠Проигрыш _(5 картинок у Банкира)_")},
             "blind_golden": {"condition": b_points < 21 and not (b_number == 5 and b_max <= 4) and you_points == 22,
                              "do": do_golden,
                              "end_message": "\n*Результат:* 🎉Выигрыш _(Золотое 21)_"},
             "blind_nature_21": {"condition": b_points < 21 and not (b_number == 5 and b_max <= 4) and you_points == 21,
                                 "do": do_nature_21,
                                 "end_message": "\n*Результат:* 🎉Выигрыш _(Натуральное 21)_"},
             "blind_win": {
                 "condition": not (b_number == 5 and b_max <= 4) and 21 > you_points > b_points,
                 "do": b_lose,
                 "end_message": "\n*Результат:* 🎉Выигрыш _(по очкам)_"},
             "blind_lose": {
                 "condition": not (b_number == 5 and b_max <= 4) and 21 > b_points >= you_points,
                 "do": b_win,
                 "end_message": "\n*Результат:* ☠Проигрыш _(по очкам)_"},
             "blind_b_exceeded": {"condition": b_points > 22 or b_points == 22 and b_number > 2,
                                  "do": b_exactly_lose,
                                  "end_message": "\n*Результат:* 🎉Выигрыш _(Перебор у Банкира)_"}}.items():
        if data["condition"]:
            return situation, data["do"], data["end_message"]


def blind(update, context):
    # Вступление
    telegram_id, game_message_id = update.callback_query.message.chat.id, update.callback_query.message.message_id
    user = context.user_data
    data, bet, banker, you, bottom_card = user['data'], user['BET'], user['BANKER'], user['YOU'], user['BOTTOM_CARD']
    blind_situations, game_message, banker_max_point, banker_min_point = [], None, None, None

    # Игрок вытащил вторую карту вслепую
    you['number_open_cards'] += 1
    you['points'], _, _ = calc_points(deck=you['deck'], number=you['number_open_cards'])
    you['points'] += 5
    blind_card, blind_points = " ❓", "11+"

    # Банкир вытаскивает карты по одной, всю инфу для каждого шага сохраняем в список (как в yourself())
    for ((b_points, b_max_point, b_min_point), b_number) in \
            [(calc_points(deck=banker['deck'], number=number), number) for number in range(1, len(banker['deck']) + 1)]:
        game_message = text.BLIND_GAME_MESSAGE.format(n=text.three_digits(n=data[1]),
                                                      mode=text.BLIND_BUTTON,
                                                      bet=text.three_digits(n=bet),
                                                      b_cards=' '.join(banker['deck'][0:b_number]),
                                                      b_points=b_points,
                                                      you_cards=you['deck'][0] + blind_card,
                                                      you_points=blind_points,
                                                      bottom=bottom_card)
        if b_points <= 16 and (b_number == 5 and b_max_point > 4 or b_number != 5):
            blind_situations.append(("b_continuation", game_message))
        else:
            situation, end, do_function = what_is_the_situation(
                data=(b_points, b_max_point, b_min_point, b_number, user['YOU']['points']))
            blind_situations.append((situation, game_message))
            banker['points'], banker_max_point, banker_min_point = b_points, b_max_point, b_min_point
            break

    # Раскрываем вторую карту игрока, рассчитываем результат игры и заносим это в тот же список
    game_message = text.BLIND_GAME_MESSAGE.format(n=text.three_digits(n=data[1]),
                                                  mode=text.BLIND_BUTTON,
                                                  bet=text.three_digits(n=bet),
                                                  b_cards=' '.join(banker['deck'][:len(blind_situations)]),
                                                  b_points=banker['points'],
                                                  you_cards=' '.join(you['deck'][:2]),
                                                  you_points=you['points'],
                                                  bottom=bottom_card)
    end_situation, blind_function, end_message = what_is_the_blind_situation(you_points=you['points'],
                                                                             b_points=banker['points'],
                                                                             b_max=banker_max_point,
                                                                             b_number=len(blind_situations))

    blind_function(context)
    blind_situations.append((end_situation, game_message + end_message))
    sql.update_twenty_one_data(data=data[:-1], prize=user["prize"])
    repeat = 1.5
    context.job_queue.run_repeating(callback=job_blind,
                                    first=0,
                                    interval=repeat,
                                    context=(telegram_id, game_message_id, blind_situations))
    context.job_queue.run_once(callback=job_back_to_twenty_one_menu,
                               when=repeat * len(blind_situations) + 1.5,
                               context=telegram_id)
    context.user_data["in_game_flag"] = False


def finish(update, context):
    telegram_id, game_message_id = update.callback_query.message.chat.id, update.callback_query.message.message_id
    user = context.user_data
    data, bet, banker, you, bottom_card = user['data'], user['BET'], user['BANKER'], user['YOU'], user['BOTTOM_CARD']
    you['points'], _, _ = calc_points(deck=you['deck'], number=you['number_open_cards'])
    banker['points'], _, _ = calc_points(deck=banker['deck'], number=banker['number_open_cards'])

    game_message = text.GAME_MESSAGE.format(n=text.three_digits(n=data[1]),
                                            bet=text.three_digits(n=bet),
                                            b_cards=' '.join(banker['deck'][:banker['number_open_cards']]),
                                            b_points=banker['points'],
                                            you_cards=' '.join(you['deck'][:you['number_open_cards']]),
                                            you_points=you['points'],
                                            bottom=bottom_card)
    do_exceeded(context)
    sql.update_twenty_one_data(data=context.user_data["data"], prize=context.user_data["prize"])
    context.bot.edit_message_text(chat_id=telegram_id,
                                  message_id=game_message_id,
                                  text=game_message + "\n*Результат:* ☠Проигрыш _(выход из Игры)_",
                                  reply_markup=None,
                                  parse_mode=ParseMode.MARKDOWN)
    context.job_queue.run_once(callback=job_back_to_twenty_one_menu, when=1.5, context=telegram_id)
    context.user_data["in_game_flag"] = False


def game(update, context):
    if context.user_data["in_game_flag"]:
        return state.TWENTY_ONE
    try:
        chips_bet = int(update.message.text)
    except ValueError:
        update.message.reply_markdown(
            text=text.ENTER_ERROR_MESSAGE.format(min=text.three_digits(n=config.MIN_CHIPS_FOR_TWENTY_ONE)))
        return state.TWENTY_ONE_ENTER_BET
    else:
        if chips_bet <= 0:
            update.message.reply_markdown(
                text=text.ENTER_ERROR_MESSAGE.format(min=text.three_digits(n=config.MIN_CHIPS_FOR_TWENTY_ONE)))
            return state.TWENTY_ONE_ENTER_BET
        chips_in_balance = sql.chips_in_balance(telegram_id=update.message.chat.id)
        if chips_bet > chips_in_balance:
            update.message.reply_markdown(text=text.FEW_CHIPS_FOR_BET)
            return state.TWENTY_ONE_ENTER_BET
        else:
            context.user_data["in_game_flag"] = True
            context.user_data["BET"] = chips_bet
            update.message.reply_markdown(text=text.BET_IS_ACCEPTED)
            try:
                context.job_queue.run_once(
                    callback=job_first_cards_message,
                    when=2,
                    context=(update.message.chat.id,
                             context.user_data["data"][1],
                             context.user_data["BET"],
                             context.user_data['BANKER'],
                             context.user_data['YOU'],
                             context.user_data["BOTTOM_CARD"],
                             context.user_data['entry_message_id']))
            except TelegramError as mysterious_error:
                for developer in sql.get_dev_id():
                    context.bot.send_message(chat_id=developer,
                                             text=mysterious_error)
            return state.TWENTY_ONE


def main_rules(update, context):
    context.user_data['rules_message_id'] = update.callback_query.message.message_id
    context.user_data['telegram_id'] = update.callback_query.message.chat.id
    context.bot.edit_message_text(chat_id=context.user_data['telegram_id'],
                                  message_id=context.user_data['rules_message_id'],
                                  text=text.MAIN_RULES_TEXT,
                                  reply_markup=menu.inline_show(menu=text.INLINE_RULES, patterns=text.RULES_PATTERNS),
                                  parse_mode=ParseMode.MARKDOWN)


def game_progress_rules(update, context):
    context.user_data['rules_message_id'] = update.callback_query.message.message_id
    context.user_data['telegram_id'] = update.callback_query.message.chat.id
    context.bot.edit_message_text(chat_id=context.user_data['telegram_id'],
                                  message_id=context.user_data['rules_message_id'],
                                  text=text.GAME_PROGRESS_TEXT,
                                  reply_markup=menu.inline_show(menu=text.INLINE_RULES, patterns=text.RULES_PATTERNS),
                                  parse_mode=ParseMode.MARKDOWN)


def blind_rules(update, context):
    context.user_data['rules_message_id'] = update.callback_query.message.message_id
    context.user_data['telegram_id'] = update.callback_query.message.chat.id
    context.bot.edit_message_text(chat_id=context.user_data['telegram_id'],
                                  message_id=context.user_data['rules_message_id'],
                                  text=text.BLIND_RULES_TEXT,
                                  reply_markup=menu.inline_show(menu=text.INLINE_RULES, patterns=text.RULES_PATTERNS),
                                  parse_mode=ParseMode.MARKDOWN)


def points_rules(update, context):
    context.user_data['rules_message_id'] = update.callback_query.message.message_id
    context.user_data['telegram_id'] = update.callback_query.message.chat.id
    context.bot.edit_message_text(chat_id=context.user_data['telegram_id'],
                                  message_id=context.user_data['rules_message_id'],
                                  text=text.POINTS_RULES_TEXT,
                                  reply_markup=menu.inline_show(menu=text.INLINE_RULES, patterns=text.RULES_PATTERNS),
                                  parse_mode=ParseMode.MARKDOWN)


def all_is_ok(update, context):
    context.user_data['rules_message_id'] = update.callback_query.message.message_id
    context.user_data['telegram_id'] = update.callback_query.message.chat.id
    context.bot.delete_message(chat_id=context.user_data['telegram_id'],
                               message_id=context.user_data['rules_message_id'])


def rules(update, context):
    if context.user_data["in_game_flag"]:
        return state.TWENTY_ONE
    context.bot.send_message(
        chat_id=update.message.chat.id,
        text=text.RULES_START_MESSAGE,
        reply_markup=menu.inline_show(menu=text.INLINE_RULES, patterns=text.RULES_PATTERNS),
        parse_mode=ParseMode.MARKDOWN)
    return state.TWENTY_ONE


def rating(update, context):
    if context.user_data["in_game_flag"]:
        return state.TWENTY_ONE
    update.message.reply_markdown(text=text.RATING_DESC, reply_markup=menu.show(menu=text.TWENTY_ONE_RATING))
    return state.TWENTY_ONE_RATING


def word_ending(n):
    if (n % 10 == 1) and (n != 11):
        return "игра"
    elif (n % 10 in range(2, 5)) and (n not in range(12, 15)):
        return "игры"
    else:
        return "игр"


def games_number_rating(update, _):
    nick, number = range(2)
    games_number_message = text.GAMES_NUMBER_HEADING
    for serial_number, user in enumerate(sql.twenty_one_rating(key="games_number")):
        games_number_message += text.GAMES_NUMBER_LINE.format(sn=serial_number + 1,
                                                              nick=user[nick],
                                                              number=text.three_digits(n=user[number]),
                                                              end=word_ending(n=user[number]))
    update.message.reply_markdown(text=games_number_message)
    return state.TWENTY_ONE_RATING


def win_percent_rating(update, _):
    nick, percent = range(2)
    rating_text = text.WIN_PERCENT_HEADING
    for serial_number, user in enumerate(sql.twenty_one_rating(key="win_percent")):
        rating_text += text.WIN_PERCENT_LINE.format(sn=serial_number + 1, nick=user[nick], percent=user[percent])
    update.message.reply_markdown(text=rating_text)
    return state.TWENTY_ONE_RATING


def max_win_rating(update, _):
    nick, max_win = range(2)
    rating_text = text.MAX_WIN_HEADING
    for serial_number, user in enumerate(sql.twenty_one_rating(key="max_win")):
        rating_text += text.MAX_WIN_LINE.format(sn=serial_number + 1,
                                                nick=user[nick],
                                                max_win=text.three_digits(n=user[max_win]))
    update.message.reply_markdown(text=rating_text)
    return state.TWENTY_ONE_RATING


def max_lose_rating(update, _):
    nick, max_lose = range(2)
    rating_text = text.MAX_LOSE_HEADING
    for serial_number, user in enumerate(sql.twenty_one_rating(key="max_lose")):
        rating_text += text.MAX_LOSE_LINE.format(sn=serial_number + 1,
                                                 nick=user[nick],
                                                 max_lose=text.three_digits(n=user[max_lose]))
    update.message.reply_markdown(text=rating_text)
    return state.TWENTY_ONE_RATING


def my_stats(update, context):
    if context.user_data["in_game_flag"]:
        return state.TWENTY_ONE
    stats = sql.twenty_one_stats(telegram_id=update.message.chat.id)
    win_percent = round(100 * stats[3] / stats[2], 3) if stats[2] else 0
    update.message.reply_markdown(text=text.MY_STATS_TEXT.format(nick=stats[0],
                                                                 balance=text.three_digits(n=stats[13]),
                                                                 games=text.three_digits(n=stats[2]),
                                                                 win=text.three_digits(n=stats[3]),
                                                                 nature_21=text.three_digits(n=stats[8]),
                                                                 golden_21=text.three_digits(n=stats[11]),
                                                                 five_pictures=text.three_digits(n=stats[9]),
                                                                 three_sevens=text.three_digits(n=stats[10]),
                                                                 six_seven_eight=text.three_digits(n=stats[12]),
                                                                 win_percent=win_percent if stats[2] >= 20 else '-',
                                                                 lose=text.three_digits(n=stats[4]),
                                                                 total_win=text.three_digits(n=stats[7]),
                                                                 max_win=text.three_digits(n=stats[5]),
                                                                 max_lose=text.three_digits(n=stats[6])))
    return state.TWENTY_ONE
