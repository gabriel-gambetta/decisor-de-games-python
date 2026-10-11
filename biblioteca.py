import API
import cache
from models.games import Game

def formar_biblioteca(idUsuario):
    biblioteca = []
    jogoNovo = False

    idJogos = API.obter_id_jogos(idUsuario)

    try:
        listaTags = API.listar_tags()

    except Exception:
        listaTags = None

    for id in idJogos:
        dadosCache = cache.ler_cache(id)

        # Cache hit.
        if dadosCache is not None:
            nome, generos, tags = dadosCache

        # Cache miss.
        else:
            if listaTags is not None:

                try:
                    nome, idTags = API.dados_getitems(id)
                    tags = API.nomear_tags(idTags, listaTags)

                    try:
                        generos = API.genres_steamspy(id)

                    # Fallback dos generos.
                    except Exception:
                        generos = API.genres_getappdetails(id)


                # Fallback do dados_getitems()
                except Exception:
                    nome, generos, tags = API.dados_steamspy(id)

            # Fallback de listar_tags().
            else:
                nome, generos, tags = API.dados_steamspy(id)

            jogoNovo = True


        biblioteca.append(Game(id, nome, generos, tags))

    if jogoNovo:
        cache.escrever_cache(biblioteca)

    return biblioteca
