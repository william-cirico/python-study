"""
Sorted

sorted() serve para ordenar.
"""
lista = [4, 7, 8, 1, 4, 2]
lista.sort()
print(lista)
numeros = [6, 1, 8, 2]
print(sorted(numeros))  # Sempre retorna uma lista
print(numeros)  # Não modifica o iterável diferente do sort()

# Adicionando parâmetros
print(sorted(numeros, reverse=True))

# Podemos utilizar o sorted para coisas mais complexas
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato", "Eu adoro pizzas"]},
    {"username": "jeff", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros"]}
]

# Ordenando pelo username
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

# Último Exemplo
musicas = [
    {'Título': 'Thunderstruck', 'tocou': 3},
    {'Título': 'Dead Skin Masc', 'tocou': 2},
    {'Título': 'Back in Black', 'tocou': 4}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
