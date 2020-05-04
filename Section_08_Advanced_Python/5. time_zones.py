from datetime import datetime, timezone

today = datetime.now(timezone.utc)
print(today)
print(today.strftime('%Y-%m-%d %H:%M:%S'))
