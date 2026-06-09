"""
・インスタンスメソッド（既存）に加えて以下を追加する


・クラスメソッド
- BankAccount.create_empty(owner) — balance=0 のインスタンスを返す
  （@classmethod を使う）

・スタティックメソッド
- BankAccount.is_valid_amount(amount) — amount が 1 以上の整数なら True
を返す
  （@staticmethod を使う）

・動作確認
- create_empty でインスタンスを作って show() する
- is_valid_amount(500) と is_valid_amount(-10) の結果を print する
"""

from typing import Self


class BankAccount:
    def __init__(self, owner: str, balance: int = 0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        if self.balance < amount:
            print("残高が不足しています。")
            return
        self.balance -= amount

    def show(self) -> None:
        print(f"owner: {self.owner}, balance: {self.balance}円")

    """
    ・クラスメソッド
    - BankAccount.create_empty(owner) — balance=0 のインスタンスを返す
      （@classmethod を使う）
    """

    @classmethod
    def create_empty(cls, owner: str) -> Self:
        return cls(owner)

    """
    ・スタティックメソッド
    - BankAccount.is_valid_amount(amount) — amount が 1 以上の整数なら True
    を返す
      （@staticmethod を使う）
    """

    @staticmethod
    def is_valid_amount(amount: int) -> bool:
        return amount >= 1


account = BankAccount.create_empty("Ryota")
account.show()

print(BankAccount.is_valid_amount(500))
print(BankAccount.is_valid_amount(-10))
