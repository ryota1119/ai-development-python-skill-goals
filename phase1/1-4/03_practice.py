from collections import Counter

logs = [
    "2024-01-15 ERROR failed to connect",
    "2024-01-15 INFO server started",
    "2024-01-16 ERROR timeout",
    "2024-01-16 INFO request received",
    "2024-01-16 ERROR disk full",
    "2024-01-17 INFO shutdown",
]

# 課題1: ERROR のログだけ抽出して出力
error_logs = [log for log in logs if "ERROR" in log]
print(error_logs)

# 課題2: 日付ごとのログ件数を集計して出力
days_list = [log.split(" ", 2)[0] for log in logs]
print(Counter(days_list))

# 課題3: ログレベル（ERROR / INFO）ごとの件数を集計して出力
status_list = [log.split(" ", 2)[1] for log in logs]
print(Counter(status_list))
