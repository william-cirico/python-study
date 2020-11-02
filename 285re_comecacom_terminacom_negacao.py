# ^ -> Começa com
# $ -> Termina com
# [^a-z] -> Negação

import re

cpf = "018.149.059-52"
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
cpf2 = "018.149.059-52 lul"
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf2))
print(re.findall(r'[^a-z]+', cpf))
print(re.findall(r'[^0-9]+', cpf))
print(re.findall(r'[^.-]', cpf))
print(re.sub(r'[^0-9]', '', cpf))

