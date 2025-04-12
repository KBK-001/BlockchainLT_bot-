import os
import telebot

bot_token = os.getenv("BOT_TOKEN")
if not bot_token:
    raise Exception("Bot token is not defined")

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Sveikas! Čia tavo BlockchainLT naujienų botas.")

bot.polling()
