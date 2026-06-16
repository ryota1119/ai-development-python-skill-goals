"""
問題1 — add(a, b) に型注釈を付けて実装
add(3, 4)  -> 7
"""


def add(x: int, y: int) -> int:
    return x + y


print(add(3, 4))

"""
問題2 — greet(name) に型注釈を付けて実装
greet("Alice")  -> "Hello, Alice!"
"""


def greet(name: str) -> str:
    return f"Hello, {name}!"


print(greet("Ryota"))

"""
問題3 — total(numbers) に型注釈を付けて実装
- list[int] を使うこと（Python 3.9+。Go の []int に相当）
total([1, 2, 3])  -> 6
"""


def total(numbers: list[int]) -> int:
    return sum(numbers)


print(total([1, 2, 3]))

"""
問題4 — average_score(scores) に型注釈を付けて実装
- dict[str, int] を使うこと（Go の map[string]int に相当）
average_score({"Alice": 80, "Bob": 90, "Carol": 70})  -> 80.0
"""


def average_score(scores: dict[str, int]) -> float:
    return sum(scores.values()) / len(scores)


print(average_score({"Alice": 80, "Bob": 90, "Carol": 70}))
