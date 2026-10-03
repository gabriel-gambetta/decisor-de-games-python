import API.steamlibrary, API.steamappdetails
from time import sleep


idJogos = API.steamlibrary.obter_id_jogos(76561199660430406)

indice, listaGames = API.steamappdetails.dados_steamspy(idJogos)

for game in listaGames:
    print(game.nome)
    print(game.genero)
    print(game.caracteristicas_fantasia)
    sleep(2)