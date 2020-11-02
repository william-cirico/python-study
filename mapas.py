"""
Mapas -> Conhecidos em Python como dicionários
"""

receita = {"jan": 100, "fev": 250, "mar": 400}

# Iterar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])\

for chave in receita:
    print(f'Em {chave} recebi: {receita[chave]}')

print(receita.keys())

for chave in receita.keys():  # Recomendado
    print(receita[chave])

# Acessando os valores
print(receita)

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'chave: {chave} e valor: {valor}')

# Soma, Valor máximo, valor mínimo e tamnho
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
