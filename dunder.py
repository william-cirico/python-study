"""
Dunder Name e Dunder Main

Dunder Name -> __name__
Dunder Main -> __main__

Em Python dunder são utilizados para criar funções, atributos, propriedades e etc para não gerar
conflito de nomes;

# En Python, se executarmos um módulo Python diretamente na linha de comando, internamente
o Python atribuirá à variável __name__ o valor __main__ indicando que este módulo é o módulo
de execução principal.
"""
from primeiro import funcao1
funcao1()


