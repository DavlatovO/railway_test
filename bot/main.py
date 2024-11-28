import os
from flask import Flask, request
import requests

app = Flask(__name__)

# Environment variables for configuration
TOKEN = '8172278340:AAFdSmIBn9xtDgxcbrEDG8nFHGcm9sSOgjk'
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    chat_id = data["message"]["chat"]["id"]
    user_message = data["message"]["text"]

    # Echo the message
    send_message(chat_id, f"You said: {user_message}")

    return "OK", 200

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    # Use Railway's default port and host
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
