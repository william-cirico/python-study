"""
StringIO

- Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    * Permissão de Leitura
    * Permissão de Escrita

StringIO -> Utilizado para ler e criar arquivos em memória.
"""
# Primeiro fazemos o import
from io import StringIO

mensagem = "Este é apenas uma string normal"

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')
print(arquivo.read())
arquivo.write('Outro texto')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()
