"""
Escrevendo em arquivos CSV

reader() -> writer()
writerow() -> Escreve uma linha
DictReader() -> DictWriter()
"""
from csv import writer, DictWriter

# writer
"""
with open("filmes.csv", "w", encoding="utf-8") as arquivo:
    escritor_csv = writer(arquivo)
    escritor_csv.writerow(["Título", "Gênero", "Duração"])
    filme = None
    while filme != "sair":
        filme = input("Informe o nome do filme: ")
        if filme != "sair":
            genero = input("Informe o gênero: ")
            duracao = input("Informe a duração (em minutos): ")
            escritor_csv.writerow([filme, genero, duracao])
"""

# DictWriter
with open("filmes.csv", "w", encoding="utf-8") as arquivo:
    cabecalho = ["Título", "Gênero", "Duração"]
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != "sair":
        filme = input("Informe o nome do filme: ")
        if filme != "sair":
            genero = input("Informe o gênero: ")
            duracao = input("Informe a duração (em minutos): ")
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})



