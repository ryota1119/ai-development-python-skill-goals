"""
1. sample.txt というファイルを作成し、以下の3行を書き込む
Hello, Python!
ファイル操作の練習
3行目のテスト
"""

file_name = "./phase1/1-5/sample.txt"

with open(file_name, "w", encoding="utf-8") as f:
    f.write("Hello, Python!\nファイル操作の練習\n3行目のテスト")

"""
2. 書き込んだファイルを開いて、1行ずつ読み込んで print() する
"""

with open(file_name, "r", encoding="utf-8") as f:
    for line in f:
        print(line)

"""
3. read() と readline() / readlines() の違いを確かめる
"""

with open(file_name, "r", encoding="utf-8") as f:
    print(f.read())

with open(file_name, "r", encoding="utf-8") as f:
    print(f.readline())

with open(file_name, "r", encoding="utf-8") as f:
    print(f.readlines())
