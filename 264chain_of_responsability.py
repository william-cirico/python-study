"""
Chain of responsability (COR) é um padrão comportamental que tem a intenção de
evitar o acoplamento do remetente de uma solicitação ao seu receptor, ao dar
a mais de um objeto a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação ao longo da cadeia até
que um objeto a trate.
"""


# Implementando com funções
def handler_abc(letter: str) -> str:
    letters = ['A', 'B', 'C']

    if letter in letters:
        return f'handler_abc: conseguiu tratar o valor {letter}'
    return handler_def(letter)


def handler_def(letter: str) -> str:
    letters = ['D', 'E', 'F']

    if letter in letters:
        return f'handler_def: conseguiu tratar o valor {letter}'
    return handler_unsolved(letter)


def handler_unsolved(letter: str) -> str:
    return f'handler_unsolved: não sei tratar {letter}'


if __name__ == '__main__':
    print(handler_abc('D'))
    print(handler_abc('Z'))

