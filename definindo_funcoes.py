"""
Definindo Funções

- Funções são pequenos trechos de código que realizam tarefas específicas;
- Pode ou não receber entrada de dados e retornar saída de dados;
- São úteis para exercutar procedimentos similares por repetidas vezes;
"""

# Exemplo de Utilização
cores = ['verde', 'amarelo', 'branco', 'azul']

# Utilizando a função integrada (Built-in) do Python print()
print(cores)

curso = 'Programação em Python: Essencial'
print(curso)

cores.append('roxo')

# DRY - Don't Repeat Yoursel

# Mas então, como definir funções?
"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
"""

# Definindo a primeira função


def diz_oi():
    print('Oi')


# Utilizando funções
diz_oi()


# Exemplo 2
def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitas anos de vida')
    print('Viva William!!!')


for n in range(5):
    cantar_parabens()


canta = cantar_parabens

canta()




