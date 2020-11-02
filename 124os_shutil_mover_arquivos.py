import os
import shutil

caminho_original = r"C:\Users\William\Desktop\teste1"
caminho_novo = r"C:\Users\William\Desktop\teste2"

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f"Pastas {caminho_novo} já existe")

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if ".txt" in file:
            shutil.move(old_file_path, new_file_path)
            print(f"Arquivo {file} movido com sucesso!")

        os.remove(new_file_path)
