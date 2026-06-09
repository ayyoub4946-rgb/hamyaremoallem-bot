import os
import requests
import jdatetime

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "-1003725162783"

today = jdatetime.date.today()

message = f"""
📅 تقویم روز | همیار معلم

🗓 {today.strftime('%Y/%m/%d')}

🌸 صبح بخیر فرهنگیان گرامی

💡 جمله امروز:
«هر روز فرصتی تازه برای یادگیری و رشد است.»

📚 همیار معلم
@HamyareMoallem
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
