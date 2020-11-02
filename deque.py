"""
Módulo Collections - Deque

Deque é uma lista de alta performance
"""
# Importe
from collections import deque

# Criando deques
deq = deque('geek')
print(deq)

# Adicionando elementos no deque
deq.append('y')  # Adiciona no final
print(deq)

deq.appendleft('k')
print(deq)  # Adiciona no começo

# Remover elementos

print(deq.pop())  # Remove e retorna o último elemento
print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento
print(deq)
