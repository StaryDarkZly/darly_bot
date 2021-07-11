#version:1.4    Created: by StaryDark

from telegram.ext import Updater, CommandHandler, Filters
import functions, time
import threading


token = open("credentials/token.txt").read()
updater = Updater(token=token, use_context=True)

#Funciones de los comandos
def start(update, context):
    """Saluda a Darly"""

    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola mi nombre es Darly, estoy para servirles")

def getinfo(update, context):
    """Obtiene info de un jugador"""
    id = " ".join(context.args)
    info = functions.get_info(id)
    update.message.reply_text(info)  

def list_miembros(update, context):
    """Obtiene la lista de miembros del clan"""
    clan = " ".join(context.args)
    miembros = functions.list_members(clan, onlyname=False)
    update.message.reply_text(miembros)

def help(update, context):
    """Informacion acerca del bot"""
    helps = functions.help()
    context.bot.send_message(chat_id=update.effective_chat.id, text=helps)

isalive = [True, False] #primer argumento=parar el bucle   segundo argumento= evitar que se ejecuten mas bucles
def searchplayers(history, clan, context, update, isalive):
    """ Detectar a nuevos jugadores del clan"""
    isalive[1] = True
    while isalive[0]:
        print ("Escaneo de jugadores iniciado")
        miembros = functions.list_members(clan, onlyname=True)
        for member in miembros:
            if member not in history:
                welcome = ("♦️El jugador " +member+ " se unio al clan...♦️")
                context.bot.send_message(chat_id=update.effective_chat.id, text=welcome)

        history = miembros
        print ("Esperando 5 minutos...")
        time.sleep(300)

def newplayers(update, context, isalive=isalive):
    """Detectar a nuevos jugadores del clan """
    clan = " ".join(context.args)
    history = functions.list_members(clan, onlyname=True)
    whileplayers = threading.Thread(target=searchplayers, args=(history, clan, context, update, isalive))

    if isalive[1]:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ya estoy trabajando en ello...")
    else:
        isalive[0] = True
        whileplayers.start()

def newplayersoff(update, context, isalive=isalive):
    isalive[0] = False
    context.bot.send_message(chat_id=update.effective_chat.id, text="Busqueda apagada")

#Listeners 
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
getinfo_handler = CommandHandler('getinfo', getinfo, pass_args=True)
list_miembros_handler = CommandHandler('getmembers', list_miembros, pass_args=True)
newplayer_handler = CommandHandler('newplayers', newplayers, pass_args=True)
newplayeroff_handler = CommandHandler('newplayersoff', newplayersoff)

updater.dispatcher.add_handler(getinfo_handler)
updater.dispatcher.add_handler(newplayer_handler)
updater.dispatcher.add_handler(newplayeroff_handler)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.dispatcher.add_handler(list_miembros_handler)
updater.start_polling()