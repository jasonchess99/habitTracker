#function files
from commands import *

#allow for OS operations to be ran by this script
import os

#Logging
import logging

#reading environment Variables
from dotenv import load_dotenv

#Telegram dependencies
from telegram import Update
from telegram.ext import(
    filters,
    Application, 
    ApplicationBuilder, 
    ContextTypes, 
    CommandHandler, 
    MessageHandler
)



#loading .env file and instantiating the bot token within this script (hard code bypass)
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


#creates logging for when bot crashes
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



#this is main
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    #start the jobqueue
    job_queue = application.job_queue
    
    # the /start command
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)


    #log command
    log_handler = CommandHandler('log', log)
    application.add_handler(log_handler)
    
    

    # /remindme 60 example reminder
    # reminds the user every 60 minutes
    remindMe_handler = CommandHandler('remindme', remindMe)
    application.add_handler(remindMe_handler)
    
    #unknown commands
    #must be added last. will trigger irresponsibly otherwise
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

    #runs bot until Ctrl + C
    application.run_polling()

