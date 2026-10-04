from requests import get
from dotenv import load_dotenv
from os import getenv

load_dotenv()
api_key = getenv('STEAM_API_KEY')

def dados_getitems(idJogo):
    nome = None
    idTags = []

    request = get(f'https://api.steampowered.com/IStoreBrowseService/GetItems/v1/?key={api_key}&input_json=%7B%22ids%22%3A%5B%7B%22appid%22%3A%22{idJogo}%22%7D%5D%2C%22context%22%3A%7B%22language%22%3A%22english%22%2C%22country_code%22%3A%22US%22%7D%2C%22data_request%22%3A%7B%22include_tag_count%22%3A%2250%22%7D%7D')

    if request.status_code != 200:
        return request.status_code

    gameDado = request.json()

    nome = gameDado['response']['store_items'][0]['name']

    for id in gameDado['response']['store_items'][0]['tagids']:
        idTags.append(id)

    return nome, idTags
