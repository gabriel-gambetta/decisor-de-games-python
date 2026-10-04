import API.getownedgames, API.steamspy, API.gettaglist, API.getappdetails, API.getitems
from time import sleep
from dotenv import load_dotenv
from os import getenv

load_dotenv()
steamID = getenv('STEAM_USER_ID_EXAMPLE')


idJogos = API.getownedgames.obter_id_jogos(steamID)

nome, tags = API.getitems.dados_getitems(489830)

print(nome)
print(tags)