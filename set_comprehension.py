"""
Set Comprehension

Set = {1, 2, 3, 4}
"""
# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplo
numeros = {x ** 2 for x in range(10)}
print(numeros)

# Desafio: Faça uma alteração na estrutura acima para gerar um dicionário
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Finalizando
letras = {letra for letra in 'Geek University'}
print(letras)
