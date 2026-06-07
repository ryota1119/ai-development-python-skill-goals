# 1. 挨拶文を返す関数 greet()
#    - name: 名前（必須）
#    - greeting: 挨拶語（デフォルト: "Hello"）
#    例: greet("Alice")           -> "Hello, Alice!"
#    例: greet("Bob", "Hi")       -> "Hi, Bob!"
#    例: greet(greeting="Hey", name="Carol") -> "Hey, Carol!"


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


print(greet("Alice"))
print(greet("Bob", "Hi"))
print(greet(greeting="Hey", name="Carol"))

# 2. 価格と数量から合計金額を計算する関数 calculate_total()
#    - price: 単価（必須）
#    - quantity: 数量（デフォルト: 1）
#    - tax_rate: 税率（デフォルト: 0.1）
#    例: calculate_total(100)          -> 110.0
#    例: calculate_total(100, 3)       -> 330.0
#    例: calculate_total(100, tax_rate=0.08) -> 108.0


def calculate_total(price, quantity=1, tax_rate=0.1) -> float:
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax


print(calculate_total(100))
print(calculate_total(100, 3))
print(calculate_total(100, tax_rate=0.08))
