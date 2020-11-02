"""
Módulo Ramdom

- Em Python, módulos são arquivos python.

Módulo Random -> POssui várias funções para geração
de números pseudo-aleatórios.

# Obs.: Existem duas formas de utilitar um módulo
"""
# Forma 1 - Importando o módulo completo
import random

print(random.random())

# Forma 2 - Importando uma função específica do módulo (recomendado)
from random import random

for i in range(10):
    print(random())

# uniform() -> Gerar um número pseudo-aleatório entre os valores estabelecidos
from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 não está incluído

# randint() -> Gera valores pseudo-aleatórios inteiros
from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')

# choice() -> Mostra um valor aleatório entre um iterável
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

# shuffle() -> Tem a função de embaralhar dados
from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(cartas)
