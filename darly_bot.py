#version:2.0    Created: by StaryDark

from telegram.ext import Updater, CommandHandler, Filters
import telegram
import threading, time, random, os
import functions

config = functions.config() 

print ("Iniciando a darly....")
os.system("clear")
print ("\nDarly ha sido iniciado...")

updater = Updater(token=config["token"] , use_context=True)

#Funciones de los comandos
def start(update, context):
    """Saluda a Darly"""
    saludos = ("Hola mi nombre es Darly, estoy para servirles", "Si si, estoy aqui", "Holaa", "Usted diga y yo ejecuto", "Quien osa llamarme!","No puedes vivir sin mi xd")
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(saludos))

def getinfo(update, context):
    """Obtiene info de un jugador"""
    
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    id = " ".join(context.args)
    if len(id) < 4:
        update.message.reply_text("ID invalido... Debes darme el id de jugador para encontrarlo :b\n\nEj: /getinfo P99QYJJVC \nRecuerda no usar #")  
    else:
        info = functions.get_info(id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=info, disable_web_page_preview = True, parse_mode=telegram.ParseMode.HTML)
        #context.bot.send_message(chat_id=update.effective_chat.id, text=info)
        

def list_miembros(update, context, clan=config["clan"]):
    """Obtiene la lista de miembros del clan"""
    miembros = functions.list_members(clan, onlyname=False)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text(miembros)

def help(update, context):
    """Informacion acerca del bot"""
    helps = functions.help()
    context.bot.send_message(chat_id=update.effective_chat.id, text=helps)

isalive = [False, False] #primer= Parar proceso segundo = Evitar mas de un subproceso
def searchplayers(history, context, update, isalive, clan=config["clan"]):
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

def newplayers(update, context, isalive=isalive, clan=config["clan"]):
    """Detectar a nuevos jugadores del clan """
    history = functions.list_members(clan, onlyname=True)
    whileplayers = threading.Thread(target=searchplayers, args=(history, context, update, isalive))

    if isalive[1]:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ya estoy trabajando en ello...")
    else:
        isalive[0] = True
        whileplayers.start()

def newplayersoff(update, context, isalive=isalive):
    isalive[0] = False
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