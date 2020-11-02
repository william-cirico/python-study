"""
Filter
filter(): Serve para filtrar dados de uma determinada coleção
"""
# Biblioteca para trabalhar com dados estatísticos
import statistics
valores = 1, 2, 3, 4, 5, 6
media = sum(valores) / len(valores)
print(media)

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
# Obs.: Assim como a função map(), a filter recebe 2 parâmetros
# função e iterável
res = filter(lambda valor: valor > media, dados)
print(list(res))
# Assim como map() os dados se auto-destroem ao sere utilizados
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia']
print(paises)
res = filter(None, paises)
print(list(res))

# A diferença entre map e filter é:
# map(): retorna um objeto mapeando a função para cada elemento do iteável;
# filter(): retorna um objeto filtrando apenas os elementos de acordo com a função;

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato", "Eu adoro pizzas"]},
    {"username": "jeff", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros"]}
]


# Filtrar os usuários que estão inativos no Twitter

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

# Combinar filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f'Sua intrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

