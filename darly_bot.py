#version:0.1 by StaryDark

from telegram.ext import Updater, CommandHandler, Filters
import functions

token = open("credentials/token.txt").read()

updater = Updater(token=token, use_context=True)
admins = ["@Dark_zly"]

#Commands
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola mi nombre es Darly, estoy para servirles")

def getinfo(update, context):
    id = " ".join(context.args)
    info = functions.get_info(id)
    update.message.reply_text(info)  

def list_miembros(update, context):
    miembros = functions.list_members()
    update.message.reply_text(miembros)

#Listeners 
start_handler = CommandHandler('start', start, Filters.user(username=admins))
getinfo_handler = CommandHandler('getinfo', getinfo, pass_args=True)
list_miembros_handler = CommandHandler('getmembers', list_miembros)

updater.dispatcher.add_handler(getinfo_handler)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(list_miembros_handler)
updater.start_polling()
