"""
Funções com Parâmetro

- Funções que recebem dados para serem processados dentro da mesma;

entrada -> processamento -> saída
"""


# Refatorando uma função
def quadrado_de_7():
    return 7 * 7


print(quadrado_de_7())


def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(2))  # TypeError


# Refatorando outra função
def cantar_parabens(nome):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitas anos de vida')
    print(f'Viva {nome}!')


cantar_parabens('William')


# Funções podem ter n parâmetros de entrada
def soma(a, b):
    return a + b


print(soma(2, 3))


# Nomeando parâmetros
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo("William", "Círico"))


# A diferência entre parâmetros e argumentos:
# Argumentos são dados passados durante a execução de uma função;
# Parâmetros são variáveis declaradas na definição de uma função;

# KeyWords Arguments
print(nome_completo(nome='William', sobrenome='Círico'))


# Erro comum na utilização do return
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))


