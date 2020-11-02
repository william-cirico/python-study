from itertools import zip_longest
cidades = ["São Paulo", "Belo Horizonte", "Salvador", "Florianópolis"]
estados = ["SP", "MG", "BA"]

# Utilizando zip (Itera até o último elemento da menor lista)
cidades_estados = zip(cidades, estados)
print(list(cidades_estados))

# Utilizando zip_longest (Itera até o último elemento da maior lista)
cidades_estados = zip_longest(cidades, estados)  # Preenche com None
print(list(cidades_estados))
