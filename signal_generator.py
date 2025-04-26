# signal_generator.py

from technical_analysis import fetch_ohlcv, calculate_indicators
from fundamental_analysis import analyze_fundamentals

def generate_signal(symbol='BTC/USDT'):
    df = fetch_ohlcv(symbol)
    df = calculate_indicators(df)
    latest = df.iloc[-1]

    fundamentals = analyze_fundamentals()

    if (latest['rsi'] < 30 and latest['macd'] > 0 and latest['close'] > latest['ema50']
        and fundamentals['sentiment_score'] > 0
        and latest['fib_0.5'] < latest['close'] < latest['fib_0.382']):
        
        market_type = 'FUTURES' if latest['adx'] > 25 else 'SPOT'
        leverage = '10x' if market_type == 'FUTURES' else 'None'

        return {
            'market': market_type,
            'symbol': symbol,
            'action': 'BUY',
            'entry': latest['close'],
            'targets': [latest['close'] * 1.02, latest['close'] * 1.04],
            'stop_loss': latest['close'] * 0.98,
            'leverage': leverage
        }
    else:
        return None
