def	help(update, context):
	update.message.reply_text("Lista de funciones del bot: ")
	update.message.reply_text("/start propociona un mensaje de ayuda.")
	update.message.reply_text("/imagen envia una imagen de prueba")




def start(update, context):
    update.message.reply_text("El bot de las constelaciones de discretas.")
    
	
    update.message.reply_text("Escriba /help para ver la lista de funcionalidades del bot")


def imagen(update, context):
	# Obtener la ID del chat
	chat_id = update.message.chat.id
	# archivo
	img = open('./media/imagen.jpg', 'rb')
	# Enviar imagen
	context.bot.send_photo(chat_id, photo=img)