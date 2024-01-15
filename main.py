import telebot

API_TOKEN = '5993744682:AAGVfdBsXaLS4ZrtWLnn1JfJCgXN2yE1osI'
bot = telebot.TeleBot(API_TOKEN)

user_to_admin_mapping = {}
admin_chat_id = 6018099549

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hello')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def send_message(message, admin_chat_id=6018099549):
    user_chat_id = message.chat.id

    if user_chat_id not in user_to_admin_mapping:
        user_to_admin_mapping[user_chat_id] = admin_chat_id

    admin_chat_id = user_to_admin_mapping[user_chat_id]
    bot.send_message(admin_chat_id, message.text)
    # bot.send_message(user_chat_id)

bot.polling(none_stop=True)