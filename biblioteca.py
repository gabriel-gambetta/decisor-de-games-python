import API
from games import Game

def formar_biblioteca(idUsuario):
    biblioteca = []

    idJogos = API.obter_id_jogos(idUsuario)

    for id in idJogos:

        try:
            nome, idTags = API.dados_getitems(id)
            tags = API.nomear_tags(idTags)

            try:
                generos = API.genres_steamspy(id)

            # Fallback dos generos.
            except Exception:
                generos = API.genres_getappdetails(id)


        # Fallback.
        except Exception:
            nome, generos, tags = API.dados_steamspy(id)

        biblioteca.append(Game(nome, generos, tags))

    return biblioteca
