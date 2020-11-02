"""
POO - Atributos

Atributos representam as características do objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância: Significa que ao criarmos instância/obejtos todos as isntâncias terão
    estes atributos;
    - Atributos de Classe: Atributos declarados diretamento na classe (fora do construtor). Geralmente
    já tem seu valor inicializado.
    - Atributos Dinâmicos: Um atributo de instância que pode ser criado em tempo de execução.


# Atributos de instância: São atributos declarados dentro do método construtor

# Por convenção ficou estabelecido que t0do atributo de uma classe é público, ou seja pode ser acessado
em t0do o projeto. Para tornar privado usar dunder (__). Conhecido como Name Mangling.
"""


# Atributos privados
class Lampada:

    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False


# Atributos públicos
class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Exemplo de uso de atributo privado
class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


user = Acesso("user@gmail.com", "123456")
print(user.email)
# print(user.__senha)  # AttributeError
print(user._Acesso__senha)  # Temos acesso. Mas não deveríamos fazer este acesso
user.mostra_senha()

# Atributo de Instância
user1 = Acesso("user1@gmail.com", "123456")
user2 = Acesso("user2@gmail.com", "123456")


# Atributo de classe
class ProdutoRefatorado:
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = ProdutoRefatorado.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * ProdutoRefatorado.imposto)
        ProdutoRefatorado.contador = self.id


p1 = ProdutoRefatorado("PLaystation 4", "Video Game", 2300)
p2 = ProdutoRefatorado("Xbox S", "Video Game", 4500)

print(p1.valor)  # Acesso incorreto
print(p2.valor)

# Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe
print(ProdutoRefatorado.imposto)  # Acesso correto

# Atributos dinâmicos (Não é comum)
p2.peso = "5kg"
print(f"Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}")

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

del p2.peso
del p2.valor

print(p1.__dict__)
print(p2.__dict__)