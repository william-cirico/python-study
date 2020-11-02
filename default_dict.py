"""
Módulo Collections - Default Dict

Ao criar um dicionário utilzando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre
que não houver um valor definido. Caso tentamos acessar uma chave que
não existe, essa chave será criada e o valor default será atribuído.

Obs.: Lambdas são funções sem nome, que podem ou não receber parâmetros
de entrada e retornar valores.
"""
# Fazendo import
from collections import defaultdict

dicionario = {'curso': 'Programação em Python: Essencial'}
print(dicionario)
print(dicionario['curso'])

dicionario = defaultdict(lambda: 0)
print(dicionario)
dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario['outro'])
print(dicionario)






