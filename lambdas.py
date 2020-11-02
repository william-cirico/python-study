"""
Utilizando lambdas

- São funções sem nome ou anônimas;

# Função em Python
def soma(a, b):
    return a + b
"""


# Expressão Lambda
lambda a, b: a + b

# Como usar
calc = lambda a, b: a + b
print(calc(1, 2))

# Podemos ter expressões lambdas com múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' William ', ' círico '))

amar = lambda: 'Como não amar Python'
print(amar())

# Outro exemplo
autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heilein', 'Arthur C. Clarke', 'Frank Herbert',
           'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

# [-1] pega o último elemento da lista
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

# Função Quadrática
# f(x) = a * x ** 2 + b * x + c


# Definindo a função
def geradora_função_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_função_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

