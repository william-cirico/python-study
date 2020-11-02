"""
O padrão Observer tem a intenção de definir uma dependência de um-para-muitos
entre objetos, de maneira que quando um objeto muda de estado, todos os seus
dependentes são notificados e atualizados automaticamente.

Um observer é um objeto que gostaria de ser informado, um observable (subject)
é a entidade que gera as informações.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObservable(ABC):
    """Observable"""

    @property
    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class WeatherStation(IObservable):
    """Observable"""
    def __init__(self):
        self.__observers: List[IObserver] = []
        self.__status: Dict = {}

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, update_status: Dict):
        new_status: Dict = {**self.__status, **update_status}

        if new_status != self.__status:
            self.__status = new_status
            self.notify_observers()

    def reset_status(self):
        self.__status = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self.__observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer in self.__observers:
            self.__observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.__observers:
            observer.update()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None:
        pass


class Smartphone(IObserver):
    def __init__(self, observable: IObservable):
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} acabou '
              f'de ser atualizado => {self.observable.status}')


if __name__ == '__main__':
    weater_station = WeatherStation()

    smartphone = Smartphone('iPhone', weater_station)
    outro_smartphone = Smartphone('Outro Smartphone', weater_station)

    weater_station.add_observer(smartphone)
    weater_station.add_observer(outro_smartphone)

    weater_station.status = {'temperature': '30'}
    weater_station.status = {'temperature': '32'}


