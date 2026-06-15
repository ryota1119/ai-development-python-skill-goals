def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name}!"


"""
以下の関数をテストするファイルを書いてください。
条件：
- test_add_正常系 と test_greet_正常系 の2つのテスト関数を書く
- pytest の命名規則に従う（関数名は test_ で始める）
- uv run pytest phase1/1-8/01_basic_test.py -v
で全テストがパスすること
"""


def test_add_正常系() -> None:
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(-2, 1) == -1


def test_greet_正常系() -> None:
    assert greet("Ryota") == "Hello, Ryota!"
    assert greet("Alice") == "Hello, Alice!"
    assert greet("bob") == "Hello, bob!"
