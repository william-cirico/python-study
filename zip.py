"""
zip() - Cria um iteável (Zip Object) que agrega cada elemento
de cada um dos iteráveis passados como entrada em pares.
"""
# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)

print(list(zip1))

texto = 'abcdefg', 'absdw'
numeros = 123456, 12323

zip2 = zip(texto, numeros)

print(list(zip2))

tupla = 1, 2, 3
lista = [4, 5, 6]
dicionario = {"a": 7, "b": 8, "c": 9}
zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))