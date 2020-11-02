"""
O bloco with - Forma Pythônica de manipular arquivos

- Utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with.
"""
with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)

