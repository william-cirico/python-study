"""
Bloco try/except

- Utilizamos o bloco try/except para tratar erros que podem ocorrer no código.

Sintaxe:

try:
    //execução problemática
except:
    // o que deve ser feito em caso de problema
"""

# Exemplo 1
try:
    geek()
except:
    print("Deu algum problema")

# Exemplo 2
try:
    len(5)
except:
    print("Deu algum problema")

# Exemplo 3 - Tratando um erro específico
try:
    geek()
except NameError as err:
    print(f"Você está utilizando uma função inexistente: {err}")

# Exemplo 4
try:
    len(5)
except NameError as erra:
    print(f"Deu NameError: {erra}")
except TypeError as errb:
    print(f"Deu TypeError: {errb}")


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "Geek"}
print(pega_valor(dic, "nome"))
print(pega_valor(dic, "robô"))
