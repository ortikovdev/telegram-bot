import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather on Telegram
bot_token = '5993744682:AAGVfdBsXaLS4ZrtWLnn1JfJCgXN2yE1osI'

# Create a bot instance
bot = telebot.TeleBot(bot_token)

# Admin's chat ID (replace with your own)
admin_chat_id = 6018099549  # Replace with your admin chat ID

# Handle the "/start" command
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Welcome to the bot! You can send messages to the admin here.")

# Handle messages from users to admin
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_messages(message):
    bot.send_message(admin_chat_id, f"User {message.chat.id} says: {message.text}")
    bot.send_message(message.chat.id, "Your message has been forwarded to the admin.")

# Handle admin's responses to users
@bot.message_handler(func=lambda message: message.chat.id == admin_chat_id, content_types=['text'])
def handle_admin_responses(message):
    bot.send_message(message.text.split()[0], f"Admin says: {message.text}")

# Polling loop
bot.polling(none_stop=True)
