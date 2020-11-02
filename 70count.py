from itertools import count

lista = [1, 2, 3]
contador = count()
lista = zip(contador, lista)
print(list(lista))