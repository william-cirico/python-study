from random import randint


def formatar_cnpj(c):
    lista = [".", "/", "-", " "]
    for item in lista:
        c = c.replace(item, "")

    return c


def gerar_digitos(c):
    soma = 0
    for digito, indice in zip(c, range(5, 1, -1)):
        soma += int(digito) * indice

    for digito, indice in zip(c[4:], range(9, 1, -1)):
        soma += int(digito) * indice

    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0

    c = f"{c}{digito1}"
    soma = 0

    for digito, indice in zip(c, range(6, 1, -1)):
        soma += int(digito) * indice

    for digito, indice in zip(c[5:], range(9, 1, -1)):
        soma += int(digito) * indice

    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    c = f"{c}{digito2}"

    return c


def validar_cnpj(c):
    cnpj_f = formatar_cnpj(c)
    cnpj_formatado = cnpj_f[:-2]
    cnpj_validado = gerar_digitos(cnpj_formatado)
    if cnpj_validado == cnpj_f:
        print(f"O cnpj: {c} é válido!")
    else:
        print(f"O cnpj: {c} é inválido!")


def gerar_cnpj():
    primeiro_bloco = randint(10, 99)
    segundo_bloco = randint(100, 999)
    terceiro_bloco = randint(100, 999)
    quarto_bloco = "0001"

    inicio_cnpj = f"{primeiro_bloco}{segundo_bloco}{terceiro_bloco}{quarto_bloco}"
    novo_cnpj = gerar_digitos(inicio_cnpj)
    print(novo_cnpj)


cnpj = input("Digite seu CNPJ: ")
validar_cnpj(cnpj)
validar_cnpj(gerar_cnpj())
