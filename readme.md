# Decisor de Games
> Um decisor para o indeciso.

Por enquanto, o Decisor pega a biblioteca do usuário através do SteamID64 e monta uma lista de jogos. Cada jogo possui gêneros, definidos oficialmente, e tags, associadas popularmente àquele jogo, mas não oficiais. Junto às preferências de gêneros e tags do usuário, o decisor aplica filtros progressivos, buscando deixar apenas um candidato. Caso ainda reste mais de um jogo após os filtros, um deles é escolhido aleatoriamente.

## Tecnologias utilizadas

- Python
- Requests
- python-dotenv
- Git
- Steam Web API
- SteamSpy API
- GetAppDetails API

## Status

Em desenvolvimento.

### Próximos passos

- Atualizar como é atualizado o cache pra evitar reescrever o arquivo inteiro.
- Adicionar novos filtros opcionais para refinar as recomendações.
- Criar uma interface gráfica (GUI) para facilitar a utilização do programa.
