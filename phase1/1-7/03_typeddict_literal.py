"""
問題1 — TypedDict で辞書の型を定義する

# 以下の構造を持つ辞書の型 User を TypedDict で定義せよ
# name: str
# age: int
# email: str

# そしてこの関数を実装すること
def greet_user(user: User) -> str:
    ...

# 期待出力
# greet_user({"name": "Alice", "age": 30, "email": "alice@example.com"})
# -> "Alice (30歳) <alice@example.com>"
"""

from typing import Literal, TypedDict


class User(TypedDict):
    name: str
    age: int
    email: str


def greet_user(user: User) -> str:
    return f"{user['name']} ({user['age']}歳) <{user['email']}>"


print(greet_user({"name": "Alice", "age": 30, "email": "alice@example.com"}))


"""
問題2 — Literal で受け取れる値を制限する

# 引数 direction は "left" / "right" / "up" / "down" のみ受け付ける
def move(direction: Literal[...]) -> str:
    ...

# 期待出力
# move("left")  -> "左に移動"
# move("right") -> "右に移動"
# move("up")    -> "上に移動"
# move("down")  -> "下に移動"
"""


def move(direction: Literal["left", "right", "up", "down"]) -> str:
    labels = {
        "left": "左に移動",
        "right": "右に移動",
        "up": "上に移動",
        "down": "下に移動",
    }
    return labels[direction]


print(move("left"))
print(move("right"))
print(move("up"))
print(move("down"))

"""
問題3 — TypedDict + Literal を組み合わせる

# 以下の構造を持つ TypedDict を定義せよ
# title: str
# status: Literal["todo", "in_progress", "done"]

# そしてこの関数を実装すること
def format_task(task: Task) -> str:
    ...

# 期待出力
# format_task({"title": "型ヒントを学ぶ", "status": "in_progress"})
# -> "[進行中] 型ヒントを学ぶ"
# format_task({"title": "mypy を試す", "status": "done"})
# -> "[完了] mypy を試す"
# format_task({"title": "復習する", "status": "todo"})
# -> "[未着手] 復習する"
"""


class Task(TypedDict):
    title: str
    status: Literal["todo", "in_progress", "done"]


def format_task(task: Task) -> str:
    labels = {"todo": "未着手", "in_progress": "進行中", "done": "完了"}
    return f"[{labels[task['status']]}] {task['title']}"


print(format_task({"title": "型ヒントを学ぶ", "status": "in_progress"}))
print(format_task({"title": "復習する", "status": "todo"}))
print(format_task({"title": "mypy を試す", "status": "done"}))
