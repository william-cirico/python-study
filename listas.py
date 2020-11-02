"""
Listas

Funcionam como vetores/matrizes com a diferença de serem DINÂMICOS
e podem abrigar QUALQUER tipo de dado

Em C (Arrays):
- Possuem tamanho e tipo de dados fixo;

Em Python
- Dinâmico: Não possui tamanho fixo;

Em Python as listas são representadas por: []
"""

type([])

lista1 = [5, 4, 3, 2, 1, 6, 7, 8]
lista2 = ['a', 'b', 'c', 'd']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

# Podemos checar se determinado valor está contido na lista
if 8 in lista4:
    print('Encontrei o número 8')
else:
    print('Não encontrei o número 8')

if 'e' in lista5:
    print('Encontrei a letra "e" na lista')
else:
    print('Não encontrei a letra "e" na lista')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em
# uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas (append)
# Obs.: Com append só conseguimos adicionar 1 elemento por vez
lista1.append(9)
print(lista1)

lista1.append([12, 13])  # Coloca cada elemento da lista como uma nova lista

if [12, 13] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([10, 11])
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# Obs.: Não substitui o valor inicial
lista1.insert(2, "Novo Valor")
print(lista1)

# Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)
lista1.extend(lista2)
print(lista1)

# Imprimir lista invertida
lista1.reverse()
print(lista1)
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Tamanho da lista
print(len(lista3))

# Podemos remover facilmente o último elemento de uma lista
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos repetir elementos em uma lista
nova = [1, 2, 3]
nova *= 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# 1)
curso = "Programação em Python: Essencial"
print(curso)
curso = curso.split()
print(curso)

# 2)
curso = "Programação,em,Python:,Essencial"
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
# Coloca espaço entre cada elemento e gera a string
convertido = ' '.join(curso)
print(convertido)

convertido = '|'.join(curso)
print(convertido)

# Podemos colocar qualquer tipo de dado em uma lista
lista7 = [1, 2.34, 'a', [1232, 1231]]
print(lista7)

# Iterando sobre listas

# 1) Com FOR
for elemento in lista1:
    print(elemento)

# 2) Com WHILE
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]

# Fazemos acesso aos elementos de forma indexada
cores = ['Verde', 'Amarelo', 'Azul', 'Branco']
print(cores[0])  # Verde
print(cores[1])  # Armarelo
print(cores[2])  # Azul
print(cores[3])  # Branco

# Índice negativo funciona como um círculo
print(cores[-1])  # Branco
print(cores[-2])  # Azul
print(cores[-3])  # Amarelo
print(cores[-4])  # Verde

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# - Listas aceitam valores repetidos

# Encontrar o índice de um elemento na lista
numeros = [5, 6, 7, 9, 5]
print(numeros.index(7))  # Caso não exista o elemento na lista ValueError

# Podemos fazer busca dentro de um range
print(numeros.index(5, 1))  # Buscando a partir do indice 1
print(numeros.index(5, 2))

# Podemos fazer busca dentro de um range (Ínicio/Fim)
print(numeros.index(6, 1, 2))

# Revisando slicing

# - lista[inicio:fim:passo]
# - range(inicio:fim:passo)

lista = [1, 2, 3, 4, 5]
print(lista[1, 3, 1])

# Invertendo string
stringa = "Leite"
print(stringa[::-1])

# Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)

# Desempacotamento de lista
lista = [1, 2, 3]
num1, num2, num3 = lista

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 (Deep Copy): Listas independentes
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)
nova.append(4)

print(lista)
print(nova)

# Forma 2 (Shallow Copy): Listas interligadas
lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(4)

print(lista)
print(nova)












