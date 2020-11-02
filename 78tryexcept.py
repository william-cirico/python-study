def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


numero = converte_numero(input("Digite um valor: "))
if numero is None:
    print("Erro: isso não é um número")
else:
    print(numero * 5)