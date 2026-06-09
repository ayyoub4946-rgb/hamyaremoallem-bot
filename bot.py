import requests
from datetime import datetime

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHANNEL_ID"

today = datetime.now().strftime("%Y-%m-%d")

message = f"""
📅 تقویم روز

🗓 {today}

🌸 صبح بخیر فرهنگیان گرامی

💡 جمله امروز:
«هر روز فرصتی تازه برای یادگیری و رشد است.»

📚 همیار معلم
@HamyareMoallem
"""

url = f"https://api.telegram.org/bot{8957022702:AAGyd-pYfaI_QgHXmUr_KSHu_s3jRamhpv0}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
