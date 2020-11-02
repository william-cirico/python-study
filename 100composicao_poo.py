# Quando o objeto é dono de outro objeto

class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = []

    @property
    def nome(self):
        return self.__nome

    def insere_endereco(self, cidade, estado):
        endereco = Endereco(cidade, estado)
        self.__endereco.append(endereco)

    def lista_endereco(self):
        for endereco in self.__endereco:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f"{self.__nome} FOI APAGADO DA MEMÓRIA!")


class Endereco:
    def __init__(self, cidade, estado):
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

    def __del__(self):
        print(f"{self.__cidade}/{self.__estado} FOI APAGADO DA MEMÓRIA!")


cliente1 = Cliente("William", 20)
cliente1.insere_endereco("Blumenau", "SC")
print(cliente1.nome)
cliente1.lista_endereco()
del cliente1

print()
cliente2 = Cliente("Maria", 21)
cliente2.insere_endereco("Florianópolis", "SC")
print(cliente2.nome)
cliente2.lista_endereco()

print("###################################################")


