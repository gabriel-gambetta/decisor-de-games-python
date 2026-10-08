from random import choice

def decidir_game(biblioteca, gostos):
    listaFiltrada = []
    jogoEscolhido = None
    qtd_gostos = len(gostos.tags)
    qtd_generos = len(gostos.generos)

    # Adiciona jogos a listaFiltrada que possuem pelo menos um atributo em comum com gostos.
    for game in biblioteca:

        for genero in gostos.generos:
            if genero in game.generos and game not in listaFiltrada:
                listaFiltrada.append(game)

        for fantasia in gostos.tags:
            if fantasia in game.tags and game not in listaFiltrada:
                listaFiltrada.append(game)

    if not listaFiltrada:
        return 'Lista Vazia!'

    # Filtro progressivo de generos.
    listaRefinada = listaFiltrada.copy()
    for contador in range(1, qtd_generos + 1):
            
        for game in listaRefinada:
            if len(listaRefinada) == 1:
                break

            else:
                for genero in gostos.generos[0:contador]:
                    if genero not in game.generos:
                        if game in listaRefinada:
                            listaRefinada.remove(game)

    # Filtro progressivo de tags.
    candidatos = listaRefinada.copy()
    for contador in range(1, qtd_gostos + 1):

        for game in candidatos:
            if len(candidatos) == 1:
                break

            else:
                for fantasia in gostos.tags[0:contador]:
                    if fantasia not in game.tags:
                        if game in candidatos:
                            candidatos.remove(game)

    


    if len(candidatos) > 1:
        jogoEscolhido = choice(candidatos).nome

    else:
        jogoEscolhido = candidatos[0].nome

    return jogoEscolhido

class Game:
    def __init__(self, nome, generos, tags):
        self.nome = nome
        self.generos = generos
        self.tags = tags      

