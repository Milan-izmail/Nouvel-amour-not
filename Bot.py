from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = 7605141182:AAEzJpHBi1yxWmWOS7DSgDlmhpnfq4Hpf2A

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привіт! Це бот "Nouvel Amour". Що б ви хотіли дізнатися або зробити?')

def main():
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
