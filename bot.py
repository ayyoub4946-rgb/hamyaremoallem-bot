import os
import random
import requests
import jdatetime
from datetime import datetime

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "-1003725162783"

# شرط ساعت ایران
today_iran = jdatetime.datetime.now()
hour_iran = today_iran.hour
minute_iran = today_iran.minute

if 7 <= hour_iran < 8 or (hour_iran == 8 and minute_iran <= 30):
    today = jdatetime.date.today()
    
    # ترتیب درست روزهای هفته (شنبه = 0)
    weekdays = ["شنبه", "یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه"]
    months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
    
    day_name = weekdays[today.weekday()]  # الان درست کار می‌کند
    month_name = months[today.month - 1]
    date_text = f"{day_name} {today.day} {month_name} {today.year}"
    
    quotes = [
        "تلاش امروز، موفقیت فرداست.",
        "دانایی، سرمایه‌ای است که هرگز از بین نمی‌رود.",
        "معلمی، هنر ساختن آینده است.",
        "هر روز فرصتی تازه برای یادگیری و رشد است.",
        "هیچ تلاشی بی‌ثمر نمی‌ماند.",
        "موفقیت از پشتکار متولد می‌شود.",
        "امروز بهترین فرصت برای شروع دوباره است.",
        "آینده را کسانی می‌سازند که امروز می‌آموزند."
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
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    })
else:
    print(f"Skipped sending at hour {hour_iran}:{minute_iran}")
