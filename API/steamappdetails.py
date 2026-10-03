from requests import get
from time import sleep
from games import Game

def dados_steamspy(idJogos):
    listaGames = []

    for indice, id in enumerate(idJogos):

        erros = 0  
        while erros <= 2:
            game = get(f'https://steamspy.com/api.php?request=appdetails&appid={id}')


            if game.status_code == 200:
                dadoGame = game.json()

                listaGames.append(Game(
                    dadoGame['name'],
                    dadoGame['genre'].split(", "),
                    list(dadoGame['tags'])
                ))

                break

            else:
                erros += 1
                sleep(5)

        if erros > 2:
            return indice, listaGames

    return indice, listaGames