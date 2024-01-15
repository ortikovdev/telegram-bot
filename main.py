import telebot

API_TOKEN = '5993744682:AAGVfdBsXaLS4ZrtWLnn1JfJCgXN2yE1osI'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hello')


bot.polling(none_stop=True)