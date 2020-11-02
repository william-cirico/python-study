from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays, monthrange

data = datetime(2019, 4, 20, 10, 53, 20)
print(data.strftime("%d/%m/%Y %H:%M:%S"))

data = datetime.strptime("20/04/2019", "%d/%m/%Y")
print(data)

data1 = datetime.strptime("20/04/1987 20:00:00", "%d/%m/%Y %H:%M:%S")
data2 = datetime.strptime("25/04/1987 20:00:00", "%d/%m/%Y %H:%M:%S")
dif = data2 - data1
print(dif)

setlocale(LC_ALL, "pt_BR.utf-8")
dt = datetime.now()
formatacao = dt.strftime("%A, %d de %B de %Y")
print(formatacao)

mes_atual = int(dt.strftime("%m"))
print(mes_atual, mdays[mes_atual])

# Ano Bissexto
ultimos_dias_de_meses_do_ano_atual = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
]
print(ultimos_dias_de_meses_do_ano_atual)