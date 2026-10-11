from json import load, dump

def ler_cache(idJogo):

      with open('data/cache.json', 'r', encoding='utf-8') as cache:
            cachejson = load(cache)

            jogo = cachejson.get(str(idJogo))

            if jogo is None:
                  return None
            
            else:
                  nome = jogo['nome']
                  generos = jogo['generos']
                  tags = jogo['tags']

      return nome, generos, tags

def escrever_cache(biblioteca):
    data = {}

    for game in biblioteca:
          data[str(game.id)] = {}
          data[str(game.id)]['nome'] = game.nome
          data[str(game.id)]['generos'] = game.generos
          data[str(game.id)]['tags'] = game.tags

    with open('data/cache.json', 'w', encoding='utf-8') as cache:
            dump(data, cache, indent=4, ensure_ascii=False)
