import numpy as np

# 以下を実装してください。出力は print で確認します。

# 1. 要素ごとの四則演算
#   - a = np.array([1, 2, 3])、b = np.array([10, 20, 30]) を作り、a + b / a - b / a * b
# / a / b を試す
#   - 👉 Ruby/PHP の配列と違い、a * b がループなしで要素ごとに掛かる点を体感

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 2. スカラーとのブロードキャスト
#   - a * 2 や a + 100 のように、配列とスカラーの演算を試す

print(a * 2)
print(a + 100)

# 3. 形の違う配列同士のブロードキャスト
#   - m = np.arange(6).reshape(2, 3)（2×3）と v = np.array([10, 20, 30])（長さ3）を足す
#   - 👉 (2,3) + (3,) がなぜ成立するか、出力を見て考える

m = np.arange(6).reshape(2, 3)
v = np.array([10, 20, 30])

print(m, v)
print(m + v)
# (2,3) + (3,) がなぜ成立するか考察
# 行列の計算と似ている

# 4. 行列積
#   - A = np.array([[1, 2], [3, 4]])、B = np.array([[5, 6], [7, 8]]) を作り
#   - 要素ごとの積 A * B と 行列積 A @ B の違いを並べて出力

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A * B)
print(A @ B)
