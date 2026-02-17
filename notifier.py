import os
import requests


def send_telegram_message(text: str) -> bool:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print(
            "[WARN] TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not set. "
            "Skipping Telegram notification."
        )
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
    }

    try:
        resp = requests.post(url, json=payload, timeout=10)
        if resp.status_code != 200:
            print(f"[ERROR] Telegram API error: {resp.status_code} - {resp.text}")
            return False
        return True
    except requests.RequestException as e:
        print(f"[ERROR] Failed to send Telegram message: {e}")
        return False
