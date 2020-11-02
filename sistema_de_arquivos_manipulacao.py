"""
Sistema de Arquivos - Manipulação
"""
import os
# Descobrindo se um arquivo ou diretório existe:
print(os.path.exists("frutas.txt"))

# Criando arquivos
open('aquivo-teste.txt', 'w').close()

# Outra forma
with open('arquivo-teste.txt', 'w') as arquivo:
    pass  # Evitar erros de identação

# Melhor forma
os.mknod('arquivo-teste.txt')
# Obs.: Se o arquivo já existir -> FileExistsError

# Criar diretórios (um a um)
os.mkdir('templates')
# Obs.: Se o diretório já existir -> FileExistsError

# Criar múltiplos diretórios
os.mkdirs('templates/geek/university')

# Ignorando o erro de diretório já existente
os.mkdirs('templates/geek/university', exist_ok=True)

# Renomear arquivos e diretórios
os.rename('arquivo-teste.txt', 'arquivoteste.txt')
# Obs.: Se o diretório não exister teremos um FileNotFoundError

# Deletando arquivos
# Obs.: Os arquivos deletados não vão para lixeira, eles somem.
os.remove('arquivo-teste.txt')

# Deletando diretórios
os.rmdir('xazan')
# Obs.: Se o diretório tiver qualquer conteúdo teremos um OSError

# Deletando uma árvore de arquivos
for arquivo in os.scandir('xazan'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Deletando uma árvore de diretórios vazios
os.removedirs('xazan/abc/dsdasad')

# Para enviar para lixeira utilizar o pacote send2trash
# pip install Send2Trash
from send2trash import send2trash
send2trash('arquivo-teste.txt')

# Trabalhando com arquivos e diretórios temporários
import tempfile

with tempfile.TemporaryDirectory as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Criando um arquivo temporário
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())
# Obs.: Em arquivos temporários só conseguimos escrever bits, por isso utilizamos o 'b'

# Saber o patch do arquivo
with tempfile.NamedTemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    print(tmp.name)
    input()

