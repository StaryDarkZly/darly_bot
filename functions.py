import requests, re

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
    info = (f"**Nickname:** {nickname}\nID: #{id}\n**Puesto:** {datos2[4]}\n**Clan:** {datos2[3]}\n**Pais:** {datos2[2]}\n**TH principal:** {datos2[0]}\n**TH Oscuro:** {datos2[1]} ")
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
    help = ("Create by: StaryDark (Telegram:t.me/Dark_zly) \nVersion: 1.2")
    return help