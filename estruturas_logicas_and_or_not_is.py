"""
Estruturas lógicas: and, or, not e is

Operadores unários:
    - not
Operadores binários:
    - and, or, binario
"""
ativo = True
logado = False

if ativo and logado:
    print("Usuário ativo no sistema")
else:
    print("Você precisa ativar sua conta. Por favor, cheque "
          "seu email")


if not ativo:
    print("Você precisa checar a sua conta. Por favor, cheque"
          "seu email")
else:
    print("Bem-Vindo usuário")

# Ativo é falso?
print(ativo is False)
