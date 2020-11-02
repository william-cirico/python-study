"""
Escrevendo em arquivos

# Obs.: Ao abrir um arquivo para leitura, não é possível escrever nele
"""
# Exemplo de escrita ("w")
with open('texto.txt', 'w') as arquivo:
    arquivo.write("Escrever dados em arquivo é muito fácil \n")
    arquivo.write("Podemos colocar quantas linhas quisermos \n")
    arquivo.write("Esta é a última linha")

with open('texto.txt', 'w') as arquivo:
    arquivo.write(10 * (("Xablau" * 100) + "\n"))

with open('frutas.txt', 'w') as frutas:
    while True:
        fruta = input("Informe uma fruta ou digite sair: ")
        if fruta != 'sair':
            frutas.write(fruta + ", ")
        else:
            break
