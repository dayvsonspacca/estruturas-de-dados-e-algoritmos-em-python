
from typing import Any
from random import randint

"""
A estrutura de dados Fila segue o principio de FIFO, first-in first-out ou seja,
o primeiro elemento a entra na lista é o primeiro a sair.
"""


class Queue:

    def __init__(self):
        self.queue = []
        self.lenght = len(self.queue)

    def dequeue(self):
        return self.queue.pop(0)

    def enqueue(self, item: Any):
        self.queue.append(item)

    def show(self):
        print(self.queue)


def main():

    queue = Queue()

    # Inserção de valores aleatórios na fila
    for i in range(5):
        queue.enqueue(randint(0, 10))

    # Consultando a fila
    queue.show()
    # Removendo o 1° e 2° valor da fila.
    queue.dequeue()
    queue.dequeue()
    # Consultando novamente a fila.
    queue.show()


if __name__ == "__main__":
    main()
