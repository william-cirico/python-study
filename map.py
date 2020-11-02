"""
Map

Com map, fazemos mapeamento de valores para função;
"""
import math


def area(r):
    """Calcula a área de um círculo com raio 'r'"""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma utilizando map
areas = map(area, raios)  # Retorna em tipo map por isso é necessário converter para list
print(list(areas))

# Forma com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))
# Obs.: Após utilizar a função map() ele se auto-destrói.

# Outro exemplo
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26)]
print(cidades)
# f = 9/5 * c + 32

# Lambda
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))

