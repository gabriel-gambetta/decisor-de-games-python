import API.steamlibrary, API.steamappdetails, API.taglist
from time import sleep
from dotenv import load_dotenv
from os import getenv

load_dotenv()
steamID = getenv('STEAM_USER_ID_EXAMPLE')


idJogos = API.steamlibrary.obter_id_jogos(steamID)

print(API.taglist.nomear_tags([1695, 122, 1684]))
