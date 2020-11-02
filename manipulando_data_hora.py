"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
"""
import datetime
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a data e a hora corrente
print(datetime.datetime.now())

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)

# Alterar o horário para 16 horas, 0 minutos, 0 segundo
inicio = inicio.replace(hour=16, minute=0, second=0)
print(inicio)

evento = datetime.datetime(2020, 1, 1, 0)
print(evento)

nascimento = input("Informe sua data de nascimento (dd/mm/yyyy): ")
nascimento = nascimento.split("/")
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)
