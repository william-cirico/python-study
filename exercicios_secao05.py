from math import sqrt, log10
"""
# 1)
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print("Números são iguais")

# 2)
num = int(input("Digite um número: "))
if num > 0:
    print(sqrt(num))
else:
    print("Número inválido")
    
# 3)
num = float(input("Digite um número: "))
if num > 0:
    print(sqrt(num))
else:
    print(num ** 2)

# 4)
num = float(input("Digite um número: "))
if num > 0:
    print(sqrt(num))
    print(num ** 2)

# 5)
num = int(input("Digite um número: "))
if num % 2:
    print("Número é ímpar")
else:
    print("Número é par")

# 6)
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
if num1 > num2:
    print(f"Maior: {num1} Diferença: {num1 - num2}")
elif num1 < num2:
    print(f"Maior: {num2} Diferença: {num2 - num1}")
else:
    print("Números são iguais")

# 7)
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print("Números são iguais")

# 8)
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
if (n1 in range(0, 11)) and (n2 in range(0, 11)):
    print(f"{(n1 + n2) / 2}")
else:
    print("Notas inválidas")

# 9)
salario = float(input("Digite o salário: "))
prestacao = float(input("Digite o valor da prestação: "))
if salario * 0.2 < prestacao:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")

# 10)
sexo = input("Digite seu sexo: ")
altura = float(input("Digite sua altura: "))
if sexo == "M" or sexo == "m":
    peso_ideal = 72.7 * altura - 58
    print(peso_ideal)
elif sexo == "F" or sexo == "f":
    peso_ideal = 62.1 * altura - 44.7
    print(peso_ideal)
else:
    print("Sexo Inválido")

# 11)
num = int(input("Digite um número: "))
if num > 0:
    soma = 0
    while num / 10:
        soma += num % 10
        num //= 10
    print(soma)
else:
    print("Número inválido")

# 12)
num = int(input("Digite um número: "))
if num > 0:
    num = log10(num)
    print(num)
else:
    print("Número Inválido")

# 13)
notas = []
for nota in range(1, 4):
    notas.append(float(input(f"Digite a {nota} nota: ")))
media = (notas[0] + notas[1] + (notas[2] * 2)) / 4
print(media)
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")

# 14)
notas = []
for nota in range(1, 4):
    notas.append(float(input(f"Digite a {nota} nota: ")))
media = ((notas[0] * 2) + (notas[1] * 3) + (notas[2] * 5)) / 10
print(media)
if 0 < media < 3:
    print("Reprovado")
elif 3 <= media < 5:
    print("Recuperação")
elif 5 <= media <= 10:
    print("Aprovado")
else:
    print("Média Inválida")

# 15)
dia = int(input("Digite o dia da semana (1-7): "))
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sábado")
else:
    print("Dia inválido")

# 16)
mes = int(input("Digite o mês do ano (1-7): "))
if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Mês Inválido")

# 17)
base1 = float(input("Digite o valor de uma base: "))
base2 = float(input("Digite o valor de outra base: "))
altura = float(input("Digite a altura do trapézio: "))
if base1 > 0 and base2 > 0:
    area = ((base1 + base2) * altura) / 2
else:
    print("Bases inválidas")

# 18)
num1 = int("Digite um número: ")
num2 = int("Digite outro número: ")
opcao = int(input(print(""
Operações Matemáticas:

1 - Soma
2 - Subração
3 - Multiplicação
4 - Divisão

Opção Escolhida: 
"")))
if opcao == 1:
    print(f"{num1 + num2}")
elif opcao == 2:
    print(f"{num1} - {num2}")
elif opcao == 3:
    print(f"{num1} * {num2}")
elif opcao == 4:
    print(f"{num1} / {num2}")

# 19)
num = int(input("Digite um número: "))
if num % 3 == 0 and num % 5 != 0:
    print(f"O número {num} é divisível apenas por 3")
elif num % 5 == 0 and num % 3 != 0:
    print(f"O número {num} é divisível apenas por 5")
elif num % 5 == 0 and num % 3 == 0:
    print(f"O número {num} é divisível por 3 e 5")
else:
    print(f"O número {num} não é divisível por 3 e 5")

# 20)
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

if a < (b + c) and b < (a + c) and c < (a + b):
    if a == b and a == c:
        print("Triângulo Esquilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não é um triângulo")

# 21)
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
opcao = int(input("
Escolha a opção:
1 - Soma de 2 números;
2 - Diferença entre 2 números (maior pelo maior);
3 - Produto entre 2 números;
4 - Divisião entre 2 números (o denominador não pode ser zero).
Opção: 
"))
if opcao == 1:
    soma = num1 + num2
    print(f"Soma: {soma}")
elif opcao == 2:
    sub = num1 - num2
    print(f"Subtração: {sub}")
elif opcao == 3:
    multi = num1 * num2
    print(f"Multiplicação: {multi}")
elif opcao == 4:
    try:
        divisao = num1 / num2
    except ZeroDivisionError:
        print("Divisão por Zero!")
else:
    print("Opção Inválida")

# 22)
idade = int(input("Digite a idade: "))
tempo_servico = int(input("Digite o tempo de serviço: "))
if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
    print("Pode se aposentar!")
else:
    print("Não pode se aposentar")
"""
# 23)
ano = int(input("Digite um ano: "))
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print(f"{ano} é bissexto")
else:
    print(f"{ano} não é bissexto")

# 24)
valor = float(input("Digite o valor do produto: "))
estado = input("""
Escolha o estado de destino:

1 - MG
2 - SP
3 - RJ
4 - MJ
""")
if estado == "1":
    valor_final = valor + (valor * (7 / 100))
    print(f"Preço final: {valor_final}")
elif estado == "2":
    valor_final = valor + (valor * (12 / 100))
    print(f"Preço final: {valor_final}")
elif estado == "3":
    valor_final = valor + (valor * (15 / 100))
    print(f"Preço final: {valor_final}")
elif estado == "4":
    valor_final = valor + (valor * (8 / 100))
    print(f"Preço final: {valor_final}")
else:
    print("Estado Inválido")

# 25)
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print("Não existe raiz")
elif delta == 0:
    print("Raiz única")
else:
    x1 = (-b + sqrt(delta)) / 2 * a
    x2 = (-b - sqrt(delta)) / 2 * a
    print(f"X1: {x1} | X2: {x2}")

# 26)
distancia = float(input("Digite a distância em Km percorridos: "))
litros = float(input("Digite a quantidade de litros consumidos: "))
consumo = distancia / litros
if consumo < 8:
    print("Venda o carro!")
elif 8 <= consumo <= 14:
    print("Econômico!")
elif consumo > 12:
    print("Super econômico!")
else:
    print("Consumo Inválido!")

# 27)
idade = int(input("Digite sua idade: "))
if 5 <= idade <= 7:
    print("Infantil A")
elif 8 <= idade <= 10:
    print("Infantil B")
elif 11 <= idade <= 13:
    print("Juvenil A")
elif 14 <= idade <= 17:
    print("Juvenil B")
elif idade >= 18:
    print("Maiores de 18 anos")
else:
    print("Idade Inválida")

# 28)

