from requests import get
from dotenv import load_dotenv
from os import getenv

load_dotenv()
api_key = getenv('STEAM_API_KEY')

def listar_tags():
        
    erro = 0
    while True:
        if erro == 3:
            raise Exception(f'Erro ao obter lista de tags, código: {request.status_code}')
        
        request = get(f'https://api.steampowered.com/IStoreService/GetTagList/v1/?key={api_key}&language=english')

        if request.status_code != 200:
            erro += 1

        else:
            break

    listaTags = request.json()

    return listaTags

def nomear_tags(tagsID, listaTags):
    tags = []

    for id in tagsID:
        for tag in listaTags['response']['tags']:
            if tag['tagid'] == id:
                tags.append(tag['name'])

    return tags
