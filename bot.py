from telegram import Update
from telegram.ext import Updater, CommandHandler

def start(update: Update, context):
    update.message.reply_text('Привіт! Це бот компанії "Nouvel Amour". Як я можу вам допомогти?')

def main():
    updater = Updater(6882328095:AAHa8qlP7qnjvrwR98lzDJy2gAIWVdnsL7I, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
