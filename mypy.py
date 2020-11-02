# mypy mypy.py
def cabecalho_modificado(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()}".center(50, "#")


print(cabecalho_modificado("geek univserity"))
print(cabecalho_modificado("geek university", alinhamento="Dale"))
