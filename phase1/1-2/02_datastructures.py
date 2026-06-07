"""
1. リスト操作

果物を3つ持つリストを作り、以下をすべて試す：

- 末尾に1つ追加する
- 先頭の要素を削除する
- 2番目から4番目までをスライスで取り出す
"""

fruits = ["apple", "orange", "grape"]
fruits.append("lemon")
print(fruits)

del fruits[0]
print(fruits)

new_list = fruits[1:4]
print(new_list)

"""
2. 辞書操作

以下の情報を辞書で管理し、それぞれ試す：

- 名前：自分の名前、年齢：自分の年齢、言語：["Go", "Ruby", "Python"]
- 年齢の値を更新する
- キー "language" が存在するか確認する
- 存在しないキーを get() で安全に取得する（デフォルト値付き）
"""

profile = {"name": "Ryota", "age": 30, "language": ["Go", "Ruby", "Python"]}
profile["age"] = 33
print(profile)
print("language" in profile)

void_key = profile.get("company")
print(profile.get("company", "未設定"))

"""
3. タプルとセット

# タプル（イミュータブル）
coordinates = (35.6895, 139.6917)

# セット（重複なし・順序なし）
languages = {"Go", "Ruby", "Python", "Go", "Ruby"}

上記を作り、それぞれ以下をコメントで書く：
- タプルはなぜイミュータブルなのか（どんな用途に向くか）
- セットで重複が除去されることを print で確認する
"""

coordinates = (35.6895, 139.6917)
languages = {"Go", "Ruby", "Python", "Go", "Ruby"}

# イミュータブルは不変を意味する
# 辞書のキーや、変更されたくないデータに利用され

print(languages)
