# É possível formatar strings das seguintes formas:
nome = "William Círico"
idade = 20
peso = 70.31287418293472

print("Nome: ", nome, "Idade: ", idade, "Peso: ", peso)
print("Nome: {0} Idade: {1} Peso: {2}".format(nome, idade, peso))
print("Nome: {n} Idade: {i} Peso: {p}".format(n=nome, i=idade, p=peso))
print(f"Nome: {nome} Idade: {idade} Peso: {peso:.2f}")