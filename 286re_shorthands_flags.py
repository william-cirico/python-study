import re
# Shorhands
# -----------
# \w -> [a-zA-Z0-9À-ú_]
# \W -> [^a-zA-Z0-9À-ú_]
# \d -> [0-9}
# \D -> [^0-9]
# \s -> [ \r\n\f\t]
# \S -> [^ \r\n\f\t]
# \b -> borda
# -------------
# Flags
# re.A -> Só pega caracteres da tabela ASCII
# re.I -> IGNORECASE
# re.M -> MULTILINE (Checa por linha)
# re.S -> DOTALL ()
texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
Jã
'''

# Sem shorthand
print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))

# Com shorthand \w
print(re.findall(r'\w+', texto))
print(re.findall(r'\W+', texto))
print(re.findall(r'\be\w', texto))  # palavras que começam com e
print(re.findall(r'\w+e\b', texto))  # palavras que terminam com e
print(re.findall(r'\b\w{5}\b', texto))  # palavras de 5 letras

cpf = """
131.234.123-21 A
123.546.234-43 B
341.423.543-23
"""

# Flags
print(re.findall(r'^\d{3}.\d{3}.\d{3}-\d{2}$', cpf, flags=re.M))

texto2 = """O João gosta de folia
E adora ser amado"""
print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))
