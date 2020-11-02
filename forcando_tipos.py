"""
Forçando tipos de dados com decoradores

Zip
A = (1, 3, 5)
B = (2, 4, 6)
C = zip(a,b)

C = (1, 2) , (3, 4), (5, 6)
"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converter
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('Geek', '3')


@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)


dividir('1', 5)
