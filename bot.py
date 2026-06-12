import os
import requests
from datetime import datetime, timezone

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "-1003725162783"

utc_now = datetime.now(timezone.utc)
iran_now = utc_now.replace(hour=(utc_now.hour + 3) % 24, minute=utc_now.minute + 30)

message = f"""
🔧 **تست ربات - همیار معلم**

🕐 **UTC:** {utc_now.strftime('%H:%M:%S')}
🕒 **ایران:** {iran_now.strftime('%H:%M:%S')}

ربات در این ساعت اجرا شده است.
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
r = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message,
    "parse_mode": "HTML"
})

print(r.status_code, r.text)
