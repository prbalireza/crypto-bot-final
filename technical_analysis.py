# technical_analysis.py

import pandas as pd
import ccxt
import ta
from config import BINANCE_API_KEY, BINANCE_SECRET_KEY

def fetch_ohlcv(symbol='BTC/USDT', timeframe='1h', limit=100):
    exchange = ccxt.binance({
        'apiKey': BINANCE_API_KEY,
        'secret': BINANCE_SECRET_KEY,
        'enableRateLimit': True,
    })
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def calculate_indicators(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    df['macd'] = ta.trend.MACD(df['close']).macd()
    df['ema50'] = ta.trend.EMAIndicator(df['close'], window=50).ema_indicator()
    df['adx'] = ta.trend.ADXIndicator(df['high'], df['low'], df['close']).adx()
    df['bb_high'] = ta.volatility.BollingerBands(df['close']).bollinger_hband()
    df['bb_low'] = ta.volatility.BollingerBands(df['close']).bollinger_lband()
    df = calculate_fibonacci(df)
    return df

def calculate_fibonacci(df):
    high = df['high'].max()
    low = df['low'].min()
    diff = high - low
    df['fib_0.382'] = high - diff * 0.382
    df['fib_0.5'] = high - diff * 0.5
    df['fib_0.618'] = high - diff * 0.618
    return df
