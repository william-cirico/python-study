"""
:s - Texto
:d - Inteiros
:f - Números
:.(NUMERO)f - Quantidade de casas decimais
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO)

> - Esquerda
< - Direita
^ - Centro
"""
num = 1
string = "OO II"
print(f"{num:0>10}")
print(f"{num:0<10}")
print(f"{string:-^11}")
print(f"{num:.2f}")