"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Vírgula

dados.gov.br/dataset -> Site com arquivos em csv

A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;
"""
from csv import reader
from csv import DictReader

# Forma Errada
with open("lutadores.csv", encoding="utf-8") as arquivo:
    dados = arquivo.read()
    print(dados)
    dados = dados.split(",")[3:]
    print(dados)


# Forma Correta (reader)
with open("lutadores.csv", encoding="utf-8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        print(f"{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]}")

# Forma Correta (DictReader)
with open("lutadores.csv", encoding="utf-8") as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=",")
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")