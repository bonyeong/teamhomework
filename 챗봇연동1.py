import telegram

mooodtest_token = '1162111643:AAEPZuDg6Ecxn515KYhLGG8yMHFoHvE76R0'

mooodtest = telegram.Bot(token = mooodtest_token)

updates = mooodtest.getUpdates()

for u in updates:
    print(u.message)
