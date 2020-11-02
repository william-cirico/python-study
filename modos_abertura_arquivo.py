"""
Modos de abertura de arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita - somente se o arquivo não existir
a -> Abre para escrita - adicionando o conteúdo ao final do arquivo
+ -+> Abre para o modo de atualização: Leitura e escrita. (controle do cursor)
"""
try:
    with('texto.txt', 'x') as texto:
        texto.write('Teste de conteúdo')
except FileExistsError:
    print('Arquivo já existe!')

with open('frutas.txt', 'a') as frutas:
    while True:
        fruta = input("Informe uma fruta ou digite sair: ")
        if fruta != 'sair':
            frutas.write(fruta + ", ")
        else:
            break
