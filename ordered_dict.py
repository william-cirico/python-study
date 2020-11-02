"""
Módulo Collections: Ordered Dict

É um dicionário que nos garante a ordem de inserção dos elementos.
"""
# Fazendo o import

from collections import OrderedDict

# Em um dicionário a ordem de inserção dos elementos não é garantida
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3})

for chave, valor in dicionario.items():
    print(f'chave = {chave}:valor={valor}')

