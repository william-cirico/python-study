from itertools import groupby, tee

alunos = [
    {"nome": "Luiz", "nota": "B"},
    {"nome": "Letícia", "nota": "A"},
    {"nome": "Fabrício", "nota": "C"},
    {"nome": "Rosemary", "nota": "B"},
    {"nome": "Joana", "nota": "B"},
    {"nome": "João", "nota": "C"},
    {"nome": "Eduardo", "nota": "D"},
    {"nome": "André", "nota": "C"},
    {"nome": "Anderson", "nota": "B"},
    {"nome": "José", "nota": "A"},
    {"nome": "Pedro", "nota": "D"},
]

# Para o groupby funcionar é necessário ordenar os dados
ordenacao = lambda aluno: aluno['nota']
alunos.sort(key=ordenacao)
alunos_agrupados = groupby(alunos, ordenacao)
for agrupamento, valores_agrupados in alunos_agrupados:
    it1, it2 = tee(valores_agrupados)  # Fiz duas cópias do iterator

    print(f"Agrupamento: {agrupamento}")

    for aluno in it1:
        print(aluno)

    quantidade = len(list(it2))
    print(f"Quantidade de alunos: {quantidade}")
    print()
