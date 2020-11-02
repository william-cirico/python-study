logged_user = False

if logged_user:
    msg = "Logado"
else:
    msg = "Não logado"

print(msg)

msg = "Logado" if logged_user else "Não logado"
print(msg)

idade = 17
if idade >= 18:
    msg = "Pode acessar"
else:
    msg = "Não pode acessar"

maior_de_idade = (idade >= 18)
msg = "Pode acessar" if maior_de_idade else "Não pode acessar"


