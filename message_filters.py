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
