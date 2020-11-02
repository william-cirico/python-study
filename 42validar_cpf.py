def limpar_formatacao(cpf):
    lista = [".", "-", " "]
    for item in lista:
        cpf = cpf.replace(item, "")
    return cpf


def gerar_numeros(cpf):
    soma = 0
    for c, i in zip(cpf, range(10, 1, -1)):
        soma += int(c) * i

    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0

    cpf = f"{cpf}{digito1}"
    soma = 0
    for c, i in zip(cpf, range(11, 1, -1)):
        soma += int(c) * i

    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    return f"{digito1}{digito2}"


def gerar_novo_cpf(cpf):
    cpf = cpf[:-2]
    novo_cpf = cpf + gerar_numeros(cpf)
    return novo_cpf


def validar_cpf(cpf):
    cpf_formatado = limpar_formatacao(cpf)
    if cpf_formatado == gerar_novo_cpf(cpf_formatado):
        print(f"O CPF {cpf} é válido!")
    else:
        print(f"O CPF {cpf} é inválido!")


cpf = input("Digite seu CPF: ")
validar_cpf(cpf)





