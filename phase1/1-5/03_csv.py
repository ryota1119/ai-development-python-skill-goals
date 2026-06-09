"""
1. csv モジュールを使って以下のデータを  に書き込む
 ヘッダー: name, score
 データ  : Alice/85, Bob/92, Carol/78
"""

import csv

file_name = "./phase1/1-5/sample.csv"

scores = {"Alice": 85, "Bob": 92, "Carol": 78}

with open(file_name, "w", newline="", encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    for name, score in scores.items():
        writer.writerow([name, score])

"""
2. 書き込んだ scores.csv を読み込んで、1行ずつ print() する
"""

with open(file_name, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

"""
3. DictReader を使って読み込み、name と score をそれぞれ取り出して print() する
"""
with open(file_name, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["score"])
