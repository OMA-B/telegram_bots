from responses import sample_response
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
import os


load_dotenv()
BOT_NAME= "@juxt_simple_bot"


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Type something random to get started!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('If you need help, you should ask it on Google or ChatGPT!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')


# Responses
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text
    message_type: str = update.message.chat.type

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_NAME in text:
            new_text: str = text.replace(BOT_NAME, '').strip()
            response = sample_response(input_text=new_text)
        else:
            return
    else:
        response = sample_response(input_text=text)

    await update.message.reply_text(response)


# Errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused an error: {context.error}')


if __name__ == '__main__':

    print('Bot Awakened...')

    app = Application.builder().token(os.getenv('API_KEY')).build()

    # Commands
    app.add_handler(handler=CommandHandler(command='start', callback=start_command))
    app.add_handler(handler=CommandHandler(command='help', callback=help_command))
    app.add_handler(handler=CommandHandler(command='custom', callback=custom_command))

    # Messages
    app.add_handler(handler=MessageHandler(filters=filters.TEXT, callback=handle_message))

    # Errors
    app.add_error_handler(callback=error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3.0)