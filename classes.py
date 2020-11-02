"""
POO - Classes

Classes nada mais são do que modelos dos objetos do mundo real sendo representado computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
- Atributos -> Características do objeto. Ex.: Tensão da lâmpada
- Método (funções) -> Comportamento ou ações. Ex.: Ligar a lâmpada

Para definir uma classe, utilizamos a palavra reservada class.

Obs.: Utilizamos a palavra "pass" quando temos um bloco de código que ainda não está implementado

# Quando nomeamos uma classe em Python a inicial deve ser maiúscula. (CamelCase)

Classes também são chamadas de entidade.
"""


class Lampada:
    pass


lamp = Lampada()
print(type(lamp))


class ContaCorrente:
    pass

