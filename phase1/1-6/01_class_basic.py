"""
・BankAccount（銀行口座）クラスを定義する
- 属性: owner（名義人）, balance（残高、デフォルト0）
- メソッド:
  - deposit(amount): 残高を増やす
  - withdraw(amount): 残高を減らす（残高不足のときは print
でエラーを出す）
  - show(): "owner: ○○, balance: ○○円" と表示する
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


"""
・インスタンスを作って deposit / withdraw / show を呼び出して動作確認する
"""
account = BankAccount("Shinoara Ryota")

account.deposit(100)
account.withdraw(200)

account.show()
