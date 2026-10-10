from requests import get

requisicoes = 0

# Limite de 200 requests / 5 minutos.
def genres_getappdetails(idJogo):
    global requisicoes

    genres = []

    erro = 0
    while True:
        if erro == 3:
            raise Exception(f'Erro ao obter gêneros, código: {request.status_code}')

        if requisicoes > 199:
            raise Exception('Limite da API atingido.')

        request = get(f'https://store.steampowered.com/api/appdetails?appids={idJogo}')

        requisicoes += 1

        if request.status_code != 200:
            erro += 1

        else:
            break

    dadoGame = request.json()

    for genero in dadoGame[str(idJogo)]['data']['genres']:
        genres.append(genero['description'])

    return genres
