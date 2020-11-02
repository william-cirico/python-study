"""
Len, Abs, Sum, Round

# Len
len() - Retorna o tamanho de um iterável

# Abs
abs() - Retorna o valor absoluto de um número inteiro ou real.

# Sum
sum() - Retorna a soma total dos elementos
# Obs.: O valor inicial default = 0

# Round
round() - Retorna um número arredondado para n dígitos.
"""
# Len
print(len("Geek University"))
print(len([1, 2, 3, 4, 5]))

# Dunder len
print('Geek University'.__len__())

# Abs
print(abs(-7.5))
print(abs(-6))

# Sum
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))

# Round
print(round(10.5))
print(round(10.6))
print(round(1.212121221, 2))
print(round(1.219121221, 2))

