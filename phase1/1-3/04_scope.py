# 1. 以下のコードを読んで、出力結果を予測してからコメントに書いてください。
#    その後、実際に実行して確認すること。

x = 10


def outer():
    x = 20

    def inner():
        x = 30
        print(x)  # Q1: 何が出力される？ → A: 30

    inner()
    print(x)  # Q2: 何が出力される？ → A: 20


outer()
print(x)  # Q3: 何が出力される？ → A: 10

# 2. global を使ってグローバル変数を関数内から書き換える関数 increment_counter()を実装
#    - グローバル変数 counter = 0 を定義する
#    - increment_counter() を呼ぶたびに counter が 1 増える
#    - 3回呼んだあと counter を print すると 3 になること

counter = 0


def increment_counter() -> None:
    global counter
    counter += 1


increment_counter()
increment_counter()
increment_counter()
print(counter)


# 3. nonlocal を使って外側の変数を書き換える make_counter() を実装
#    - make_counter() はクロージャを返す
#    - 返された関数を呼ぶたびに内側のカウンタが 1 増えて、現在値を返す
#    例:
#      counter = make_counter()
#      print(counter())  # -> 1
#      print(counter())  # -> 2
#      print(counter())  # -> 3


def make_counter():
    count = 0

    def add_counter() -> int:
        nonlocal count
        count += 1
        return count

    return add_counter


add_count = make_counter()
print(add_count())
print(add_count())
print(add_count())
