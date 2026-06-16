"""
以下の EmailSender クラスを対象に、モックを使ったテストを書いてください。

条件：
- smtplib.SMTP を unittest.mock.patch でモックに差し替える
- send() が True を返すことを確認するテストを書く
- smtp.sendmail が正しい引数で呼ばれたかを assert_called_once_with で検証する
"""

import smtplib
from unittest import TestCase
from unittest.mock import patch


class EmailSender:
    def send(self, to: str, subject: str, body: str) -> bool:
        with smtplib.SMTP("localhost") as smtp:
            smtp.sendmail("from@example.com", to, f"Subject: {subject}\n\n{body}")
        return True


class TestEmailSender(TestCase):
    def test_send(self):
        with patch("smtplib.SMTP") as mock_smtp:
            instance = mock_smtp.return_value.__enter__.return_value

            sender = EmailSender()
            result = sender.send(
                to="to@example.com", subject="テスト件名", body="本文です"
            )

            self.assertTrue(result)

            instance.sendmail.assert_called_once_with(
                "from@example.com", "to@example.com", "Subject: テスト件名\n\n本文です"
            )
