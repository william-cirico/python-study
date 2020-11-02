"""
Entendendo Iterator e Iterable

* Iterator
  - Um objeto que pode ser iterável
  - Retoran um dado quando uma função next() é chamada

* Iterable
  - Um objeto que irá retornar um iterator quando a função iter() for chamada.
"""
# Exemplos de Iterable
nome = 'Geek'
numeros = {1, 2, 3, 4, 5, 6}

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

for letra in nome:
    print(f'{letra}', end=' ')
