"""
Trabalhando com deltas de data e hora

data_inicio = dd/mm/yyyy 12:55:34
data_final = dd/mm/yyyy 13:34:23

delta = data_final - data_inicio
"""
import datetime
data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2020, 10, 3, 0)
tempo_evento = aniversario - data_hoje
print(tempo_evento)
print(f"Falta {tempo_evento.days} dias para o evento")

regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)
data_compra = data_hoje + regra_boleto
print(data_compra)