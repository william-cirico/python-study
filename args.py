"""
Entendendo o *args

- O *args é um parâmetro como outro qualquer. Isso significa que você
poderá chamar de qualquer coisa, desde que começe com '*'

Exemplo:
*xis

Mas por convenção, utilizamos *args para defini-lo

- O *args utilizado em uma função, coloca os valores extras informados
como entrada em uma tupla.
"""


# Exemplo sem *args
def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))
# print(soma_todos_numeros(4, 6, 9, 2))  TypeError


# Entendendo o *args
def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros(3, 6))


# Outro exemplo
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-Vindo Geek'
    return 'Eu não tenho certeza quem você é...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))


# Desempacotador
numeros = [1, 2, 3, 4, 5, 6, 7]
print(soma_todos_numeros(*numeros))
# Obs.: O * server para informar ao Python que estamos passando
# como argumentos uma coleção de dados, desta forma ele sabe
# que precisa desempacotar os dados.
