def novo_game():

    nome = input("Nome: ")
    fantasia = input("Fantasia: ")
    categoria = input("Categoria: ")

    fantasia_ativa = (input("Interesse: "))

    if fantasia_ativa[0].upper() in 'T1':
        fantasia_ativa = True

    elif fantasia_ativa[0].upper() in 'F0':
        fantasia_ativa = False

    else:
        fantasia_ativa = None

    return Game(nome, fantasia, categoria, fantasia_ativa)


class Game:
    def __init__(self, nome, fantasia, categoria, fantasia_ativa):
        self.nome = nome
        self.fantasia = fantasia
        self.categoria = categoria
        self.fantasia_ativa = fantasia_ativa

