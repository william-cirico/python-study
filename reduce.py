"""
Obs.: A partir do Python3+ a função redcue() não é mais (built-in)
Importar a partido módulo 'functools'

Para entender o reduce()

# Imagine que você tem uma coleção de dados:
dados = [1, 2, 3, 4]

# E você tem uma função que recebe dois parâmetros:
def funcao(x, y):
    return x * y

- A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(1, 2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    Passo 2: res2 = f(2, 3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o resultado
    Isso é repetido até o final
"""
# Na prática
# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista
from functools import reduce
dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23]
# Para utilizar o reduce() precisamos de uma função que recebe dois parâmetros
multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)

# Utilizando um loop normal
res = 1
for n in dados:
    res = res * n

print(res)