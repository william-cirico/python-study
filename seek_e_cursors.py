"""
Seek e Cursors

seek() -> É utilizado para movimentar o cursor pelo arquivo

Passos para trabalhar com um arquivo:
1 - Abrir o arquivo
2 - Processar o arquivo
3 - Fechar o arquivo
"""
# 1)
arquivo = open('texto.txt')

# 2)
print(arquivo.read())
arquivo.seek(0)
print(arquivo.read(5))

# readline() -> Função que lê o arquivo linha a linha
arquivo.seek(0)
print(arquivo.readline())

# readlines()
arquivo.seek(0)
print(arquivo.readlines())
arquivo.seek(0)
print(len(arquivo.readlines()))
print(arquivo.close())  # Verifica se o arquivo está aberto ou fechado


# 3)
arquivo.close()
