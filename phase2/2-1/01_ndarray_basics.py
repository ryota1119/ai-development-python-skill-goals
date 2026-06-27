import numpy as np

# 1. Pythonのリスト [[1, 2, 3], [4, 5, 6]] から NumPy配列を作る
data = [[1, 2, 3], [4, 5, 6]]
arr = np.array(data)

# 2. その配列の以下を print で確認する：
# - shape（形状）
# - dtype（要素の型）
# - ndim（次元数）
# - size（要素数の合計）
print(arr.shape)
print(arr.dtype)
print(arr.ndim)
print(arr.size)

# 3. reshape で形状を変える（例: 2×3 → 3×2、または 1次元の arange から作って reshape）
print(arr.reshape(-1, 2))

# 4. 便利な生成関数を1つずつ試す：
# - np.zeros((2, 3)) / np.ones((2, 3)) / np.arange(0, 10, 2) / np.linspace(0, 1, 5)
print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))
