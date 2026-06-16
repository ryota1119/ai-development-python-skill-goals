"""
以下の Authenticator クラスに対してテストを書き、カバレッジ100%を目指してください。

class Authenticator:
  def __init__(self) -> None:
      self.users: dict[str, str] = {"admin": "pass123"}

  def login(self, username: str, password: str) -> str:
      if username not in self.users:
          return "user_not_found"
      if self.users[username] != password:
          return "wrong_password"
      return "ok"

条件：
- pytest-cov を使ってカバレッジを計測する
- login() の3つの分岐（user_not_found / wrong_password /
ok）をすべてカバーするテストを書く
- 実行コマンド：

uv run pytest phase1/1-8/05_coverage.py --cov=phase1/1-8/05_coverage
--cov-report=term-missing -v
"""

from unittest import TestCase


class Authenticator:
    def __init__(self) -> None:
        self.users: dict[str, str] = {"admin": "pass123"}

    def login(self, username: str, password: str) -> str:
        if username not in self.users:
            return "user_not_found"
        if self.users[username] != password:
            return "wrong_password"
        return "ok"


class TestAuthenticator(TestCase):
    def test_login_ok(self):
        authenticator = Authenticator()
        self.assertEqual(authenticator.login("admin", "pass123"), "ok")

    def test_login_user_not_found(self):
        authenticator = Authenticator()
        self.assertEqual(authenticator.login("user", "pass123"), "user_not_found")

    def test_login_wrong_password(self):
        authenticator = Authenticator()
        self.assertEqual(authenticator.login("admin", "pass456"), "wrong_password")
