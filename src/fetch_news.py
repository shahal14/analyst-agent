from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_ai_news(page_size=100, max_pages=1):
    if NEWS_API_KEY is None:
        raise ValueError("NEWS_API_KEY not set in environment (.env)")

    articles = []
    base_url = "https://newsapi.org/v2/everything"

    for page in range(1, max_pages + 1):
        params = {
            "q": "\"AI startup\" OR \"artificial intelligence\" OR \"AI company\"",
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": page_size,
            "page": page,
            "apiKey": NEWS_API_KEY,
        }

        resp = requests.get(base_url, params=params, timeout=20)
        resp.raise_for_status()
        data = resp.json()

        batch = data.get("articles", [])
        if not batch:
            break

        articles.extend(batch)

    os.makedirs("data", exist_ok=True)
    with open("data/raw_articles.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2)

    return articles
