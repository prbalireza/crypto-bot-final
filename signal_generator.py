def generate_signal(symbol='bitcoin'):
    price = get_coincap_price(symbol)
    fundamentals = analyze_fundamentals()

    if price is not None and fundamentals['sentiment_score'] > 0:
        return {
            'market': 'SPOT',
            'symbol': symbol.upper(),
            'action': 'BUY',
            'entry': price,
            'targets': [price * 1.02, price * 1.04],
            'stop_loss': price * 0.98,
            'leverage': 'None'
        }
    else:
        return None
