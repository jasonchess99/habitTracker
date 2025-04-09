#reading environment Variables
from dotenv import load_dotenv

#allow for OS operations to be ran by this script
import os


#Telegram bot dependencies
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

#loading .env file and instantiating the bot token within this script (hard code bypass)
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()



print(TOKEN)