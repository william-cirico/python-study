"""
Command tem a intenção de encapsular uma solicitação como um objeto, desta
forma permitindo parametrizar clientes com diferentes solicitações, enfileirar
ou fazer registro (log) de solicitações e suportar operações que podem ser
desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a ação a ser executada) e um receiver (o objeto que vai executar a
ação no final).
"""
from abc import ABC, abstractmethod
from typing import Dict


class Light:
    """Receiver"""
    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'{self.name} in {self.room_name} is now ON')

    def off(self) -> None:
        print(f'{self.name} in {self.room_name} is now OFF')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f'{self.name} in {self.room_name} is now {self.color}')


class ICommand(ABC):
    """Interface de comando"""
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class LightOnCommand(ICommand):
    """Comando concreto"""
    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightChangeColor(ICommand):
    """Comando concreto"""
    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = self.light.color
        self.__old_color = self.light.color

    def execute(self) -> None:
        self.__old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self.__old_color)


class RemoteController:
    """Invoker"""
    def __init__(self) -> None:
        self.__buttons: Dict[str, ICommand] = {}
        self.__undos = []

    def button_add_command(self, name: str, command: ICommand) -> None:
        self.__buttons[name] = command

    def button_pressed(self, name: str) -> None:
        if name in self.__buttons:
            self.__buttons[name].execute()
            self.__undos.append((name, 'execute'))

    def button_undo(self, name: str) -> None:
        if name in self.__buttons:
            self.__buttons[name].undo()
            self.__undos.append((name, 'undo'))

    def global_undo(self) -> None:
        if not self.__undos:
            print('Nothing to undo')
            return None

        button_name, action = self.__undos[-1]

        if action == 'execute':
            self.__buttons[button_name].undo()
        else:
            self.__buttons[button_name].execute()

        self.__undos.pop()


if __name__ == '__main__':
    bedroom_light = Light('Luz quarto', 'quarto')
    bathroom_light = Light('Luz banheiro', 'banheiro')

    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light, 'Blue')
    bedroom_light_red = LightChangeColor(bedroom_light, 'Red')

    remote = RemoteController()
    remote.button_add_command('first_button', bedroom_light_on)
    remote.button_add_command('second_button', bedroom_light_blue)
    remote.button_pressed('first_button')
    remote.button_pressed('second_button')
    remote.global_undo()

