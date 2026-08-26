# Day 76: Datetime Operations
from datetime import datetime, timedelta, timezone

now = datetime.now(timezone.utc)
print("Current UTC:", now.isoformat())

formatted = now.strftime("%A, %B %d, %Y - %H:%M:%S UTC")
print("Formatted string:", formatted)

future = now + timedelta(days=100)
print("Date 100 days from now:", future.strftime("%Y-%m-%d"))
