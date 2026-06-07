import datetime
import math
import random

# 1. math で計算
# 2の10乗の平方根を計算して出力

print(math.sqrt(2**10))

# 2. random でリスト生成
# 1〜100のランダムな整数を5つリストで作る

nums = random.sample(range(1, 101), 5)
print(nums)

# 3. datetime で日付計算
# 今日の日付と、100日後の日付を出力

today = datetime.date.today()

print(today)
print(today + datetime.timedelta(days=100))
