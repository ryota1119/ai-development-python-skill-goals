"""
問題 1 — 成績集計

以下の点数リストを使って：

scores = [45, 82, 91, 67, 55, 78, 34, 88, 72, 60]

1. 平均点を計算して表示する
2. 内包表記で「70点以上」の点数だけのリストを作り、表示する
3. 各点数を if/elif/else で判定し、{"優": n人, "良": n人, "可": n人, "不可":
n人} という辞書を作って表示する

期待する出力例：
平均: 67.2
70点以上: [82, 91, 78, 88, 72]
成績分布: {'優': 2, '良': 4, '可': 2, '不可': 2}
"""

scores = [45, 82, 91, 67, 55, 78, 34, 88, 72, 60]

# 1. 平均点を計算して表示する
print(sum(scores) / len(scores))

# 2. 内包表記で「70点以上」の点数だけのリストを作り、表示する
scores_upper_than_70 = [i for i in scores if i >= 70]
print(scores_upper_than_70)

# 3. 各点数を if/elif/else で判定し、{"優": n人, "良": n人, "可": n人, "不可": n人} という辞書を作って表示する
grade_count = {"優": 0, "良": 0, "可": 0, "不可": 0}

for i in scores:
    if i >= 90:
        grade_count["優"] += 1
    elif i >= 70:
        grade_count["良"] += 1
    elif i >= 50:
        grade_count["可"] += 1
    else:
        grade_count["不可"] += 1
print(grade_count)

"""
問題 2 — 単語カウンター

以下の文章から単語の出現回数を数える：

text = "apple banana apple cherry banana apple grape cherry"

1. split() で単語リストに分割する
2. 辞書を使って各単語の出現回数をカウントする
3. 出現回数が2以上の単語だけを辞書内包表記で抽出して表示する

期待する出力例：
全カウント: {'apple': 3, 'banana': 2, 'cherry': 2, 'grape': 1}
2回以上: {'apple': 3, 'banana': 2, 'cherry': 2}
"""

text = "apple banana apple cherry banana apple grape cherry"

# 1. split() で単語リストに分割する
word_list = text.split()

# 2. 辞書を使って各単語の出現回数をカウントする
word_dict = {}
for v in word_list:
    word_dict[v] = word_dict.get(v, 0) + 1
print(word_dict)

# 3. 出現回数が2以上の単語だけを辞書内包表記で抽出して表示する
print({k: v for k, v in word_dict.items() if v >= 2})
