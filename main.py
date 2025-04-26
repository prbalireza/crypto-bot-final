# main.py

from signal_generator import generate_signal
from telegram_bot import send_signal_to_telegram

watchlist = ['bitcoin', 'ethereum', 'solana', 'ripple', 'binance-coin', 'dogecoin', 'cardano', 'shiba-inu', 'polkadot', 'litecoin']


if __name__ == '__main__':
    for symbol in watchlist:
        signal = generate_signal(symbol)
        send_signal_to_telegram(signal)
