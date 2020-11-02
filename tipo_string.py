"""
Tipo String
"""

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = """"Angelina
Jolie"""
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome.upper())
print(nome.lower())
print(nome.split())  # Transforma em uma lista de strings
print(nome[0:4])  # Slice de string
print(nome[5:15])  # Slice de String
print(nome.split()[0])
print(nome.split()[1])
print(nome[::-1])  # Inversão da String
print(nome.replace('G', 'P'))

