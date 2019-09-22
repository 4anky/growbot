from telegram.ext.filters import BaseFilter

import menu_bot as menu


class Home(BaseFilter):

    def __init__(self):
        self.names = menu.main[0][0]

    def filter(self, message):
        return bool(message.text == self.names)


class Markets(BaseFilter):

    def __init__(self):
        self.names = menu.main[0][1]

    def filter(self, message):
        return bool(message.text == self.names)


class SellGoods(BaseFilter):

    def __init__(self):
        self.names = menu.main[1][0]

    def filter(self, message):
        return bool(message.text == self.names)


class Casino(BaseFilter):

    def __init__(self):
        self.names = menu.main[1][1]

    def filter(self, message):
        return bool(message.text == self.names)


class SideJob(BaseFilter):

    def __init__(self):
        self.names = menu.main[2][0]

    def filter(self, message):
        return bool(message.text == self.names)


class Info(BaseFilter):

    def __init__(self):
        self.names = menu.main[2][1]

    def filter(self, message):
        return bool(message.text == self.names)


class Farm(BaseFilter):

    def __init__(self):
        self.names = menu.home[0][0]

    def filter(self, message):
        return bool(message.text == self.names)


class Stock(BaseFilter):

    def __init__(self):
        self.names = menu.home[0][1]

    def filter(self, message):
        return bool(message.text == self.names)


class Rating(BaseFilter):

    def __init__(self):
        self.names = menu.home[1][0]

    def filter(self, message):
        return bool(message.text == self.names)


class HighGrowing(BaseFilter):

    def __init__(self):
        self.names = menu.markets[0][0]

    def filter(self, message):
        return bool(message.text == self.names)


class Agent(BaseFilter):

    def __init__(self):
        self.names = menu.sell_goods[0][0]

    def filter(self, message):
        return bool(message.text == self.names)


class Street(BaseFilter):

    def __init__(self):
        self.names = menu.sell_goods[0][1]

    def filter(self, message):
        return bool(message.text == self.names)


class Bones(BaseFilter):

    def __init__(self):
        self.names = menu.casino[0][0]

    def filter(self, message):
        return bool(message.text == self.names)


class Invite(BaseFilter):

    def __init__(self):
        self.names = menu.side_job[0][0]

    def filter(self, message):
        return bool(message.text == self.names)


class FAQ(BaseFilter):

    def __init__(self):
        self.names = menu.info[0][0]

    def filter(self, message):
        return bool(message.text == self.names)


class Community(BaseFilter):

    def __init__(self):
        self.names = menu.info[0][1]

    def filter(self, message):
        return bool(message.text == self.names)


class Letter(BaseFilter):

    def __init__(self):
        self.names = menu.info[1][0]

    def filter(self, message):
        return bool(message.text == self.names)


class Version(BaseFilter):

    def __init__(self):
        self.names = menu.info[1][1]

    def filter(self, message):
        return bool(message.text == self.names)


class Back(BaseFilter):

    def __init__(self):
        self.names = menu.back_button

    def filter(self, message):
        return bool(message.text == self.names)
