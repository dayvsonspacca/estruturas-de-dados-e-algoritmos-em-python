
from typing import Any
from random import randint

"""
A estrutura de dados Pilha segue o principio de FILO, first-in last-out ou seja,
o primeiro elemento a entra na lista é o último a sair.
"""


class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        self.stack.pop()

    def push(self, value: Any):
        self.stack.append(value)

    def show(self):
        print(self.stack)

    def __str__(self):
        return f"{self.stack}"

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.stack):
            item = self.stack[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


def main():
    stack = Stack()
    # Inserção de valores aleatórios na pilha.
    for i in range(5):
        stack.push(randint(0, 10))

    # Consultando a fila
    stack.show()
    # Removendo o 1° e 2° valor da pilha.
    stack.pop()
    stack.pop()
    # Consultando novamente a pilha.
    stack.show()
    print(stack)
    # Iterando na pilha.
    for item in stack:
        print(item)


if __name__ == "__main__":
    main()
