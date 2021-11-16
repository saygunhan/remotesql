import constants as key
from telegram.ext import *
import responses as R
import mysqlcon as my

print("bot started...")

def start_commmand(update,context):
    update.message.reply_text('Type something to get started')


def handle_message(update,context):
    text=str(update.message.text).lower()
    response = my.mysqlcon(text)
    #response2 = sample_responses(input_text)
    update.message.reply_text(response)
    #update.message.reply_text(response2)


def error(update,context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater= Updater(key.API_KEY,use_context=True)
    dp=updater.dispatcher

    dp.add_handler(CommandHandler("start",start_commmand))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(5)
    updater.idle()

main()
