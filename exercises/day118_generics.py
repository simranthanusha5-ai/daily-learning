# Day 118: Generics and TypeVar
from typing import TypeVar, Generic, List

T = TypeVar("T")

class GenericStack(Generic[T]):
    def __init__(self):
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

int_stack = GenericStack[int]()
int_stack.push(10)
int_stack.push(20)
print("Popped integer:", int_stack.pop())
