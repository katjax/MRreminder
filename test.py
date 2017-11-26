import telebot
token = "480231200:AAHPR1rENTGbwrnsIlmBy13DguB1Ki1sGjc"
bot = telebot.TeleBot(token)
# bot.send_message(79801945,"привет")
# upd = bot.get_updates()
# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)

#@bot.message_handler(commands=['start', 'help'])
#def send_welcome(message):
#	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['help'])
def handle_welcome(message):
	    bot.send_message(message.chat.id, "Описание")

@bot.message_handler(content_types=['text'])
def handle_welcome(message):
    if message.text =="a":
	    bot.send_message(message.chat.id, "b")
    elif message.text == "b":
        bot.send_message(message.chat.id, "a")
    else:
        bot.send_message(message.chat.id, "ты не умеешь играть в эту игру")
bot.polling(none_stop=True, interval=0)