import os
import shutil

cursopython_path = r'C:\Users\William\PycharmProjects\cursopython'
guppe_path = r'C:\Users\William\PycharmProjects\guppe'
pythonstudy_path = r'C:\Users\William\Desktop\python-study'


# Criando a pasta de destino
try:
    os.mkdir(pythonstudy_path)
except FileExistsError:
    print(f'O Path {pythonstudy_path} já existe.')


# Copiando os arquivos .py
def file_copy(old_dir_name, new_dir_name):
    for dir_path, dir_names, file_names in os.walk(old_dir_name):
        for file_name in file_names:
            if '.py' in file_name:
                old_file_path = os.path.join(dir_path, file_name)
                new_file_path = os.path.join(new_dir_name, file_name)
                shutil.copy(old_file_path, new_file_path)


file_copy(cursopython_path, pythonstudy_path)
file_copy(guppe_path, pythonstudy_path)