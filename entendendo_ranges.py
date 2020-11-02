"""
* Precisamos conhecer for para conhecer ranges
* Precisamos conhecer os ranges para trabalhar com o for

Ranges são utilizados para gerar sequências numéricas, não de forma
aleatória, mas sim de maneira especificada.

Obs.: Ínicio padrão 0 e passo de 1 em 1
"""

# Forma 1 (Sem valor inicial)
for num in range(11):
    print(num)

# Forma 2 (Com valor inicial)
for num in range(1, 11):
    print(num)

# Forma 3 (Com valor inicial e valor de passo)
for num in range(2, 11, 2):
    print(num)

# Forma 4 (Descrescente)
for num in range(10, 2, -2):
    print(num)




