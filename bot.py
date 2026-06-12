import os
import random
import requests
import jdatetime

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "-1003725162783"

today = jdatetime.date.today()

weekdays = ["شنبه", "یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه"]
months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]

day_name = weekdays[today.weekday()]
month_name = months[today.month - 1]
date_text = f"{day_name} {today.day} {month_name} {today.year}"

quotes = [
    "تلاش امروز، موفقیت فرداست.",
    "دانایی، سرمایه‌ای است که هرگز از بین نمی‌رود.",
    "معلمی، هنر ساختن آینده است.",
    "هر روز فرصتی تازه برای یادگیری و رشد است.",
]

quote = random.choice(quotes)

message = f"""
🌸 <b>صبح بخیر فرهنگیان گرامی</b>

📅 <b>{date_text}</b>

💡 <b>سخن امروز:</b>
{quote}

🌱 روزی سرشار از سلامتی، آرامش و موفقیت برای شما آرزومندیم.

📚 <b>همیار معلم</b>
@HamyareMoallem
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
response = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message,
    "parse_mode": "HTML"
})

print(response.status_code)
print(response.text)
