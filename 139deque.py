# LIFO - Last in, first out
# FIFO - First in, first out
# Filas podem ter efeitos colaterais em desempenho
from collections import deque

fila = deque(maxlen=5)
fila.append("João")
fila.append("Maria")
fila.append("Marcos")
fila.append("José")

for nome in fila:
    print(nome)

for i in range(4):
    print(f"Saiu {fila.popleft()}")