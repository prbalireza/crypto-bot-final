# telegram_bot.py

import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_signal_to_telegram(signal):
    if signal:
        message = f"[{signal['market']}] - {signal['symbol']}\nSignal: {signal['action']}\nEntry: {signal['entry']:.2f}\nTargets: {signal['targets'][0]:.2f} / {signal['targets'][1]:.2f}\nStop: {signal['stop_loss']:.2f}\nLeverage: {signal['leverage']}"
        url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
        payload = {'chat_id': TELEGRAM_CHAT_ID, 'text': message, 'parse_mode': 'Markdown'}
        requests.post(url, data=payload)
