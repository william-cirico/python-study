# 1)
def funcao1():
    print("Função 1")


def funcao2(funcao):
    return funcao()


funcao2(funcao1)


# 2)
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f"Oi {nome}"


def saudacao(nome, saudacao):
    return f"{saudacao} {nome}"


print(mestre(fala_oi, "William"))
print(mestre(saudacao, "William", saudacao="Olá"))
