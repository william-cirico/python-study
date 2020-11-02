"""
Try / Except / Else / Finally

Quando tratar código:

Toda entrada de dados deve ser tratada

- O finally, geralmente é utilizado para fechar ou desalocar
recursos
"""
try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor incorreto")
else:
    print(f'Você digitou {num}')

# Exemplo com finally
try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor incorreto")
else:
    print(f"Você digitou {num}")
finally:  # Sempre executado com exceção ou não
    print("Executando o finally")


# Exemplo mais complexo ERRADO
def dividir(a, b):
    return a / b


num1 = int(input("Informe o primeiro número: "))
try:
    num2 = int(input("Informe o segundo número: "))
except ValueError:
    print("O valor precisa ser númerico")

try:
    print(dividir(num1, num2))
except NameError:
    print("Valor incorreto")


# Exemplo mais complexo CERTO
def dividir_certo(a, b):
    try:
        return a / b
    except ValueError:
        return "Valor Incorreto"
    except ZeroDivisionError:
        return "Não é possível dividir por zero"


num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))


# Exemplo mais complexo (Semi-genérico)
def dividir_generico(a, b):
    try:
        return a / b
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um problema {err}"


num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
