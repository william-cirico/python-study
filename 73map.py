from dados import produtos, pessoas, lista


def main():
    # Com map
    nova_lista_map = map(lambda x: x * 2, lista)

    # Com list comprehension
    nova_lista = [x * 2 for x in lista]

    print(list(nova_lista_map))
    print(nova_lista)

    # ----

    precos = map(lambda p: p['preco'], produtos)
    print(list(precos))

    precos_aumento = map(aumenta_preco, produtos)
    print(list(precos_aumento))


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


if __name__ == "__main__":
    main()
