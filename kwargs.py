"""
**kwargs

Poderíamos chamar este parâmetro de **xis, mas por convenção
se usa **kwargs;

- O **kwargs exige que utilizemos parâmetros nomeados e transforma
eles em um dicionário.

* Ordem dos parâmetros:
 1 - Parâmetros Obrigatórios;
 2 - *args;
 3 - Parâmetros Default;
 4 - **kwargs;
"""


# Exemplo
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul')
# Obs.: Os parâmetros *args e **kwargs não são obrigatórios


# Exemplo mais complexo
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(geek="Python"))
print(cumprimento_especial(geek="Oi!"))


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(34, 'William', 4, 5, 3, solteiro=True, python=True)


# Entendo a importância da ordem dos parâmetros
def mostra_info(a, b, *args, intrutor='Geek', **kwargs):
    return [a, b, args, intrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Desempacotar com **kwargs
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'William', 'sobrenome': 'Círico'}
print(mostra_nomes(**nomes))


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
soma_multiplos_numeros(*lista)

