import API
from time import sleep
from dotenv import load_dotenv
from os import getenv

load_dotenv()
steamID = getenv('STEAM_USER_ID_EXAMPLE')

class Erro(Exception):
    pass

idJogos = API.obter_id_jogos(steamID)

nome, tags = API.dados_getitems(440)

if nome == 'Team Fortress 2':
    raise Erro(f'Erro ao tentar obter jogo, HTTP {nome}')

print(nome)
print(tags)