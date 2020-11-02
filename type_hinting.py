def cumprimentar(nome: str) -> str:
    return f"Olá, {nome}"


print(cumprimentar("Geek"))


def cabecalho(texto, alinhamento=True):
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()}".center(50, "#")


print(cabecalho("geek univserity"))
print(cabecalho("geek university", alinhamento=False))


def cabecalho_modificado(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()}".center(50, "#")


print(cabecalho_modificado("geek univserity"))
print(cabecalho_modificado("geek university", alinhamento=False))
