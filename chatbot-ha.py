import telegram
import sys
import ChatBotModel_ha

chii_token = '1184525831:AAGXQ9-Es5COmMc8TSjV3Z6EWGHy3efjyUI'
chii = telegram.Bot(token = chii_token)
updates = chii .getUpdates()
for u in updates:
    print(u.message)

def proc_rolling(bot, update):
    chii.sendMessage('안녕')
    chii.sendMessage('만나서 반가워. 나는 챗봇이야')
    chii.sendMessage('무엇을 도와줄까?')

def proc_stop(bot, update):
    chii.sendMessage('치이 봇이 잠듭니다.')
    chii.stop()

chii = ChatBotModel.BotChii()
chii.add_handler('hi', proc_rolling)
chii.add_handler('stop', proc_stop)
chii.start()