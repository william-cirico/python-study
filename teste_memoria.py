"""
Teste de Memória com Generators

# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13...
"""


def fib_lista(maxi):
    nums = []
    a, b = 0, 1
    while len(nums) < maxi:
        nums.append(b)
        a, b = b, a + b
    return nums


for n in fib_lista(10000):
    print(n, end=" ")


# Função usando geradores
def fib_gen(maxi):
    a, b, contador = 0, 1, 0
    while contador < maxi:
        a, b = b, a + b
        yield a
        contador += 1


for n in fib_lista(50000):
    print(n, end=" ")

