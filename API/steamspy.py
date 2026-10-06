from requests import get

def dados_steamspy(idJogo):
    nome = generos = tags = None


    erro = 0
    while True:
        if erro == 3:
            raise Exception(f'Erro ao tentar obter jogo, código: {request.status_code}')

        request = get(f'https://steamspy.com/api.php?request=appdetails&appid={idJogo}')

        if request.status_code != 200:
            erro += 1

        else:
            break


    gameDado = request.json()

    nome = gameDado['name']
    generos = gameDado['genre'].split(", ")
    tags = list(gameDado['tags'])

    return nome, generos, tags

def genres_steamspy(idJogo):
    genres = None

    erro = 0
    while True:
        if erro == 3:
            raise Exception(f'Erro ao obter gêneros, código: {request.status_code}')

        request = get(f'https://steamspy.com/api.php?request=appdetails&appid={idJogo}')

        if request.status_code != 200:
            erro += 1

        else:
            break

    dadoGame = request.json()

    genres = (dadoGame['genre'].split(", "))

    return genres
