import os
import sys
from collections import Counter
from itertools import chain

file_path = "day4/02_stdlib.py"

# 課題1: os を使ってカレントディレクトリのパスを取得して出力
print(os.getcwd())

# 課題2: os.path を使って "day4/02_stdlib.py" の拡張子を取得して出力
_, ext = os.path.splitext(file_path)
print(ext)

# 課題3: sys.version を使ってPythonのバージョンを出力
print(sys.version)

# 課題4: Counter を使って以下のリストの出現回数を集計して出力
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print(Counter(fruits))

# 課題5: chain を使って [1, 2, 3] と [4, 5, 6] を結合してループで出力
list_a = [1, 2, 3]
list_b = [4, 5, 6]

for i in chain(list_a, list_b):
    print(i)
