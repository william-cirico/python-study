from dataclasses import dataclass, field


@dataclass(repr=False)
class Pessoa:
    __nome: str = field(repr=False)
    __sobrenome: str = field(repr=False)

    def __post_init__(self):
        self.__nome_completo = f"{self.__nome} {self.__sobrenome}"

        if not isinstance(self.__nome, str):
            raise TypeError("Tipo Inválido")

    @property
    def nome(self):
        return self.__nome


p1 = Pessoa("William", "Círico")
print(p1)
print(p1.nome)
