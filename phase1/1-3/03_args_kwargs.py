# 1. 可変長引数で複数の数値を受け取り、合計を返す関数 my_sum()
#    例: my_sum(1, 2, 3)       -> 6
#    例: my_sum(10, 20)        -> 30
#    ※ sum() 組み込みは使わずに実装すること


def my_sum(*args: int) -> int:
    total = 0
    for i in args:
        total += i
    return total


print(my_sum(1, 2, 3))
print(my_sum(10, 20))

# 2. キーワード引数を受け取り、"key: value" の形式で1行ずつ表示する関数 show_profile()
#    例: show_profile(name="Alice", age=30, city="Tokyo")
#    出力:
#      name: Alice
#      age: 30
#      city: Tokyo


def show_profile(**kwargs) -> None:
    for k, v in kwargs.items():
        print(f"{k}: {v}")


show_profile(name="Alice", age=30, city="Tokyo")


# 3. 位置引数もキーワード引数も両方受け取れる関数 mixed()
#    - *args の中身を表示
#    - **kwargs の中身を表示
#    例: mixed(1, 2, name="Alice", age=30)
#    出力:
#      args: (1, 2)
#      kwargs: {'name': 'Alice', 'age': 30}


def mixed(*args, **kwargs) -> None:
    print(f"args: {args}")
    print(f"kwards: {kwargs}")


mixed(1, 2, name="Alice", age=30)
