from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackContext

BOT_TOKEN = 'BOT TOKEN'
CHAT_IDS = [' ']

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Send me a message, and I will forward it to the specified chats.')

def broadcast(update: Update, context: CallbackContext) -> None:
    user_message = update.message
    for chat_id in CHAT_IDS:
        context.bot.send_message(chat_id=chat_id, text=user_message.text)
    update.message.reply_text('Message sent!')

def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, broadcast))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
