#reading environment Variables
from dotenv import load_dotenv

#allow for OS operations to be ran by this script
import os

#Telegram bot dependencies
import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler


#loading .env file and instantiating the bot token within this script (hard code bypass)
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


#creates logging for when bot crashes
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


#context for when the start command is called
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

#Context for Echo command
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text= update.message.text)

#caps command. /caps hello world
async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

#Message handler for unknown commands
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


#this is main
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    # the /start command
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    #Echo command
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    #caps command
    caps_handler = CommandHandler('caps', caps)
    application.add_handler(caps_handler)
    
    #unknown commands
    #must be added last. will trigger irresponsibly otherwise
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)


    #runs bot until Ctrl + C
    application.run_polling()

