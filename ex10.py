class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
        self.__valor_total = self.__valor_total()

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def valor_total(self):
        return self.__valor_total

    def __valor_total(self):
        return self.__preco * self.__preco


def cad_produtos(lista, quantidade_produtos=2):
    for i in range(1, quantidade_produtos + 1):
        nome = input(f"Digite o nome do produto {i}: ")
        preco = float(input(f"Digite o preço do produto {i}: "))
        quantidade = int(input(f"Digite a quantidade do produto {i}: "))
        lista.append(Produto(nome, preco, quantidade))


def mostra_produtos(lista):
    for i, produto in enumerate(lista):
        print(f"Nome do Produto: {lista[i].nome}")
        print(f"Preço do Produto: {lista[i].preco}")
        print(f"Quantidade do Produto: {lista[i].quantidade}")
        print(f"Valor total em Produtos: {lista[i].valor_total}")


produtos = []
cad_produtos(produtos)
mostra_produtos(produtos)

