from telegram.ext.filters import BaseFilter


class MessageFilter(BaseFilter):

    def __init__(self, button):
        self.button = button

    def filter(self, message):
        return bool(message.text in self.button)
