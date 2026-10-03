from requests import get
from dotenv import load_dotenv
from os import getenv

load_dotenv()
api_key = getenv('STEAM_API_KEY')

def obter_id_jogos(idUsuário):
    idJogos = []

    request = get(f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={idUsuário}&include_appinfo=true&include_played_free_games=true&include_free_sub=true&skip_unvetted_apps=true')

    for jogo in request.json()['response']['games']:
        idJogos.append(jogo['appid'])

    return idJogos

