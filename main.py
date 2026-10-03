import API.steamlibrary, API.steamappdetails
from time import sleep
from dotenv import load_dotenv
from os import getenv

load_dotenv()
steamID = getenv('STEAM_USER_ID_EXAMPLE')


idJogos = API.steamlibrary.obter_id_jogos(steamID)

indice, listaGames = API.steamappdetails.dados_steamspy(idJogos)

for game in listaGames:
    print(game.nome)
    print(game.genero)
    print(game.caracteristicas_fantasia)
    sleep(2)