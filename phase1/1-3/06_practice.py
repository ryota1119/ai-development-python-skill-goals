# day3 総合練習
#
# 「成績集計システム」を実装してください。
# 以下の問題を上から順番に解いてください。

# ----------------------------------------
# 問題 1
# 生徒1人分の点数リストを受け取り、平均点を返す関数 average() を実装してください。
# - 点数は可変長引数 (*scores) で受け取る
# - 点数が1つも渡されなかった場合は 0.0 を返す
# 例:
#   average(80, 90, 70)  -> 80.0
#   average(100)         -> 100.0
#   average()            -> 0.0


def average(*scores) -> float:
    if len(scores) == 0:
        return 0.0
    return sum(scores) / len(scores)


# ----------------------------------------
# 問題 2
# 平均点を受け取り、成績（文字列）を返す関数 grade() を実装してください。
# - 90以上 → "S"
# - 80以上 → "A"
# - 70以上 → "B"
# - 60以上 → "C"
# - 60未満 → "D"
# 例:
#   grade(95.0)  -> "S"
#   grade(82.0)  -> "A"
#   grade(55.0)  -> "D"


def grade(average: float) -> str:
    if average >= 90.0:
        return "S"
    elif average >= 80.0:
        return "A"
    elif average >= 70.0:
        return "B"
    elif average >= 60.0:
        return "C"
    else:
        return "D"


# ----------------------------------------
# 問題 3
# 生徒データのリストを受け取り、平均点と成績を付与して返す関数 evaluate() を実装してください。
# - **kwargs は使わず、辞書のリストをそのまま受け取る
# - map() と lambda を使って変換すること
# - 元のリストは変更しないこと（新しいリストを返す）
#
# 入力例:
students = [
    {"name": "Alice", "scores": [80, 90, 70]},
    {"name": "Bob", "scores": [60, 55, 65]},
    {"name": "Carol", "scores": [95, 100, 98]},
]
#
# 出力例（各辞書に average と grade を追加）:
# [
#   {"name": "Alice", "scores": [80, 90, 70], "average": 80.0, "grade": "A"},
#   {"name": "Bob",   "scores": [60, 55, 65], "average": 60.0, "grade": "C"},
#   {"name": "Carol", "scores": [95, 100, 98], "average": 97.67, "grade": "S"},
# ]
# ※ average は小数点2桁で丸める（round(x, 2)）


def evaluate(students: list) -> list:
    return list(
        map(
            lambda s: {
                "name": s["name"],
                "scores": s["scores"],
                "average": round(average(*s["scores"]), 2),
                "grade": grade(round(average(*s["scores"]), 2)),
            },
            students,
        )
    )


# ----------------------------------------
# 問題 4
# 評価済みの生徒リストを受け取り、成績順（S→A→B→C→D）に並べた新しいリストを返す
# 関数 rank() を実装してください。
# - sorted() と lambda を使うこと
# - ヒント: 成績を数値に変換する辞書 {"S": 0, "A": 1, ...} を使うと楽です

grade_rank = {"S": 0, "A": 1, "B": 2, "C": 3, "D": 4}


def rank(students) -> list:
    return sorted(students, key=lambda s: grade_rank[s["grade"]])


# ----------------------------------------
# 動作確認（実装後にコメントを外してください）

result = evaluate(students)
ranked = rank(result)
for s in ranked:
    print(f"{s['name']}: 平均 {s['average']} → {s['grade']}")
