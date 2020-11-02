"""
Loop while

Forma geral
while expressão_booleana:
    //Execução do loop

Vai repetir enquanto a expressão for verdadeira
"""

num = 10
while num > 0:
    print(num)
    num -= 2

# Exemplo 1
num = 1
while num < 10:
    print(num)
    num += 1

# Exemplo 2
resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')

