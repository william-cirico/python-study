import sys
# Descobrir se o objeto é iterable
lista = [0, 1, 2, 3, 4, 5]
print(hasattr(lista, '__iter__'))

# Descobrir se o objeto é um iterator
print(hasattr(lista, '__next__'))

# Para tornar um objeto em iterator
lista = iter(lista)
print(hasattr(lista, '__iter__'))
print(next(lista))
print(next(lista))
print(next(lista))

# Saber o tamanho que uma variavel ocupa da memória em bytes
print(sys.getsizeof(lista))

lista_normal = [x for x in range(10000)]
lista_generator = (x for x in range(10000))
print(sys.getsizeof(lista_normal))
print(sys.getsizeof(lista_generator))



