# Meta caracteres: ^ $
import re
from pprint import pprint

# () \1
# ()() \1 \2
# (())() \1 \2 \3

texto = """
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>
"""

print(re.findall(r'<[pdiv]{1,3}>.*?</[pdiv]{1,3}>', texto))
tags = (re.findall(r'(<([pdiv]{1,3})>(.*?)</\2>)', texto))
for tag in tags:
    um, dois, tres = tag
    print(tres)

# ?: Evita que o grupo fique salvo na memória
cpf = """147.923.213-43 
ihafdsiuhafsdfasdfiasdhasdufhasduf
018.149.059-52"""
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# ?P<nome> grupo nomeado
print(re.findall(r'<(?P<tag>[pdiv]{1,3})>.*?</(?P=tag)>', texto))

# Substituindo
print(re.sub(r'(<(.*?)>)(.*?)(</\2>)', r'\1"\3"\4', texto))
