# signal_generator.py

from technical_analysis import prepare_dataframe, calculate_indicators
from fundamental_analysis import analyze_fundamentals

def generate_signal(symbol='BTC/USDT', timeframe='1h'):
    df = prepare_dataframe(symbol, timeframe)
    df = calculate_indicators(df)
    latest = df.iloc[-1]
    fundamentals = analyze_fundamentals()

    if latest['rsi'] < 30 and latest['macd'] > 0 and latest['close'] > latest['ema50'] and fundamentals['sentiment_score'] > 0:
        return {
            'market': 'SPOT',
            'symbol': symbol,
            'action': 'BUY',
            'entry': latest['close'],
            'targets': [latest['close'] * 1.02, latest['close'] * 1.04],
            'stop_loss': latest['close'] * 0.98,
            'leverage': 'None'
        }
    elif latest['rsi'] > 70 and latest['macd'] < 0 and latest['close'] < latest['ema50']:
        return {
            'market': 'SPOT',
            'symbol': symbol,
            'action': 'SELL',
            'entry': latest['close'],
            'targets': [latest['close'] * 0.98, latest['close'] * 0.96],
            'stop_loss': latest['close'] * 1.02,
            'leverage': 'None'
        }
    else:
        return None
