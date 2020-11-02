"""
Generators
"""
from sys import getsizeof

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiano', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))

# List comprehension
res = [nome[0] == 'C' for nome in nomes]

# Generator (Ocupa menos memória)
res = (nome[0] == 'C' for nome in nomes)

# Retorna a quantidade de bytes em memória do elemento passado como parâmetro
print(getsizeof('Geek'))

# Gerando uma lista de números com List comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen_comp = getsizeof((x * 10 for x in range(1000)))

print(f'List Comprehension: {list_comp}')
print(f'Set Comprehension: {set_comp}')
print(f'Dictionary Comprehension: {dict_comp}')
print(f'Generator: {gen_comp}')

# Iterando no Generator Expression
gen = (x * 10 for x in range(1000))
for num in gen:
    print(num)
