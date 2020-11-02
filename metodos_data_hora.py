"""
Métodos de Data e Hora
"""
import datetime
from textblob import TextBlob
agora = datetime.datetime.now() # Pode-se especificar o timezone
hoje = datetime.datetime.today()
print(agora)
print(hoje)

# Mudanças ocorrendo à meia-noite | combine()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)

# Encontrar o dia da semana | weekday()
# 0 - Segunda-Feira
# 1 - Terça-Feira
# 2 - Quarta-Feira
# 3 - Quinta-Feira
# 4 - Sexta-Feira
# 5 - Sábado
# 6 - Domingo
print(manutencao.weekday())

nascimento = input("Qual sua data de nascimento (dd/mm/yyyy): ")
nascimento = nascimento.split("/")
nascimento = datetime.datetime(year=int(nascimento[2]), month=int(nascimento[1]), day=int(nascimento[0]))

if nascimento.weekday() == 0:
    print("Você nasceu em uma segunda-feira")
elif nascimento.weekday() == 1:
    print("Você nasceu em uma terça-feira")
elif nascimento.weekday() == 2:
    print("Você nasceu em uma quarta-feira")
elif nascimento.weekday() == 3:
    print("Você nasceu em uma quinta-feira")
elif nascimento.weekday() == 4:
    print("Você nasceu em uma sexta-feira")
elif nascimento.weekday() == 5:
    print("Você nasceu em um sábado")
elif nascimento.weekday() == 6:
    print("Você nasceu em um domingo")

# Formatando datas/horas com strftime() - String Format Time
hoje = datetime.datetime.today()
print(hoje)
hoje_formatado = hoje.strftime("%d/%m/%Y")
print(hoje_formatado)


def formata_data(data):
    if data.month == 1:
        return f"{data.day} de Janeiro de {data.year}"
    elif data.month == 2:
        return f"{data.day} de Fevereiro de {data.year}"
    elif data.month == 3:
        return f"{data.day} de Março de {data.year}"
    elif data.month == 4:
        return f"{data.day} de Abril de {data.year}"
    elif data.month == 5:
        return f"{data.day} de Maio de {data.year}"
    elif data.month == 6:
        return f"{data.day} de Junho de {data.year}"
    elif data.month == 7:
        return f"{data.day} de Julho de {data.year}"
    elif data.month == 8:
        return f"{data.day} de Agosto de {data.year}"
    elif data.month == 9:
        return f"{data.day} de Setembro de {data.year}"
    elif data.month == 10:
        return f"{data.day} de Outubro de {data.year}"
    elif data.month == 11:
        return f"{data.day} de Novembro de {data.year}"
    elif data.month == 12:
        return f"{data.day} de Dezembro de {data.year}"


def formata_data2(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


print(formata_data(hoje))
print(formata_data(hoje))

nascimento = datetime.datetime.strptime("10/04/1998", "%d/%m/%Y")
print(nascimento)

# Somente a hora
almoco = datetime.time(12, 30, 0)
print(almoco)

# Marcando tempo de execução do nosso código com timeit
import timeit, functools

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)


# Testando se a função é eficiente
def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10000))

