"""
Loop for

Loop -> Estrutura de repetição
for -> Uma dessas estruturas

# C
for (int i = 0; i < 10; i++){
    //execução do loop
}

# Python
for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou valores iteráveis

Exemplos de iteráveis:
- String
    nome = "Geek University"

- Lista
    lista = [1, 3, 5, 7, 9]

- Range
    Obs.: O valor final não é incluído!! (1 .. 9)
    numeros = range(1, 10)
"""

nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# 1) Exemplo de for (Iterando em uma string)
for letra in nome:
    print(letra)

# 2) Exemplo de for (Iterando em uma lista)
for numero in lista:
    print(numero)

# 3) Exemplo de for (Iterando em um range)
for numero in numeros:
    print(numero)

# 4) Enumerate
for indice, letra in enumerate(nome):
    print((nome[indice]))

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):  # Usar _ Quando não precisa do valor
    print(letra)

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor '))
    soma = soma + num
print(f'A soma é {soma}')

for letra in nome:
    print(letra, end="")

# Tabela Emoji Unicode: https://apps.timwhitlock.info/emoji/tables/unicode

# Original: U+1F60D
# Modificado: U0001F60D

emoji = 'U0001F60D'
for num in range(1, 11):
    print("\U0001F60D" * num)

