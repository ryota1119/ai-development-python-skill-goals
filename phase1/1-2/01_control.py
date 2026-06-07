"""
1. input() で点数（0〜100）を受け取り、以下のように判定して表示する
90以上 → 優
70以上 → 良
50以上 → 可
50未満 → 不可
"""

point = int(input("点数を入力して下さい: "))
if point >= 90:
    print("優")
elif point >= 70:
    print("良")
elif point >= 50:
    print("可")
else:
    print("不可")

"""
2. for ループで1〜10の合計を計算して表示する
"""
total = 0
for i in range(1, 11):
    total += i

print(total)

"""
3. while を使って1〜10を表示する。ただし 5はスキップ、8で終了する
"""
num = 1
while True:
    if num > 8:
        break
    if num == 5:
        num += 1
        continue
    print(num)
    num += 1
