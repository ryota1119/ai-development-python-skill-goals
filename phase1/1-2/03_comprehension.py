"""
1. リスト内包表記

1〜10の2乗のリストを内包表記で作り、表示する
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""

numbers = [i**2 for i in range(1, 11)]
print(numbers)

"""
2. 条件付きリスト内包表記

1〜20の偶数だけのリストを内包表記で作り、表示する

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

ヒント： [x for x in range(...) if x % 2 == 0] の形

"""

numbers = [i for i in range(1, 21) if i % 2 == 0]
print(numbers)

"""
3. 辞書内包表記

prices = {"apple": 100, "banana": 200, "cherry": 300}

値が150以上のものだけを残した辞書を内包表記で作り、表示する

{'banana': 200, 'cherry': 300}

ヒント：
- {k: v for k, v in dict.items() if ...} の形
- Rubyの select / filter を1行で書く感覚。Goには相当構文なし
"""

prices = {"apple": 100, "banana": 200, "cherry": 300}
new_dict = {k: v for k, v in prices.items() if v >= 150}
print(new_dict)
