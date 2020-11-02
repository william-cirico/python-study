"""
Min e Max

max() = Retorna o maior valor em um iterável ou o maior de dois elementos
min() = Retorna o menor valor em um iterável ou o maior de dois elementos
"""
# Exemplos Max()
lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

dicionario = {'a': 10, 'b': 20, 'c': 100}
print(max(dicionario.values()))

print(max(2, 34))

val1 = int(input('Informe o valor 1: '))
val2 = int(input('Informe o valor 2: '))
print(max(val1, val2))

nomes = ['Arya', 'Sansa', 'Jon', 'Daenerys']

print(max(nomes))  # Vai printar Sansa
print(max(nomes, key=lambda nome: len(nome)))

musicas = [
    {"título": "Thunderstruck", "tocou": 3},
    {"título": "T.N.T.", "tocou": 2},
    {"título": "Back in Black", "tocou": 4}
]

print(max(musicas, key=lambda musica: musica["tocou"])['título'])

maxi = 0
for musica in musicas:
    if musica["tocou"] > maxi:
        maxi = musica["tocou"]

for musica in musicas:
    if musica["tocou"] == maxi:
        print(musica["título"])


# Exemplos Min()
lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

dicionario = {'a': 10, 'b': 20, 'c': 100}
print(min(dicionario.values()))

print(min(2, 34))

val1 = int(input('Informe o valor 1: '))
val2 = int(input('Informe o valor 2: '))
print(min(val1, val2))
