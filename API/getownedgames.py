from requests import get
from dotenv import load_dotenv
from os import getenv

load_dotenv()
api_key = getenv('STEAM_API_KEY')

def obter_id_jogos(idUsuário):
    idJogos = []

    erro = 0
    while True:
        if erro == 3:
            raise Exception(f'Erro ao tentar obter IDs de jogos da biblioteca, código: {request.status_code}')

        request = get(f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={idUsuário}&include_appinfo=true&include_played_free_games=true&include_free_sub=true&skip_unvetted_apps=true')
        
        if request.status_code != 200:
            erro += 1

        else:
            break  
    
    for jogo in request.json()['response']['games']:
        idJogos.append(jogo['appid'])

    return idJogos