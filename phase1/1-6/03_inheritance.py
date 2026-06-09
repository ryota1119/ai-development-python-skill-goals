from typing import Self

"""
・BankAccount を親クラスとして SavingsAccount（貯蓄口座）を定義する
- 追加属性: interest_rate（金利、float）
- add_interest() メソッド: balance に interest_rate
を掛けた利息を残高に加算する
- show() をオーバーライドして、金利も一緒に表示する
  例: "owner: Ryota, balance: 1050円, interest_rate: 5.0%"

・動作確認
- SavingsAccount("Ryota", 1000, 0.05) でインスタンスを作る
- add_interest() を呼んで show() する
"""


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

    @classmethod
    def create_empty(cls, owner: str) -> Self:
        return cls(owner)

    @staticmethod
    def is_valid_amount(amount: int) -> bool:
        return amount >= 1


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: int, interest_rate: float) -> None:
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self) -> None:
        self.balance += int(self.balance * self.interest_rate)

    def show(self) -> None:
        print(
            f"owner: {self.owner}, balance: {self.balance}円, interest_rate: {self.interest_rate * 100}%"
        )


account = SavingsAccount("Ryota", 1000, 0.05)
account.add_interest()
account.show()
