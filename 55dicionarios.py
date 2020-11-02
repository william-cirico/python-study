clientes = {
    "cliente1": {
        "nome": "William",
        "sobrenome": "Círico"
    },
    "cliente2": {
        "nome": "João",
        "sobrenome": "Moreira"
    },
    "cliente3": {
        "nome": "Maria",
        "sobrenome": "Moreira"
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f"Exibindo {clientes_k}")
    for dados_k, dados_v in clientes_v.items():
        print(f"\t{dados_k} = {dados_v}")

perguntas = {
    "Pergunta 1": {
        "pergunta": "Quanto é 2+2?",
        "respostas": {"a": "1", "b": "4", "c": "5", },
        "resposta_certa": "b",
    },
    "Pergunta 2": {
        "pergunta": "Quanto é 5*5?",
        "respostas": {"a": "25", "b": "10", "c": "6", },
        "resposta_certa": "a",
    },
    "Pergunta 3": {
        "pergunta": "Quanto é 100-50?",
        "respostas": {"a": "30", "b": "43", "c": "50", },
        "resposta_certa": "c",
    },
}

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")

    for rk, rv in pv['respostas'].items():
        print(f"\t{rk}) {rv}")

    resposta_usuario = input("Sua resposta: ")

    if resposta_usuario == pv['resposta_certa']:
        print("Acertou!!")
        respostas_certas += 1
    else:
        print("Errouuu!!")
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100
print(f"Voce acertou: {respostas_certas} perguntas")
print(f"Porcentagem de acerto: {porcentagem_acerto:.2f}%")
