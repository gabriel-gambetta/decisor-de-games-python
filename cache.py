import json

def escrever_cache(biblioteca):
    data = {}

    for game in biblioteca:
          data[str(game.id)] = {}
          data[str(game.id)]['nome'] = game.nome
          data[str(game.id)]['generos'] = game.generos
          data[str(game.id)]['tags'] = game.tags

    with open('cache.json', 'w', encoding='utf-8') as cache:
            json.dump(data, cache, indent=4, ensure_ascii=False)
