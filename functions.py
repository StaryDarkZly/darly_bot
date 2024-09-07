import requests, re, os, sys


def config():
    print ("Bienvenido a la configuracion del bot (:D)\n\n")
    loadconfig = input('Usar configuracion por defecto?(y/n)-->')
    if loadconfig == 'y':
        if os.path.exists('config.txt'):
            fconfig = open('config.txt', 'r')
            lineas = fconfig.readlines()
            clan = lineas[0]
            token = lineas[1]    
            config = {"clan":clan, "token":token}
            fconfig.close()
            if os.name == 'nt':
                os.system("cls")
            else:
                os.system("clear")
            return config

        else:
            print('Configuracion no detectada')
            print('Creando configuracion')
            loadconfig = 'n'
    if loadconfig == 'n':
        token = input("Ingresa el token del bot\n-->")
        clan = input("Ingresa el ID de vuestro clan (sin #) \n-->")

    
        config = {"clan":clan, "token":token}
        
        fconfig = open('config.txt', 'w')
        clan = clan + '\n'
        fconfig.write(clan)
        fconfig.write(token)
        fconfig.close()
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
        return config
        
    else:
        print ('Parametro no valido, intentalo de nuevo.')
        sys.exit()


def get_info(id):
    """Obtener informacion de los jugadores del clan"""
    
    url = ("https://www.clashofstats.com/es/players/")
    

    try:
        html = requests.get(url + id + "/summary", timeout=10)
        html = (html.text)
    except:
        return "Clash of Stats no disponible..."
    
    #Get Nickname
    nickname = re.findall(r'<title>.*?Clash of Clans - Resumen</title', html)
    nickname = str(nickname)
    basura = ["['<title>", "de Clash of Clans - Resumen</title']", 'class="num-val">', "</span>"]
    for delete in basura:
        nickname = nickname.replace(delete, "")
    
    #Get other info
    datos1  = re.findall(r'class="num-val">.*?</span>', html)
    datos2 = []
    for dato in datos1:
        for delete in basura:
            dato = dato.replace(delete, "")
        datos2.append(dato)
    playerlink = ("https://link.clashofclans.com/es?action=OpenPlayerProfile&tag=" + id)
    try:
        info = (f'<b>Nickname:</b> <code>{nickname}</code>\n<b>ID:</b> <code>{id}</code> <a href="{playerlink}">PlayerLink</a> \n<b>Puesto:</b> <code>{datos2[4]}</code>\n<b>Clan:</b> <code>{datos2[3]}</code>\n<b>Pais:</b> <code>{datos2[2]}</code>\n<b>TH principal:</b> <code>{datos2[0]}</code>\n<b>TH Oscuro:</b> <code>{datos2[1]}</code>')
    except:
        print ("[ERROR] - Jugador no encontrado")
        info = "Jugador/Clan no encontrado..."
    return info

def list_members(clan, onlyname):
    """Obtener la lista de miembros del clan"""
    try:
        url = (f"https://www.clashofstats.com/es/clans/valientes-{clan}/members/")
        html = requests.get(url, timeout=10)
    except:
        return "Clasf of Stats no esta disponible..."
    html = (html.text)

    memberlist = re.findall(r'r-val__text"><div>.*?</div><div', html)

    borrar = ['r-val__text"><div>', '</div><div']
    members = []
    texto = ""
    count = 0
    
    for member in memberlist:
        for basura in borrar:
            member = member.replace(basura, "")
        members.append(member)
    if onlyname == True:
        return members
    else:
        for member in members:
            count = count + 1
            texto = (texto + "\n" + str(count) + ">|" + member)

        texto = ("Los miembros actuales del clan son: \n\n" + texto)
        return texto

def help():
    help = ("""Comandos del bot:\n  
/start - Saluda a Darly.
/help - Obten informacion acerca de darly.
/getinfo - Obten informacion de un jugador. \n   ej: /getinfo UYLN3FIW (sin usar el #)
/getmembers - Obten la lista de jugadores de tu clan.
/newplayers - Detectar a nuevos jugadores en tu clan
/newplayersoff - Parar la busqueda de nuevos jugadores
\nCreate By: StaryDarkz (t.me/StaryDarkz) - DaryBot_v2.1
""")
    return help