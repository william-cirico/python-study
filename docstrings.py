"""
Documentando funções com Docstrings

Obs.: Podemos ter acesso à documentação de uma função em Python
utilizando a propriedade especial __doc__ ou com a função help()
"""


# Exemplos
def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    print(diz_oi())
    return 'Oi!'


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou este elevado à 'potencia' informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2
    :return:
    """