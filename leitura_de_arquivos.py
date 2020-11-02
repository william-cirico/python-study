"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função open()

open() -> retorna um _io.TextIOWrapper
"""
# Exemplo
arquivo = open('texto.txt')
print(arquivo)
print(type(arquivo))

# Para ler o conteúdo de um arquivo:
print(arquivo.read())
