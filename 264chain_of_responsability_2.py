from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def handle(self, letter: str) -> str:
        pass


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler):
        self.letters = ['A', 'B', 'C']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            nome_classe = self.__class__.__name__
            return f'{nome_classe}: conseguiu tratar o valor de {letter} '
        return self.sucessor.handle(letter)


class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        nome_classe = self.__class__.__name__
        return f'{nome_classe}: não conseguiu tratar o valor de {letter} '


if __name__ == '__main__':
    handler_unsolved = HandlerUnsolved()
    handler_abc = HandlerABC(handler_unsolved)

    print(handler_abc.handle('A'))
    print(handler_abc.handle('D'))
