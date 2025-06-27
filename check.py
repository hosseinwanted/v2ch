import requests
import os

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
CONFIG_URL = "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub13.txt"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {
        'chat_id': CHAT_ID,
        'text': message[:4000]  # محدودیت تلگرام
    }
    response = requests.post(url, params=params)
    print(f"Telegram response: {response.status_code}")  # برای دیباگ

# تست ارسال
if __name__ == "__main__":
    print("Starting script...")
    test_message = "✅ ربات فعال شد\n" + "="*30 + "\nTest message"
    send_to_telegram(test_message)
