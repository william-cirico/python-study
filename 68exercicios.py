from itertools import zip_longest
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4]

# Com zip (para na menor lista)
soma = [x + y for x, y in zip(lista1, lista2)]
print(soma)

# Com zip_longest(para na maior lista)
soma = [x + y if y is not None else x for x, y in zip_longest(lista1, lista2)]
print(soma)
