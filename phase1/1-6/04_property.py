"""
・BankAccount に @property を使って以下を追加する

- balance プロパティ（getter）: _balance を返す
- balance セッター: amount が 0 未満なら ValueError を raise する
  （属性名は _balance に変更する）

・動作確認
- 正常系: BankAccount("Ryota", 1000) を作って balance を print する
- 異常系: balance に -100 をセットしようとして ValueError を捕捉して print
する
"""

from typing import Self


class BankAccount:
    def __init__(self, owner: str, balance: int = 0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self._balance += amount

    def withdraw(self, amount: int) -> None:
        if self._balance < amount:
            print("残高が不足しています。")
            return
        self._balance -= amount

    def show(self) -> None:
        print(f"owner: {self.owner}, balance: {self._balance}円")

    @classmethod
    def create_empty(cls, owner: str) -> Self:
        return cls(owner)

    @staticmethod
    def is_valid_amount(amount: int) -> bool:
        return amount >= 1

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, value: int) -> None:
        if value < 0:
            raise ValueError("残高は0以上である必要があります")
        self._balance = value


acc = BankAccount("Ryota", 1000)
print(acc.balance)

try:
    acc.balance = -100
except ValueError as e:
    print(e)
