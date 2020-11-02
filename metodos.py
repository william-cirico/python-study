"""
POO - Métodos

- Representam os comportamentos do objeto, ou seja, as ações que esse objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, assim como os atributos em 2 grupos: Instância e Classe.

# Métodos de Instância

- O método __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir
da classe.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


# Para criptografar senha
# pip install passlib
from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    # Métodos públicos
    def correr(self, metros):
        print(f"{self.__nome} está correndo {metros} metros")

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


nome = input("Informe o nome: ")
sobrenome = input("Informe o sobrenome: ")
email = input("Informe o -email: ")
senha = input("Informe a senha: ")
confirma_senha = input("Confirme a senha: ")

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
    print("Usuário criado com sucesso")
else:
    print("Senha não confere...")
    exit(42)

senha = input("Informe a senha para acesso: ")

if user.checa_senha(senha):
    print("Acesso permitido")
else:
    print("Acesso negado")

p1 = Produto("Playstation 4", "Video Game", 2300)
print(p1.desconto(20))

u1 = Usuario("William", "Círico", "contato.williamc@gmail.com", "X*&ricr6*LS4")
print(u1.nome_completo())


# Métodos de classe (Não fazem acesso aos atributos da classe)
class UsuarioRefatorada:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f"Temos {cls.contador} usuário(s) no sistema")

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = UsuarioRefatorada.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        UsuarioRefatorada.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    # Método privado (Só pode ser acessado dentro da classe)
    def __gera_usuario(self):
        return self.__email.split("@")[0]

    # Método Estático
    @staticmethod
    def definicao():
        return "UXR344"


user1 = UsuarioRefatorada("William", "Círico", "contato.williamc@gmail.com", "123456")
user2 = UsuarioRefatorada('Felicity', 'Jones', 'felicity@gmail.com', '123456')

# Chamada do método de classe
UsuarioRefatorada.conta_usuario()

# Chamada do método privado (Errado)
print(user2._UsuarioRefatorada__gera_usuario())  # Name Mandling

# Chamada do método estático
print(UsuarioRefatorada.contador)
print(UsuarioRefatorada.definicao())


