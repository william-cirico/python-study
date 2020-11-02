"""
Geradores

- Generators são iterators;
- Funções geradoras utilizam a palavra reservada yield;

Diferenças entre Funções e Generator Functions

----------------------------------------------------------------------------------------------------
| Funções                                          | Generator Functions                           |
----------------------------------------------------------------------------------------------------
| Utilizam return                                  | Utilizam yield                                |
| Retorna uma vez                                  | Podem utilizar yield múltiplas vezes          |
| Quando executada, retorna um valor               | Quando executada, retorna um generator        |
----------------------------------------------------------------------------------------------------
"""


# Exemplo de Generator Function
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


gen = conta_ate(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(10)

for num in gen:
    print(num)
