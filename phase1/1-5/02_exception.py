"""
1. 存在しないファイルを open() しようとして FileNotFoundError を except
で捕捉し、エラーメッセージを表示する
"""

file_name = "./phase1/1-5/not_exists.txt"

try:
    f = open(file_name, "r")
except FileNotFoundError as e:
    print(e)

"""
2. try / except / else / finally を全て使う構造を1つ書く
- else：例外がなかったときだけ実行
- finally：例外の有無に関わらず必ず実行
"""
try:
    with open(file_name, "r") as f:
        contents = f.read()
except FileNotFoundError as e:
    print(e)
else:
    print(contents)
finally:
    print("Analysis complete.")


"""
3. ZeroDivisionError と TypeError を1つの try ブロックでそれぞれ別の except
で捕捉する
"""
input_number = input("数字を入力して下さい。"))

try:
    n = 10 / input_number
except ZeroDivisionError as zde:
    print(zde)
except TypeError as te:
    print(te)
else:
    print(n)
