# 1. lambda を使って以下を実装してください
#    - 2つの数値を受け取り、大きい方を返す lambda: larger

larger = lambda x, y: x if x > y else y
print(larger(2, 5))

#    - 文字列を受け取り、文字数を返す lambda: str_len

str_len = lambda text: len(text)
print(str_len("Hello, Python!"))

# 2. sorted() + lambda でソートしてください
#    - 以下のリストを「年齢の昇順」でソート
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Carol", "age": 35},
]

sorted_people = sorted(people, key=lambda profile: profile["age"])
print(sorted_people)

#    - 以下のリストを「文字列の長さ昇順」でソート
words = ["banana", "apple", "kiwi", "strawberry"]

sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)

# 3. map() と filter() を使ってください
#    - numbers = [1, 2, 3, 4, 5] の各要素を2乗した新しいリストを作る（map使用）
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda num: num**2, numbers))
print(squared_numbers)

#    - numbers から偶数だけ取り出すリストを作る（filter使用）
filterd_numbers = list(filter(lambda num: num % 2 == 0, numbers))
print(filterd_numbers)
