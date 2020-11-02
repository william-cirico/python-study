from math import pi, sqrt
from datetime import time, timedelta, date
"""
# 1)
num = int(input("Digite um número inteiro: "))
print(num)

# 2)
num = float(input("Digite um número real: "))
print(num)

# 3)
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
n3 = int(input("Digite um número inteiro: "))
print(n1 + n2 + n3)

# 4)
num = float(input("Digite um número real: "))
print(num ** 2)

# 5)
num = float(input("Digite um número real: "))
print(num / 5)

# 6)
c = float(input("Digite uma temperatura em Celsius: "))
f = c * (9 / 5) + 32
print(f)

# 7)
f = float(input("Digite uma temperatura em Fahrenheit: "))
c = 5 * (f - 32) / 9
print(c)

# 8)
k = float(input("Digite um temperatura em Kelvin: "))
c = k - 273.15
print(c)

# 9)
c = float(input("Digite um temperatura em Celsius: "))
k = c + 273.15
print(k)

# 10)
km = float(input("Digite uma velocidade em km/h: "))
ms = km / 3.6
print(ms)

# 11)
ms = float(input("Digite uma velocidade em m/s: "))
km = ms * 3.6
print(km)

# 12)
m = float(input("Digite um distância em Milhas: "))
km = m * 1.61
print(km)

# 13)
km = float(input("Digite um distância em Quilômetros: "))
m = km / 1.61
print(m)

# 14)
g = float(input("Digite um ângulo em graus: "))
r = g * pi / 180
print(r)

# 15)
r = float(input("Digite um ângulo em radianos: "))
g = r * 180 / pi
print(g)

# 16)
pl = float(input("Digite um comprimento em polegadas: "))
cm = pl * 2.54
print(cm)

# 17)
cm = float(input("Digite um comprimento em centímetros: "))
pl = cm / 2.54
print(pl)

# 18)
mc = float(input("Digite um comprimento em metros cúbicos: "))
li = mc * 1000
print(li)

# 19)
li = float(input("Digite um volume em litros: "))
mc = li / 1000
print(mc)

# 20)
kg = float(input("Digite um valor de massa em quilogramas: "))
li = kg / 0.45
print(li)

# 21)
li = float(input("Digite um valor de massa em libras: "))
kg = li * 0.45
print(kg)

# 22)
jar = float(input("Digite um comprimento em jardas: "))
m = jar * 0.91
print(m)

# 23)
m = float(input("Digite um comprimento em metros: "))
jar = m / 0.91
print(jar)

# 24)
mq = float(input("Digite uma área em metros quadrados: "))
ac = mq * 0.000247
print(ac)

# 25)
ac = float(input("Digite uma área em acres: "))
mq = ac * 4048.58
print(mq)

# 26)
mq = float(input("Digite uma área em metros quadrados: "))
hec = mq * 0.0001
print(hec)

# 27)
hec = float(input("Digite uma área em hectares: "))
mq = hec * 10000
print(mq)

# 28)
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
n3 = int(input("Digite um valor: "))
soma = (n1 ** 2) + (n2 ** 2) + (n3 ** 2)
print(soma)

# 29)
n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite uma nota: "))
n3 = float(input("Digite uma nota: "))
n4 = float(input("Digite uma nota: "))
media = (n1 + n2 + n3 + n4) / 4

# 30)
real = float(input("Digite um valor em real: "))
cot = float(input("Digite a cotação dólar: "))
dolar = real / cot
print(dolar)

# 31)
num = int(input("Digite um número: "))
ant = num - 1
suc = num + 1
print(f"{ant} {num} {suc}")

# 32)
num = int(input("Digite um número: "))
suc = num * 3 + 1
ant = num * 2 - 1
soma = ant + suc
print(soma)

# 33)
lado = float(input("Digite o tamanho do lado de um quadrado: "))
area = lado ** 2
print(area)

# 34)
raio = float(input("Digite o valor do raio de um círculo: "))
area = pi * (raio ** 2)
print(area)

# 35)
a = float(input("Digite o valor do cateto a: "))
b = float(input("Digite o valor do cateto b: "))
h = sqrt((a ** 2) + (b ** 2))
print(h)

# 36)
altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))
volume = pi * (raio ** 2) * altura
print(volume)

# 37)
produto = float(input("Digite o valor do produto: "))
desconto = produto - (produto * 0.12)
print(desconto)

# 38)
salario = float(input("Digite o valor do salário: "))
aumento = salario + (salario * 0.25)
print(aumento)

# 39)
premio = 780_000
g1 = premio * 0.46
g2 = premio * 0.32
g3 = premio * 0.22
print(f"G1: {g1} G2: {g2} G3: {g3}")

# 40)
dias = int(input("Digite a quantidade de dias: "))
valor = dias * 30 - ((dias * 30) * 0.08)
print(valor)

# 41)
valor = float(input("Digite o valor da hora: "))
quantidade = int(input("Digite a quantidade de horas trabalhadas: "))
salario = (valor * quantidade) + ((valor * quantidade) * 0.10)
print(salario)

# 42)
salario = float(input("Digite o salário base: "))
imposto = salario * 0.07
gratificao = salario * 0.05
salario_liquido = salario + gratificao - imposto

# 43)
valor = float(input("Digite um valor: "))
valor_desconto = valor - (valor * 0.10)
valor_parcela = valor / 3
comissao_vista = (valor_desconto * 0.05)
comissao_parcelado = (valor * 0.05)

# 44)
degrau = float(input("Digite a altura do degrau: "))
objetivo = float(input("Digite a altura desejada: "))
qdegrau = objetivo // degrau
print(qdegrau)

# 45)
letra = "A"
print(letra.lower())

# 46)
num = int(input("Digite um número: "))
string = str(num)
print(string[::-1])

# 47)
num = int(input("Digite um número: "))
string = str(num)
for numero in string:
    print(numero)

# 48)
segundos = int(input("Digite a duração do experimento em segundos: "))
horas = segundos // 3600
segundos -= horas * 3600
minutos = segundos // 60
segundos -= minutos * 60
final = time(horas, minutos, segundos)
print(f"Duração dos experimento: {final}")

# 49)
inicio = input("Digite o momento do início da experiência no formato: hh:mm:ss: ")
segundos_duracao = int(input("Digite a duração do experimento em segundos: "))

horas_inicio = int(inicio.split(":")[0])
minutos_inicio = int(inicio.split(":")[1])
segundos_inicio = int(inicio.split(":")[2])

segundos_duracao += segundos_inicio

horas_duracao = segundos_duracao // 3600
segundos_duracao -= horas_duracao * 3600
horas_duracao += horas_inicio


minutos_duracao = segundos_duracao // 60
segundos_duracao -= minutos_duracao * 60
minutos_duracao += minutos_inicio

final = time(horas_duracao, minutos_duracao, segundos_duracao)

print(f"Início do experimento: {inicio} | Término do experimento: {final}")

# 49) Com timedelta
inicio = input("Digite o horário de ínicio(hh:mm:ss): ")
duracao = int(input("Digite a duração do experimento em segundos: "))
horas, minutos, segundos = int(inicio.split(":")[0]), int(inicio.split(":")[1]), int(inicio.split(":")[2])
inicio = timedelta(hours=horas, minutes=minutos, seconds=segundos)
duracao = timedelta(seconds=duracao)
final = inicio + duracao
print(final)

# 50)
idade = int(input("Digite sua idade: "))
ano_atual = date.today().year
ano_nascimento = ano_atual - idade
print(ano_nascimento)

# 51)
cord = input("Digite as coordenadas x e y(x,y): ")
cord = cord.replace("(", "")
cord = cord.replace(")", "")
cord = cord.replace(" ", "")
x = int(cord.split(",")[0])
y = int(cord.split(",")[1])
distancia = sqrt(pow(x - 0, 2) + pow(y - 0, 2))
print(distancia)

# 52)
investimento = input("Digite quando cada apostador investiu: ")
investimento = investimento.replace(" ", "")
premio = float(input("Digite o valor do prêmio: "))
ap1 = int(investimento.split(",")[0])
ap2 = int(investimento.split(",")[1])
ap3 = int(investimento.split(",")[2])
total_investido = ap1 + ap2 + ap3
ap1_porcentagem = (ap1 * 100) / total_investido
ap2_porcentagem = (ap2 * 100) / total_investido
ap3_porcentagem = (ap3 * 100) / total_investido
ap1_premio = premio * (ap1_porcentagem / 100)
ap2_premio = premio * (ap2_porcentagem / 100)
ap3_premio = premio * (ap3_porcentagem / 100)
print(ap1_porcentagem)
print(ap2_porcentagem)
print(ap3_porcentagem)
print(ap1_premio)
print(ap2_premio)
print(ap3_premio)

# 53)
dimensoes = input("Digite as dimensões do terreno (comprimento e largura): ")
dimensoes = dimensoes.replace(" ", "")
comprimento, largura = float(dimensoes.split(",")[0]), float(dimensoes.split(",")[1])
preco = float(input("Digite o preço do metro de tela: "))
preco_final = ((comprimento ** 2) * preco) + ((largura ** 2) * preco)
print(preco_final)
"""



















