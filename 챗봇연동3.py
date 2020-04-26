import sys
import 연동챗봇임2

def proc_rolling(bot, update):
    mooodtest.sendMessage('안녕하세요~')
    sound = firecracker()
    mooodtest.sendMessage(sound)
    mooodtest.sendMessage('반가워요~~')

def proc_stop(bot, update):
    mooodtest.sendMessage('봇이 꺼집니다.')
    mooodtest.stop()

def firecracker():
    return '야호!'

mooodtest = 연동챗봇임2.BotChii()
mooodtest.add_handler('hi', proc_rolling)
mooodtest.add_handler('stop', proc_stop)
mooodtest.start()