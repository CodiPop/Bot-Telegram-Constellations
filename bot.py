
def start(update, context):
    update.message.reply_text("El bot de las constelaciones de discretas")

def fact(update, context):

    update.message.reply_text("1.")
    update.message.reply_text("2")
        
def imagen(update, context):
	# Obtener la ID del chat
	chat_id = update.message.chat.id
	# archivo
	img = open('./media/imagen.jpg', 'rb')
	# Enviar imagen
	context.bot.send_photo(chat_id, photo=img)