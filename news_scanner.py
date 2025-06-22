# news_scanner.py

import feedparser
from textblob import TextBlob

RSS_FEEDS = [
    "http://feeds.reuters.com/reuters/businessNews",
    "http://rss.cnn.com/rss/money_latest.rss",
    "https://www.marketwatch.com/rss/topstories",
    "https://www.investing.com/rss/news_25.rss"
]

def scan_news_sentiment():
    print("📰 Scanning news feeds for sentiment...\n")
    headlines = []
    for url in RSS_FEEDS:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:  # Limit to 5 per source
                headlines.append(entry.title)
        except Exception as e:
            print(f"Error parsing feed {url}: {e}")

    polarity_scores = []
    for headline in headlines:
        score = TextBlob(headline).sentiment.polarity
        polarity_scores.append(score)
        print(f"🧠 {headline} --> Score: {round(score, 3)}")

    avg_score = round(sum(polarity_scores) / len(polarity_scores), 3) if polarity_scores else 0.0
    print(f"\n🧠 Average Sentiment Score: {avg_score}")
    
    return {
        "avg_sentiment": avg_score,
        "headlines": headlines
    }
