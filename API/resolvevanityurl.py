from requests import get
from dotenv import load_dotenv
from os import getenv

load_dotenv()
api_key = getenv('STEAM_API_KEY')

def traduzir_vanity_url(vanityname):

    erro = 0
    while True:
        if erro == 3:
            raise Exception(f'Erro ao traduzir vanity url, código: {request.status_code}')

        request = get(f'https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/?key={api_key}&vanityurl={vanityname}&url_type=1')

        if request.status_code != 200:
            erro += 1

        else:
            break

    dados = request.json()
    codigo_sucesso = dados['response']['success']

    if codigo_sucesso != 1:
        raise Exception(f"Erro API, código: {codigo_sucesso}")

    steamID = dados['response']['steamid']

    return steamID
    