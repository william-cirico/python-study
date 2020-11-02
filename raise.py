"""
Levantando os próprios erros com raise

raise - Lança exceções

- Usado para criar nossas próprias exceções e mensagens
de erro.

raise TipoDoErro('Mensagem de erro')

Obs.: O raise finaliza a função.
"""


# Exemplo
def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor: {cor}')


colore('Geek', 4)
