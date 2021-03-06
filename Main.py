from telegram.ext import Updater, CommandHandler, InlineQueryHandler,CallbackQueryHandler

import bot

TOKEN = "1152154692:AAFjrd7G4Z56KW97kL56aLM8-LmSGQauYXM"


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    #Funciones
    dispatcher.add_handler(CommandHandler("start", bot.start))
    dispatcher.add_handler(CommandHandler("help", bot.help))
    dispatcher.add_handler(CommandHandler("imagen", bot.imagen))
    dispatcher.add_handler(CommandHandler("sky", bot.sky))
    updater.dispatcher.add_handler(CallbackQueryHandler(bot.button))
    dispatcher.add_handler(InlineQueryHandler(bot.inline_query))
    # Para el manejo de errores
    dispatcher.add_error_handler(bot.error)

    #Incio bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()      