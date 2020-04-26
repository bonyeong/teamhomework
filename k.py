import telegram

api_token = '1173273675:AAGqVv9pWGhbqe4FKdbj_u8yJp92gAU_em8'
bot = telegram.Bot(token = api_token)
#updates = api .getUpdates()


chat_id = 1132917740

bot.sendMessage(chat_id = chat_id, text='안녕')
