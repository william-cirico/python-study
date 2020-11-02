"""
JSON e Pickle

JSON -> JavaScript Object Notation (É um dicionário)
API -> São meios de comunicação entre o serviços e terceiros
json.dumps -> Formata para o formato json
"""
import json
import jsonpickle
ret = json.dumps(["produto", {"Playstation 4": ("2TB", "Novo", "220V", 2340)}])


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato("Felix", "Vira-Lata")
ret = json.dumps(felix.__dict__)

# Integrando o JSON com o Pickle (pip install jsonpickle)
ret = jsonpickle.encode(felix)

# Escrevendo o arquivo json/pickle
with open("felix.json", "w") as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

# Lendo o arquivo json/pickle
with open("felix.json", "r") as arquivo:
    counteudo = arquivo.read()
    ret = jsonpickle.decode(counteudo)
    print(ret)
    print(ret.nome)
    print(ret.raca)
