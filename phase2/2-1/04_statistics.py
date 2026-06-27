import numpy as np

# テーマ：統計関数（mean / std / sum / max / min）+ axis

# 1. 1次元配列で基本の統計
# - a = np.array([2, 4, 6, 8, 10]) を作り
# - 合計 a.sum() / 平均 a.mean() / 標準偏差 a.std() / 最大 a.max() / 最小 a.min()
# を出力

a = np.array([2, 4, 6, 8, 10])
print(a)

print(a.sum())
print(a.mean())
print(a.std())
print(a.max())
print(a.min())

# 2. 2次元配列で全体の統計
# - m = np.arange(1, 13).reshape(3, 4)（3×4）を作り
# - m.sum() で 全要素の合計 を出力

m = np.arange(1, 13).reshape(3, 4)
print(m)

print(m.sum())

# 3. axis（軸）を指定した集計 ← Phase2 で一番重要
# - m.sum(axis=0)（列ごとの合計）と m.sum(axis=1)（行ごとの合計）を出力
# - 👉 結果の形がどう変わるか観察する

print(m.sum(axis=0))
print(m.sum(axis=1))
