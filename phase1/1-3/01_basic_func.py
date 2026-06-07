# 1. 整数を受け取り、その絶対値を返す関数 absolute_value()
#    ※ abs() 組み込み関数は使わずに自分で実装すること


def absolute_value(num: int) -> int:
    return num if num >= 0 else -num


print(absolute_value(4))
print(absolute_value(-4))

# 2. リストと値を受け取り、そのリスト内での出現回数を返す関数 count_occurrences()
#    例: count_occurrences([1, 2, 2, 3], 2) -> 2


def count_occurrences(arr: list, target: int) -> int:
    return arr.count(target)


arr = [1, 2, 2, 3]
target = 2

print(count_occurrences(arr, target))

# 3. 文字列を受け取り、母音（a, e, i, o, u）の数を返す関数 count_vowels()
#    例: count_vowels("hello") -> 2


def count_vowels(text: str) -> int:
    count = 0
    for char in text:
        if char in ("a", "e", "i", "o", "u"):
            count += 1
    return count


text = "hello"
print(count_vowels(text))
