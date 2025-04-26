# fundamental_analysis.py

from data_fetcher import get_market_sentiment, get_latest_news, get_trending_coins

def analyze_fundamentals():
    sentiment = get_market_sentiment()
    news = get_latest_news()
    trending = get_trending_coins()

    sentiment_score = sentiment.get('General', {}).get('Points', 0)
    positive_news = [n for n in news if n['positive_votes'] > n['negative_votes']]
    
    return {
        'sentiment_score': sentiment_score,
        'positive_news_count': len(positive_news),
        'trending_coins': trending
    }
