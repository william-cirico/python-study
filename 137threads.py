from time import sleep
from threading import Thread
from threading import Lock


# Forma 1 - Criando e instanciando um objeto Thread
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        super().__init__()
        self.texto = texto
        self.tempo = tempo

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread("Thread 1", 5)
t1.start()

t2 = MeuThread("Thread 2", 5)
t2.start()

t3 = MeuThread("Thread 3", 5)
t3.start()


def vai_demorar(tempo, texto):
    sleep(tempo)
    print(texto)


# Forma 2
t = Thread(target=vai_demorar, args=(5, "Xesquedele"))
t.start()

for i in range(20):
    print(i)
    sleep(i)


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            self.lock.release()
            return print("Não temos ingressos suficientes")
        sleep(1)
        self.estoque -= quantidade
        print(f"Você comprou {quantidade} ingresso(s)."
              f"Ainda temos {self.estoque} em estoque.")
        self.lock.release()


if __name__ == "__main__":
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()










