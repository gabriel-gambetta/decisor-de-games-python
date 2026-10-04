import API.getownedgames, API.steamspy, API.gettaglist, API.getappdetails
from time import sleep
from dotenv import load_dotenv
from os import getenv

load_dotenv()
steamID = getenv('STEAM_USER_ID_EXAMPLE')


idJogos = API.getownedgames.obter_id_jogos(steamID)

print(API.getappdetails.genres_getappdetails(440))
