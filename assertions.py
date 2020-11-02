"""
Assertions (Asserções)

Utilizamos assert em uma expressão que queremos checar se é válida ou não.
V -> None
F -> AssertionError

# Se um programa for executado com o parâmetro -O, todas as assertions são ignoradas.
"""
# assert 4 == 2, "Não é igual"


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, "Ambos números precisam ser positivos"
    return a + b


#ret = soma_numeros_positivos(-2, 4)
#print(ret)


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], "A comida precisa ser fast food"
    return f"Eu estou comendo {comida}"


comida = input("Informe a comida: ")
print(comer_fast_food(comida))

