"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



chat = {'supergroup_chat_created': False, 'new_chat_members': [], 'message_id': 84, 'new_chat_photo': [], 'entities': [], 'text': 'Hahsjqus', 'delete_chat_photo': False, 'group_chat_created': False, 'caption_entities': [], 'date': 1657929693, 'photo': [], 'channel_chat_created': False, 'chat': {'type': 'private', 'first_name': 'Benja', 'id': 1834202461}, 'from': {'language_code': 'es', 'id': 1834202461, 'is_bot': False, 'first_name': 'Benja'}}
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

def codigo_seguridad(codigo):
    if codigo == 'PRUEBA_SIDEAM':
        return True
    else:
        return False

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Usa /login código_de_seguridad para iniciar sesion')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    print(update.message)
    print(context)
    update.message.reply_text(update.message.text)

def login(update, context):
    """Echo the user message."""
    codigo = update.message.text[6:].strip()
    valido = codigo_seguridad(codigo)
    if valido:
        update.message.reply_text(f'Código correcto')

    else:
        update.message.reply_text(f'Código incorrecto')

def notif():

    chat['message'].reply_text(f'Código correcto')




def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5404787066:AAGu2V4AcnnYiSsLx4ZzXaj_ohR_4fU-OMQ", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("login", login))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)



    # Start the Bot
    updater.start_polling()
    print("Bot started")
    notif()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.

    # updater.idle()


if __name__ == '__main__':
    main()