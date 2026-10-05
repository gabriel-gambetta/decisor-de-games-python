import API
from time import sleep
from dotenv import load_dotenv
from os import getenv

load_dotenv()
steamID = getenv('STEAM_USER_ID_EXAMPLE')


idJogos = API.obter_id_jogos(steamID)

nome, tags = API.dados_getitems(489830)

print(nome)
print(tags)