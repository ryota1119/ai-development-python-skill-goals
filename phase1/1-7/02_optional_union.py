"""
問題1 — find_name(names, target) を実装
- 名前のリストから target を探して返す
- 見つかれば str、見つからなければ None を返す
- 戻り値の型は Optional[str] を使うこと
find_name(["Alice", "Bob"], "Alice")  -> "Alice"
find_name(["Alice", "Bob"], "Carol")  -> None
"""

from typing import Any, Optional, Union


def find_name(names: list[str], target: str) -> Optional[str]:
    if target in names:
        return target
    return None


print(find_name(["Alice", "Bob"], "Alice"))
print(find_name(["Alice", "Bob"], "Carol"))


"""
問題2 — describe(value) を実装
- int か str を受け取り "値: {value}" を返す
- 引数の型は Union[int, str] を使うこと
describe(42)      -> "値: 42"
describe("hello") -> "値: hello"
"""


def describe(value: Union[int, str]) -> str:
    return f"値: {value}"


print(describe(42))
print(describe("hello"))

"""
問題3 — 問題1・2を | 演算子で書き直す（Python 3.10+ の記法）
- Optional[str] → str | None
- Union[int, str] → int | str
- 関数名は new_find, new_describe にすること
"""


def new_find(names: list[str], target: str) -> str | None:
    if target in names:
        return target
    return None


print(new_find(["Alice", "Bob"], "Alice"))
print(new_find(["Alice", "Bob"], "Carol"))


def new_describe(value: int | str) -> str:
    return f"値: {value}"


print(new_describe(42))
print(new_describe("hello"))

"""
問題4 — type_name(value) を実装
- 引数の型は Any を使うこと
- type(value).__name__ で型名が取得できる
type_name(42)     -> "int"
type_name("hi")   -> "str"
type_name([1, 2]) -> "list"
"""


def type_name(value: Any) -> str:
    return type(value).__name__


print(type_name(42))
print(type_name("hi"))
print(type_name([1, 2]))
