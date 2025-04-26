# data_fetcher.py

import ccxt
import requests
from config import BINANCE_API_KEY, BINANCE_SECRET_KEY, COINMARKETCAP_API_KEY, CRYPTOCOMPARE_API_KEY, CRYPTOPANIC_API_KEY

def get_binance_price(symbol='BTC/USDT'):
    exchange = ccxt.binance({
        'apiKey': BINANCE_API_KEY,
        'secret': BINANCE_SECRET_KEY,
        'enableRateLimit': True,
    })
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

def get_trending_coins():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/trending/latest'
    headers = {'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return [coin['name'] for coin in data['data']]

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
