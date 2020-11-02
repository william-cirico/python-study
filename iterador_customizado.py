"""
Criando um iterador customizado
range()
"""
for n in range(11):
    print(n)


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration


for n in Contador(0, 11):
    print(n)



