"""
Reversed

* A função reverse só funciona em listas
* A função reversed funciona em qualquer iterável
- Sua função é inverter o iterável
"""
# Exemplos
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
conjunto = {1, 2, 3, 4, 5}

print(list(reversed(lista)))
print(tuple(reversed(tupla)))
# print(reversed(conjunto))  # Conjunto não tem ordem definida

# Iterando sobre reversed
for letra in reversed("Geek University"):
    print(letra, end='')  # end='' retira a quebra de linha

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Slice de strings
print('Geek University'[::-1])

# Loop reverso
for n in reversed(range(0, 10)):
    print(n)

for n in range(9, -1, -1):
    print(n)