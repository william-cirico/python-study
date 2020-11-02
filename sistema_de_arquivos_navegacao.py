"""
Sistema de Arquivos e Navegação

Módulo os -> Operating System
"""
import os
import sys

# Patch atual
print(os.getcwd())

# Mudar o diretório
os.chdir("..")
print(os.getcwd())

print(os.path.isabs('/home/geek/'))

# Podemos identificar o sistema operacional
print(os.name)

# Mais detalhes sobre o sistema operacional
print(sys.platform)

#res = os.path.join(os.getcwd(), 'geek', 'university')
#os.chdir(res)
print((os.getcwd()))

# Para listar diretórios
print(os.listdir())
print(len(os.listdir('C://')))

# Para listar diretórios detalhadamente
print(list(os.scandir('C://')))
arquivos = list(os.scandir("C://"))
print(dir(arquivos[0]))
print(arquivos[0].inode)
print(arquivos[0].is_dir)
print(arquivos[0].is_file)
print(arquivos[0].is_symlink)
print(arquivos[0].name)
print(arquivos[0].stat())

# Forma correta de utilização
scanner = os.scandir()
arquivos = list(scanner)
scanner.close()
