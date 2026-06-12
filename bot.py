import os
import requests
from datetime import datetime, timezone

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "-1003725162783"

utc_now = datetime.now(timezone.utc)

# محاسبه زمان ایران (UTC+3:30)
iran_hour = utc_now.hour + 3
iran_minute = utc_now.minute + 30
if iran_minute >= 60:
    iran_minute -= 60
    iran_hour += 1
iran_hour = iran_hour % 24

message = f"""🔧 تست مستقیم ربات - همیار معلم

🕐 UTC: {utc_now.strftime('%H:%M:%S')}
🕒 ایران: {iran_hour:02d}:{iran_minute:02d}

ربات با موفقیت کار می‌کند."""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
r = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message,
    "parse_mode": "HTML"
})

print(r.status_code, r.text)
