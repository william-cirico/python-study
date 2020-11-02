"""
Módulo Collections - Named Tuple

São tuplas diferenciadas, onde, especificamos um nome para a mesma
e também parâmetros.
"""

# Importando
from collections import namedtuple
tupla = (1, 2, 3)
print(tupla)

# Precisamos definir o nome e parâmetros

# Declaração da tupla
# Forma 1
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

# Acessando os dados
# Forma 1
print(ray[0])  # Idade
print(ray[1])  # Raça
print(ray[2])  # Nome

# Forma 2
print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))
