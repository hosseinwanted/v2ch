import requests
import os

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
CONFIG_URL = "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub13.txt"

def check_configs():
    response = requests.get(CONFIG_URL)
    if response.status_code == 200:
        configs = response.text
        send_to_telegram(configs)

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {
        'chat_id': CHAT_ID,
        'text': message[:4000]  # محدودیت تلگرام
    }
    requests.post(url, params=params)

if __name__ == "__main__":
    check_configs()
