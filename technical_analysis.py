# technical_analysis.py

import pandas as pd
import ta
from data_fetcher import fetch_ohlcv

def prepare_dataframe(symbol, timeframe='1h'):
    ohlcv = fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def calculate_fibonacci(df):
    high = df['high'].max()
    low = df['low'].min()
    diff = high - low
    df['fib_0.382'] = high - diff * 0.382
    df['fib_0.5'] = high - diff * 0.5
    df['fib_0.618'] = high - diff * 0.618
    return df

def calculate_indicators(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    df['macd'] = ta.trend.MACD(df['close']).macd()
    df['ema50'] = ta.trend.EMAIndicator(df['close'], window=50).ema_indicator()
    df['ema200'] = ta.trend.EMAIndicator(df['close'], window=200).ema_indicator()
    df['adx'] = ta.trend.ADXIndicator(df['high'], df['low'], df['close']).adx()
    bb = ta.volatility.BollingerBands(df['close'])
    df['bb_high'] = bb.bollinger_hband()
    df['bb_low'] = bb.bollinger_lband()
    df = calculate_fibonacci(df)
    return df
