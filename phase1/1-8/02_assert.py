"""
以下の関数を定義し、様々な assert
パターンを使ったテストを書いてください。

条件：
- divide の正常系と例外発生のテストを書く
- get_even_numbers のテストでリストの内容を検証する
- 例外テストには pytest.raises を使う
"""

import pytest


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("ゼロ除算はできません")
    return a / b


def get_even_numbers(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]


def test_divide_正常系() -> None:
    assert divide(2.0, 1.0) == 2.0
    assert divide(5.0, 2.0) == 2.5
    assert divide(9.0, 3.0) == 3.0


def test_divide_異常系() -> None:
    with pytest.raises(ValueError) as e:
        divide(4, 0)

    assert str(e.value) == "ゼロ除算はできません"


def test_get_even_numbers_正常系() -> None:
    assert get_even_numbers([1, 2, 3]) == [2]
    assert get_even_numbers([]) == []
    assert get_even_numbers([2, 3, 4]) == [2, 4]
    assert get_even_numbers([99, 98, 97, 96]) == [98, 96]
    assert get_even_numbers([-1, 0, 1, 2]) == [0, 2]
