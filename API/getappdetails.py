from requests import get

def genres_getappdetails(idJogo):
    genres = []

    request = get(f'https://store.steampowered.com/api/appdetails?appids={idJogo}')

    if request.status_code != 200:
        return request.status_code

    dadoGame = request.json()

    for genero in dadoGame[str(idJogo)]['data']['genres']:
        genres.append(genero['description'])

    return genres
