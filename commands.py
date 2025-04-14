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
    