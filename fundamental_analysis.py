# fundamental_analysis.py

from data_fetcher import get_trending_coins, get_market_sentiment, get_latest_news

def analyze_fundamentals():
    trending = get_trending_coins()
    sentiment = get_market_sentiment()
    news = get_latest_news()

    # بررسی فقط اخبار با تاثیر مثبت (impact == 'positive')
    positive_news = [n for n in news if n.get('impact') == 'positive']

    sentiment_score = len(positive_news) + int(sentiment.get('followers', 0)) // 1000

    return {
        'trending': trending,
        'sentiment_score': sentiment_score,
    }
