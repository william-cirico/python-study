import csv

with open("arquivos.csv", "r", encoding="utf-8") as arquivo:
    dados = csv.DictReader(arquivo)

    for dado in dados:
        print(dado["Nome"], dado["Sobrenome"], dado["E-mail"], dado["Telefone"])

with open("arquivos.csv", "r", encoding="utf-8") as arquivo:
    dados = csv.reader(arquivo)
    next(dados)

    for dado in dados:
        print(dado)

with open("arquivos.csv", "r") as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]

with open("arquivos2.csv", "w") as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=",",
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = list(dados[0].keys())
    escreve.writerow([
        chaves[0],
        chaves[1],
        chaves[2],
        chaves[3],
    ])

    for dado in dados:
        escreve.writerow([
            dado["Nome"],
            dado["Sobrenome"],
            dado["E-mail"],
            dado["Telefone"]
        ])