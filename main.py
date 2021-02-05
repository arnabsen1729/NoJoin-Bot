from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import re
import os

updater = Updater(os.environ.get('BOT_API_KEY'))
dp = updater.dispatcher

def about(update, context):
  update.message.reply_text("Hello there, Dwai bhaiya said I can't have any ego. I just do what my maker asked me to. Bye !")

def test(update, context):
  message = update.message
  if message['new_chat_members']:
    dp.bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id)

def main():
  dp.add_handler(CommandHandler('about', about))
  dp.add_handler(MessageHandler(Filters.all, test))
  updater.start_polling()
  print('Bot started...')
  updater.idle()

if __name__ == "__main__":
  main()
