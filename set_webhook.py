import os
import requests
from dotenv import load_dotenv

load_dotenv()


def set_webhook():
    our_url = "https://d154-88-155-179-254.ngrok-free.app/telegram/"
    telegram_url = f"https://api.telegram.org/bot{os.environ.get('TELEGRAM_BOT_TOKEN')}/setWebhook"

    data = {
        'url': our_url
    }
    response = requests.post(telegram_url, data=data)

    print(response.json())


if __name__ == '__main__':
    set_webhook()
