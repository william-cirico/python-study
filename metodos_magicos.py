"""
POO - Métodos Mágicos

São todos os métodos que utilizam dunder (__).

__init__ -> Constructor
__repr__ -> Representação do Objeto
__str__ -> Representação do Objeto (Tem prioridade)
__len__ -> Define um atributo para ser usado na função len
__del__ -> Permite colocar uma mensagem quando deletar um objeto da classe
__add__ -> Não sei explicar
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def paginas(self):
        return self.__paginas

    def __repr__(self):
        return self.__titulo

    def __str__(self):
        return self.__titulo

    def __len__(self):
        return self.__paginas

    def __del__(self):
        return print("Um objeto do tipo Livro foi deletado da memória")

    def __add__(self, other):
        return f"{self} + {other}"

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ""
            for n in range(other):
                msg += " " + str(self)
            return msg
        return "Não posso multiplicar"


livro1 = Livro("Python Rocks!", "Geek University", 400)
livro2 = Livro("Inteligência Artificial com Python", "Geek University", 350)

print(livro1)
print(livro2)
print(len(livro1))
print(len(livro2))
print(livro1 + livro2)
print(livro1 * 3)
print(livro1 * "a")

