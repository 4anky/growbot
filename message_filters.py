from telegram.ext.filters import BaseFilter


class Market(BaseFilter):

    def __init__(self):
        self.names = "📦Магазин"

    def filter(self, message):
        return bool(message.text == self.names)


class Sell(BaseFilter):

    def __init__(self):
        self.names = "🌳Продать шишки"

    def filter(self, message):
        return bool(message.text == self.names)


class Bones(BaseFilter):

    def __init__(self):
        self.names = "🎲Кости"

    def filter(self, message):
        return bool(message.text == self.names)


class Info(BaseFilter):

    def __init__(self):
        self.names = "📢Информация"

    def filter(self, message):
        return bool(message.text == self.names)
