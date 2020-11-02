from dados import produtos, pessoas, lista
import sys

# Com filter()
nova_lista = filter(lambda x: x > 5, lista)
print(sys.getsizeof(nova_lista))  # 48
# Com list_comprehension
nova_lista = [x for x in lista if x > 5]
print(sys.getsizeof(nova_lista))  # 120

# Com Generator
nova_lista = (x for x in lista if x > 5)
print(sys.getsizeof(nova_lista))  # 112
