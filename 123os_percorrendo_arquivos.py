import os


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < mega:
        tamanho /= kilo
        texto = "K"
    elif tamanho < giga:
        tamanho /= mega
        texto = "M"
    elif tamanho < tera:
        tamanho /= giga
        texto = "G"
    elif tamanho < peta:
        tamanho /= tera
        texto = "T"
    else:
        tamanho /= peta
        texto = "P"

    tamanho = round(tamanho, 2)
    return f"{tamanho}{texto}"


caminho_procura = input("Digite um caminho: ")
termo_procura = input("Digite um termo: ")

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho_arquivo = os.path.getsize(caminho_completo)

                print()
                print("Encontrei o arquivo: ", arquivo)
                print("Caminho: ", caminho_completo)
                print("Nome: ", nome_arquivo)
                print("Extensão: ", ext_arquivo)
                print("Tamanho: ", formata_tamanho(tamanho_arquivo))
            except PermissionError as e:
                print("Sem premissões")
            except FileNotFoundError as e:
                print("Arquivo não encontrado")
            except Exception as e:
                print("Erro desconhecido: ", e)





