"""
Funções com parâmetro padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional;
"""


def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(3))
print(exponencial(3, 2))

# Obs.: Em funções Python, os parâmetros com valores default
# devem sempre estar ao final da declaração


# Outro exemplo:
def soma(num1=5, num2=3):
    return num1 + num2


print(soma(4, 3))
print(soma(3))
print(soma())


# Exemplo mais complexo
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))

# Motivos para utilizar parâmetros com valor default
# - Flexibilidade nas funções;
# - Evita erros com parâmetros incorretos;
# - Nos permite trabalhar com exemplos mais legíveis de código;


def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def math(num1, num2, fun=soma):
    return fun(num1, num2)


print(math(2, 3))
print(math(2, 2, subtracao))

total = 0


# Evitar variáveis Globais
# Escopo
def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total += 1
    return total


# Funções declaradas dentro de funções
def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())



