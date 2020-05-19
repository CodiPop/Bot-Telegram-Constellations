from telegram import InlineQueryResultArticle, InputTextMessageContent, \
 InlineQueryResultVideo, ParseMode, InlineQueryResultPhoto
from uuid import uuid4
import traceback
import logging

logger = logging.getLogger()

def	help(update, context):
	update.message.reply_text("Lista de funciones del bot: ")
	update.message.reply_text("/start propociona un mensaje de ayuda.")
	update.message.reply_text("/imagen envia una imagen de prueba")


def start(update, context):
    update.message.reply_text("El bot de las constelaciones de discretas.")
    
	
    #update.message.reply_text("Escriba /help para ver la lista de funcionalidades del bot")


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
		),
		InlineQueryResultPhoto(
			id=uuid4(), # SE REQUIERE
			title="Imagen",
			type='photo',
			thumb_url="https://www.wallpaperflare.com/static/324/867/787/mage-demon-magic-shield-wallpaper.jpg",
			photo_url="https://img.discogs.com/f3RkPKO_PjUXQidRcp0B0JX898U=/fit-in/500x500/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-14605653-1578051015-5758.jpeg.jpg",
			description="Sents pic of my cutie"
			
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

