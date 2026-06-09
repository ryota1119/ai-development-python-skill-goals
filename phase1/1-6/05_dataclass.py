"""
@dataclass を使って Product（商品）クラスを定義する。

┌────────────┬──────┬────────────┐
│ フィールド │  型  │ デフォルト │
├────────────┼──────┼────────────┤
│ name       │ str  │ なし       │
├────────────┼──────┼────────────┤
│ price      │ int  │ なし       │
├────────────┼──────┼────────────┤
│ in_stock   │ bool │ True       │
└────────────┴──────┴────────────┘

メソッドを1つ追加：
- discounted_price(rate: float) -> int：price * (1 - rate) を int で返す（例：rate=0.1
なら10%引き）

動作確認（ファイル末尾に書く）：
p = Product("リンゴ", 200)
print(p)                          # → Product(name='リンゴ', price=200, in_stock=True)
print(p.discounted_price(0.1))    # → 180
"""

from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: int
    in_stock: bool = True

    def discounted_price(self, rate: float) -> int:
        return int(self.price * (1 - rate))


p = Product("りんご", 200)
print(p)
print(p.discounted_price(0.1))
