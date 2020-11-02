"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas às nossas
List Comprehension
"""
# Exemplos
# 1)
numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# Refatorando
# 0 em Python é False
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]
print(pares)
print(impares)

# 2)
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
