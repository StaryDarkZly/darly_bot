# Darly Bot
<img src="image.jpg" alt="Avatar del Bot" width="300"/>
## Requisitos:

>Python3

>Token de bot de telegram

## Instalacion y configuracion:

 Para descargar e instalar los archivos necesarios:

```
git clone https://github.com/StaryDarkZly/darly_bot.git
cd darly_bot
pip install -r requeriments.txt
python darly_bot.py
```

La primera vez en ejecutar el bot te pedira el token y id del clan, luego se guardara por defecto, podras cargar esta config o cambiar los datos en el archivo de configuracion creado.


## Comandos Telegram:

Darly debe tener permisos de administrador o tendras que usar el @alias en cada comando


`/start`      - Saluda a Darly y validar si esta activo.

`/help`       - Obten informacion acerca de darly.

`/getinfo`    - Obten informacion de un jugador.
    
    ej: `/getinfo UYLN3FIW`  (sin usar el #)

`/getmembers` - Obten la lista de jugadores de tu clan.

`/newplayers` - Detectar a nuevos jugadores en tu clan

`/newplayersoff` - Parar la busqueda de nuevos jugadores

