from typing import List, Tuple, Dict


def gen_map(points: List) -> int:
    return "hello"


print(gen_map(points=(1, 2, 3)))


def greet(hello: str) -> str:
    return f"hello, {hello}"


print(greet(1))


def greeting(name: str) -> str:
    return True


print(greeting(1))

hello = 1, 2, 3
print(hello)

def some_func(name: str) -> int:
    """
    Testing Type Hints
    """
    return f"Hello, {name}"


print(some_func(100))


