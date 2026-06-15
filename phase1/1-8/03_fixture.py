"""
以下のクラスを対象に、fixture を使ったテストを書いてください。

条件：
- @pytest.fixture で ShoppingCart のインスタンスを返す cart fixture を定義する
- test_add、test_remove、test_count の3つのテストで fixture を引数として受け取って使う
"""


class ShoppingCart:
    def __init__(self) -> None:
        self.items: list[str] = []


def add(self, item: str) -> None:
    self.items.append(item)


def remove(self, item: str) -> None:
    self.items.remove(item)


def count(self) -> int:
    return len(self.items)
