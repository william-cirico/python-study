# 1)
num = input("Digite um número: ")
if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f"O número {num} é par")
    else:
        print(f"O número {num} é impar")
else:
    print("Não é um inteiro")

# 2)
try:
    hora = int(input("Digite a hora atual: "))
    if 0 <= hora < 12:
        print("Bom dia!")
    elif 12 <= hora < 18:
        print("Boa tarde!")
    elif 18 <= hora < 24:
        print("Boa noite!")
    else:
        print("Hora Inválida")
except ValueError:
    print("Hora inválida!")

# 3)
nome = input("Digite o seu primeiro nome: ")
if 0 > len(nome) <= 4:
    print("Seu nome é curto")
elif 5 <= len(nome) <= 6:
    print("Seu nome é normal")
elif len(nome) > 6:
    print("Seu nome é grande")
else:
    print("Nome inválido")

