"""
Introdução ao módulo Unittest

Forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser:
    - Funções/Métodos;
    - Classes;
    - Módulos;

Para criar nosssos testes, criamos classes que herddam de unittest.TestCase
Para rodar os teste, utilizamos unittest.main()

# Conhecendo as assertions
assertEqual(a, b)            a == b
assertNotEqual(a, b)         a != b
assertTrue(x)                x é verdadeiro
assertFalse(x)               x é falso
assertIs(a, b)               a é b
assertIsNot(a, b)            a não é b
assertIfNone(x)              x é None
assertIsNotNone(x)           x não é None
assertIn(a, b)               a está em b
assertNotIn(a, b)            a não está em b
assertIsInstance(a, b)       a é instância de b
assertNotIsInstance(a, b)    a não é instância de b

Por convenção, todos os testes em um test case devem ter seus nomes iniciados por:
test_

Para testar o código e obter informações
python testes.py -v

# É recomendado utilizar docstrings nos testes
"""


# Prática utilizando TDD


