import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    keyboard = [
                [InlineKeyboardButton("Firmamento", callback_data='0')],

                [InlineKeyboardButton("Boyero", callback_data='1'),
                 InlineKeyboardButton("Casiopea", callback_data='2')],

                [InlineKeyboardButton("Cazo", callback_data='3'),
                InlineKeyboardButton("Cygnet", callback_data='4')],

                [InlineKeyboardButton("Geminis", callback_data='5'),
                InlineKeyboardButton("Hydra", callback_data='6')],

                [InlineKeyboardButton("Osa mayor", callback_data='7'),
                InlineKeyboardButton("Osa menor", callback_data="8")]
                
                
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Seleccione a continuacion:  ', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    
    img = open('./media/imagen.jpg', 'rb')
    
    query.answer()
    if(int(query.data) == 0):
        img = open('./media/firmamento.jpg', 'rb')
        context.bot.send_photo(query.message.chat.id, photo=img)
        query.edit_message_text(text="Imagen seleccionada: Firmamento ")
    elif(int(query.data) == 1):
        img = open('./media/boyero.jpeg', 'rb')
        context.bot.send_photo(query.message.chat.id, photo=img)
        query.edit_message_text(text="Imagen seleccionada: Constelacion Boyero")
    elif(int(query.data) == 2):
        img = open('./media/casiopea.jpeg', 'rb')
        context.bot.send_photo(query.message.chat.id, photo=img)
        query.edit_message_text(text="Imagen seleccionada: Constelacion Casiopea")
    

    print("mande imgen")
    #query.edit_message_text(text="Selected option: {}".format(query.data))


def help(update, context):
    update.message.reply_text("Use /start to test this bot.")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    updater = Updater("1152154692:AAFjrd7G4Z56KW97kL56aLM8-LmSGQauYXM", use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)


    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()