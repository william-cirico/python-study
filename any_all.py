"""
Any e All

all(): Retorna True se todos os elementos do iterável são verdadeiros
ou se o iterável está vazio

any(): Retorna True se qualquer elemento iterável for verdadeiro.
"""
# Exemplo all()
print(all([0, 1, 2, 3, 4]))   # Todos os números são verdadeiros? False
print(all([1, 2, 3, 4]))   # Todos os números são verdadeiros? True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

# Exemplo any()
print(any([0, 1, 2, 3, 4]))  # True
print(any([num for num in [4, 2, 19, 6, 8, 9] if num % 2 == 0]))
