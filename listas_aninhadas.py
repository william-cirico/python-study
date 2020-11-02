"""
Listas Aninhadas

- Algumas linguagens de programação possuem uma estrutura de dados
chamadas de arrays:
    - Unidimensionais;
    - Multidimensionais;

Em Python nós temos as listas
"""

# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
print(listas)
print(type(listas))

# Como fazemos para acessar os dados
print(listas[0][1])

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension
[[print(num) for num in lista] for lista in listas]

# Outros exemplos
# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando valores inciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])

