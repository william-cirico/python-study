with open("abc.txt", "w+") as arquivo:
    arquivo.write("Linha1\n")
    arquivo.write("Linha2\n")
    arquivo.write("Linha3\n")
    arquivo.seek(0, 0)
    print(arquivo.read())
    print("############")
    arquivo.seek(0, 0)
    print(arquivo.readline(), end="")
    print(arquivo.readline(), end="")
    arquivo.seek(0, 0)
    for linha in arquivo:
        print(linha, end="")

# 'r' - Abre para leitura (padrão)
# 'w' - Abre para escrita
# 'x' - Abre exclusivamente para criação (falha se o arquivo já existe)
# 'a' - Abre para escrita (adicionando ao final do arquivo)
# 'b' - Modo binário
# 't' - Modo text (padrão)
# '+' - Abre para atualização (leitura e escrita)
