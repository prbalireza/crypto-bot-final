# data_fetcher.py

import ccxt
import requests
from config import BINANCE_API_KEY, BINANCE_SECRET_KEY, COINMARKETCAP_API_KEY, CRYPTOCOMPARE_API_KEY, CRYPTOPANIC_API_KEY

def fetch_ohlcv(symbol='BTC/USDT', timeframe='1h', limit=100):
    exchange = ccxt.binance({
        'apiKey': BINANCE_API_KEY,
        'secret': BINANCE_SECRET_KEY,
        'enableRateLimit': True,
    })
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    return ohlcv

def get_trending_coins():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'data' in data:
        return [coin['symbol'] + '/USDT' for coin in data['data'][:10]]
    else:
        return []

def get_market_sentiment():
    url = f'https://min-api.cryptocompare.com/data/social/coin/latest?api_key={CRYPTOCOMPARE_API_KEY}&fsym=BTC'
    response = requests.get(url)
    data = response.json()
    return data['Data']

def get_latest_news():
    url = f'https://cryptopanic.com/api/v1/posts/?auth_token={CRYPTOPANIC_API_KEY}&public=true'
    response = requests.get(url)
    data = response.json()
    return data['results']
