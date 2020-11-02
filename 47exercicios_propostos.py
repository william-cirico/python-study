# 1)
def saudacao(s, nome):
    print(f"{s} {nome}")


saudacao("Olá", "William")


# 2)
def soma(*args):
    print(sum(args))


soma(10, 20)


# 3)
def calcula_aumento(valor, percentual):
    novo_valor = valor + (valor * (percentual / 100))
    return novo_valor


print(calcula_aumento(1000, 10))


# 4)
def fizz_buzz(valor):
    if valor % 2 == 0:
        return "fizz"
    elif valor % 5 == 0 and valor % 3 == 0:
        return "FizzBuzz"
    elif valor % 5 == 0:
        return "buzz"
    else:
        return valor


print(fizz_buzz(13))
