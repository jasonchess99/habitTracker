from telegram import Update
from telegram.ext import(
    filters, 
    ApplicationBuilder, 
    ContextTypes, 
    CommandHandler, 
    MessageHandler
)

import string


#context for when the start command is called
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = "I'm a bot, please talk to me!")


#Message handler for unknown commands
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text =  "Sorry, I didn't understand that command.")


#Log Command
async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #converts context.args into a string concat with spaces in between the words
    #created through the command handler, any words after the command are sent to this
    logText = " ".join(context.args)

    await update.message.reply_text(
        f"Logged: {logText}")
    

#callback function for sending message
async def reminder_callback(context):
    reminder = context.job.data
    chat_id = context.job.chat_id
    await context.bot.send_message(chat_id=chat_id, text=reminder)

#reminde me  function creates periodic reminders of whatever the user specifies
async def remindMe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #minutes between subsequent reminders
    intervalMinutes = int(context.args[0])

    #reminder text
    reminderText = " ".join(context.args[1:])


    #converts to minutes
    intervalMinutes = intervalMinutes*60
    startMinutes = 0


    #continually runs at the set parameters
    context.job_queue.run_repeating(callback=reminder_callback,
                                    interval=intervalMinutes,
                                    first=startMinutes,
                                    chat_id=update.effective_chat.id,
                                    data=reminderText)

    
    