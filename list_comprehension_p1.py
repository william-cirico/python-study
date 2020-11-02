"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas
com dados processados a partir de um iterável.

# Sintaxe:
[dado for dado in iterável]
"""
# Exemplos
numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)
res = [numero / 2 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]

# List Comprehension x Loop
numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)

print([numero * 2 for numero in numeros])

# 1)
nomes = 'Geek University'
print([letra.upper() for letra in nomes])

# 2)
amigos = ['maria', 'julia', 'pedro', 'guilherme']
print([amigo.title() for amigo in amigos])

# 3)
print([numero * 3 for numero in range(1, 10)])

# 4)
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5)
print([str(numero) for numero in [1, 2, 3, 4, 5]])

