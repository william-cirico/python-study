"""
State

O padrão de projeto State é um padrão de projeto comportamental
que tem a intenção de permitir a um objeto mudar seu comportamento
quando o seu estado interno muda.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    """Context"""
    def __init__(self):
        self.state: OrderState = PaymentPending(self)

    def pending(self):
        print('Tentando executar pending()')
        self.state.pending()

    def approved(self):
        print('Tentando executar approve()')
        self.state.approve()

    def rejected(self):
        print('Tentando executar reject()')
        self.state.reject()


class OrderState(ABC):
    def __init__(self, order: Order):
        self.order = order

    @abstractmethod
    def pending(self) -> None:
        pass

    @abstractmethod
    def approve(self) -> None:
        pass

    @abstractmethod
    def reject(self) -> None:
        pass


class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Pagamento já pendente, não posso fazer nada.')

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Pagamento aprovado.')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado.')


class PaymentApproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento pendente.')

    def approve(self) -> None:
        print('Pagamento já aprovado, não posso fazer nada.')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado.')


class PaymentRejected(OrderState):
    def pending(self) -> None:
        print('Pagamento recusado. Não vou mover para pendente')

    def approve(self) -> None:
        print('Pagamento recusado. Não vou mover para aprovado.')

    def reject(self) -> None:
        print('Pagamento recusado. Não vou recusar novamente')


if __name__ == '__main__':
    order1 = Order()
    order1.pending()
    order1.approved()
    order1.approved()
    order1.rejected()
    order1.approved()