import requests
import re



def get_info(id):
    "Obtener informacion de los jugadores del clan"

    url = ("https://www.clashofstats.com/es/players/")
    html = requests.get(url + id + "/summary", timeout=10)
    html = (html.text)
    
    #Get Nickname
    nickname = re.findall(r'<title>.*?Clash of Clans - Resumen</title', html)
    nickname = str(nickname)
    basura = ["['<title>", "de Clash of Clans - Resumen</title']", 'class="num-val">', "</span>"]
    
    
    for delete in basura:
        nickname = nickname.replace(delete, "")

    datos1  = re.findall(r'class="num-val">.*?</span>', html)
    datos2 = []
    for dato in datos1:
        for delete in basura:
            dato = dato.replace(delete, "")
        datos2.append(dato)
    info = (f"Nickname: {nickname}\nID: #{id}\nPuesto: {datos2[4]}\nClan: {datos2[3]}\nPais: {datos2[2]}\nTH principal: {datos2[0]}\nTH Oscuro: {datos2[1]} ")
    return info

def list_members():
    url = ("https://www.clashofstats.com/es/clans/valientes-CLJGPRPV/members/")
    html = requests.get(url, timeout=10)
    html = (html.text)
    
    #Get member list
    memberlist = re.findall(r'r-val__text"><div>.*?</div><div', html)

    #memberlist = str(memberlist)
    borrar = ['r-val__text"><div>', '</div><div']
    members = []
    for member in memberlist:
        for basura in borrar:
            member = member.replace(basura, "")
        members.append(member)
    texto = ""
    count = 0
    for member in members:
        count = count + 1
        texto = (texto + "\n" + str(count) + ">|" + member)

    texto = ("Los miembros actuales del clan son: \n\n" + texto)
    return texto

