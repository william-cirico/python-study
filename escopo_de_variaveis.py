"""
Escopo de variáveis

2 casos de escopo:

1 - Variaveis globais:
    - Variáveis globais são reconhecidas em toda o programa.
2 - Variaveis locais:
    - Seu reconhecimento está limitado ao bloco onde foi declarado.

Python é uma linguagem de tipagem dinâmica.

Exemplo em C:
int numero = 42;

Exemplo em Python:
numero = 42
"""

numero = 42  # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = 5
if numero > 10:
    novo = numero + 10  # 'novo' é uma variável local

print(novo)
