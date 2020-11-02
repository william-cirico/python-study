"""
Debuggando com PDB

PDB -> Python Debugger
"""


# Utilizar o print para debugar é uma má-prática
def dividir(a, b):
    print(f'a={a} b={b}')
    try:
        return a / b
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um problema: {err}"


print(dividir(4, 0))

# Exemplo com o PDB

"""
Comandos PDB:

l - listar onde estamos no código
n - próxima linha
p - imprime variável
c - continua a execução
"""

nome = "William"
sobrenome = "Círico"
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = "Programação em Python: Essencial"
final = nome_completo + " faz o curso " + curso
print(final)

# A partir do Python 3.7 é possível utilizar breakpoint()
nome = "William"
sobrenome = "Círico"
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = "Programação em Python: Essencial"
final = nome_completo + " faz o curso " + curso
print(final)
