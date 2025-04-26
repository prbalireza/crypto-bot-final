# data_fetcher.py

import requests
from config import COINMARKETCAP_API_KEY, CRYPTOCOMPARE_API_KEY, CRYPTOPANIC_API_KEY

def get_coincap_price(symbol='bitcoin'):
    url = f'https://api.coincap.io/v2/assets/{symbol.lower()}'
    response = requests.get(url)
    data = response.json()
    if 'data' in data and 'priceUsd' in data['data']:
        price = float(data['data']['priceUsd'])
        return price
    else:
        return None

def get_trending_coins():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'data' in data:
        return [coin['name'] for coin in data['data'][:10]]  # فقط ۱۰ کوین اول بازار
    else:
        print("خطا در دریافت داده از CoinMarketCap:", data)
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
