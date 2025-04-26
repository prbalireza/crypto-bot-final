# main.py

from signal_generator import generate_signal
from telegram_bot import send_signal_to_telegram

watchlist = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'XRP/USDT', 'BNB/USDT', 'DOGE/USDT', 'ADA/USDT', 'SHIB/USDT', 'DOT/USDT', 'LTC/USDT']

if __name__ == '__main__':
    for symbol in watchlist:
        signal = generate_signal(symbol)
        send_signal_to_telegram(signal)
