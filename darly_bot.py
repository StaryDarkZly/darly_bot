#version:1.2 by StaryDark

from telegram.ext import Updater, CommandHandler, Filters
import functions

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
    miembros = functions.list_members(clan)
    update.message.reply_text(miembros)
def help(update, context):
    helps = functions.help()
    context.bot.send_message(chat_id=update.effective_chat.id, text=helps)

#Listeners 
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
getinfo_handler = CommandHandler('getinfo', getinfo, pass_args=True)
list_miembros_handler = CommandHandler('getmembers', list_miembros, pass_args=True)

updater.dispatcher.add_handler(getinfo_handler)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.dispatcher.add_handler(list_miembros_handler)
updater.start_polling()
