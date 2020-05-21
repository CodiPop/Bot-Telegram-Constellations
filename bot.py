from telegram import InlineQueryResultArticle, InputTextMessageContent, \
 InlineQueryResultVideo, ParseMode, InlineQueryResultPhoto, InlineKeyboardButton, InlineKeyboardMarkup
from uuid import uuid4
import traceback
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def	help(update, context):
	update.message.reply_text("Lista de funciones del bot: ")
	update.message.reply_text("/start propociona un mensaje de ayuda.")
	update.message.reply_text("/sky despliega un menu de opciones para escoger la constelacion deseada.")
	update.message.reply_text("/imagen envia una imagen de prueba")


def start(update, context):
    update.message.reply_text("El bot de las constelaciones de discretas.")
    update.message.reply_text("Escriba /help para ver la lista de funcionalidades del bot")

def sky(update, context):
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


def imagen(update, context):
	# Obtener la ID del chat
	chat_id = update.message.chat.id
	# archivo
	img = open('./media/imagen.jpg', 'rb')
	# Enviar imagen
	context.bot.send_photo(chat_id, photo=img)



def inline_query(update, context):
	mensaje = "/start propociona un mensaje de ayuda. \n /imagen envia una imagen de prueba "
	# opciones a desplegar
	results = [
		InlineQueryResultArticle(
			id=uuid4(), # SE REQUIERE
			title="Help",
			thumb_url="https://www.wallpaperflare.com/static/324/867/787/mage-demon-magic-shield-wallpaper.jpg",
			input_message_content=InputTextMessageContent(mensaje),
			description="Lista de funcionalidades."
		)
	]

	# enviar resultado
	try:
		update.inline_query.answer(results, cache_time=2)
	except Exception as e:
		traceback.print_stack()
		print(e)

# Función para el manejo de errores
def error(update, context):
    logger.warning('La solicitud "%s" causó el error "%s"', update, context.error)

