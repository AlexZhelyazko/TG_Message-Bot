from telegram import Update
from telegram.ext import filters, CommandHandler, MessageHandler, CallbackContext, Application
import logging
from telegram import Bot


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

try:
    chat = bot.get_chat(chat_id)
    print(f"Chat found: {chat}")
except Exception as e:
    print(f"Error: {e}")
BOT_TOKEN = 'TOKEN'
CHAT_IDS = [ "CHAT IDS"]

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! Send me a message, and I will forward it to the specified chats.')

async def broadcast(update: Update, context: CallbackContext) -> None:
    user_message = update.message
    for chat_id in CHAT_IDS:
        await context.bot.send_message(chat_id=chat_id, text=user_message.text)
    await update.message.reply_text('Message sent!')

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, broadcast))

    application.run_polling()

if __name__ == '__main__':
    main()
