lista = [
    ["P1", 30],
    ["P2", 5],
    ["P3", 100],
    ["P4", 87],
]

lista.sort(key=lambda l: l[1], reverse=True)
print(lista)
