from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram_message(message, chat_id):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(telegram_url, json=payload)

@app.route('/alert' , methods=['POST'])
def handle_alert():
    data = request.json
    message = data.get('message', 'Kein Text empfangen.')

    send_telegram_message(f"📈 Neues Signal:\n{message}", CHAT_ID)
    return {'status': 'ok'}

@app.route('/', methods=['GET'])
def home():
    return "✅ Bot läuft!"

if __name__ == '__main__':
    send_telegram_message("✅ Test: Bot läuft! Verbindung funktioniert.", CHAT_ID)
    app.run(host='0.0.0.0', port=8080)
