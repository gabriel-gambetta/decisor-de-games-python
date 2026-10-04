from requests import get
from dotenv import load_dotenv
from os import getenv

load_dotenv()
api_key = getenv('STEAM_API_KEY')

def nomear_tags(TagsID):
    listaTags = []
    request = get(f'https://api.steampowered.com/IStoreService/GetTagList/v1/?key={api_key}&language=english')

    if request.status_code != 200:
        return request.status_code

    dados = request.json()

    for id in TagsID:
        for tag in dados['response']['tags']:
            if tag['tagid'] == id:
                listaTags.append(tag['name'])

    return listaTags
