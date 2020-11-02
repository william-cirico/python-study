"""
Erros mais comuns em Python:

- SyntaxError: Erro de sintaxe;
- NameError: Variável ou função não definida;
- TypeError: Ocorre quando uma função/operação/ação é aplicada a um tipo errado.
- IndexError: Utilizar índice inválido;
- ValueError: Ocorre quando uma função/operação built-in recebe um argumento com tipo correto
mas valor inapropriado;
- KeyError: Acessar dicionário com uma chave que não existe;
- AttributeError: Ocorre quando uma variável não tem um atributo/função;
- IndentationError: Ocorre quando a identação do Python  não é respeitada (4 espaçoes)
"""
# Exemplos SyntaxError:
def funcao:
    print('Geek Univserity')

None = 1

# Exemplos NameError:
print(geek)

a = 10
if a < 10:
    msg = 'É maior que 10'

print(msg)

# Exemplos TypeError
print(len(5))

print('Geek' + [])

# Exemplos IndexError
lista = ['Geek']
print(lista[2])
print(lista[0][10])

# Exemplos ValueError
print(int('Geek'))
print(float('Geek'))

# Exemplos KeyError
dic = {}
print(dic['geek'])

# Exemplos AttributeError
tupla = (11, 2, 31, 4)
print(tupla.sort())

# # Exemplos IndentationError
def nova():
print('Geek')

for i in range(10):
i + 1

