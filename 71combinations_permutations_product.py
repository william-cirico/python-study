from itertools import combinations, permutations, product

pessoas = ["William", "Luiz", "André", "Eduardo", "Letícia", "Fabrício", "Rose"]

# Combinations (Ordem não importa - Não repete combinações)
for grupo in combinations(pessoas, 2):
    print(grupo)

# Permutations (Ordem importa - Repete combinações)
for grupo in permutations(pessoas, 2):
    print(grupo)

# Produto (Ordem importa - Repete valores únicos e combinações)
for grupo in product(pessoas, repeat=2):
    print(grupo)
