import telegram
from telegram.ext import Updater, CommandHandler

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 1260470636
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class BotChii(TelegramBot):
    def __init__(self):
        self.token = '1184525831:AAGXQ9-Es5COmMc8TSjV3Z6EWGHy3efjyUI'
        TelegramBot.__init__(self, '치이', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('치이 봇이 잠에서 깨어납니다.')
        self.updater.start_polling()
        self.updater.idle