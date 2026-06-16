"""
以下のクラスを対象に、fixture を使ったテストを書いてください。

条件：
- @pytest.fixture で ShoppingCart のインスタンスを返す cart fixture を定義する
- test_add、test_remove、test_count の3つのテストで fixture を引数として受け取って使う
"""

import pytest


class ShoppingCart:
    def __init__(self) -> None:
        self.items: list[str] = []

    def add(self, item: str) -> None:
        self.items.append(item)

    def remove(self, item: str) -> None:
        self.items.remove(item)

    def count(self) -> int:
        return len(self.items)


@pytest.fixture
def cart():
    return ShoppingCart()


def test_add_正常系(cart):
    cart.add("item1")
    assert cart.items == ["item1"]

    cart.add("item2")
    assert cart.items == ["item1", "item2"]


def test_remove_正常系(cart):
    cart.add("item1")
    cart.add("item2")
    cart.remove("item1")
    assert cart.items == ["item2"]

    cart.remove("item2")
    assert cart.items == []


def test_count_正常系(cart):
    cart.add("item1")
    assert cart.count() == 1

    cart.add("item2")
    assert cart.count() == 2

    cart.remove("item2")
    assert cart.count() == 1
