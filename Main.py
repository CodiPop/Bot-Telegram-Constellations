from telegram.ext import Updater, CommandHandler
import bot

TOKEN = "1152154692:AAFjrd7G4Z56KW97kL56aLM8-LmSGQauYXM"


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    #Funciones
    dispatcher.add_handler(CommandHandler("start", bot.start))
    dispatcher.add_handler(CommandHandler("fact", bot.fact))
    dispatcher.add_handler(CommandHandler("imagen", bot.imagen))

    #Incio bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()      