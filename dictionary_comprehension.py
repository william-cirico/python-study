"""
Dictionary Comprehension

Se quisermos criar uma lista fazemos:
lista = [1, 2, 3, 4]

Se quisermos criar uma tupla:
tupla = (1, 2, 3, 4)  # 1, 2, 3, 4

Se quisermos criar um set(conjunto):
conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário:
dicionário = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxe:
{chave:valor for valor in iterável}
"""
# Exemplos
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

numero = [1, 2, 3, 4, 5, 1, 2]  # Não aceita repetição de valor
quadrados = {valor: valor ** 2 for valor in numero}
print(quadrados)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo com lógica condicional
res = {num: ('par' if not num % 2 else 'impar') for num in numero}
print(res)