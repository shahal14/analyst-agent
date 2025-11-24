import os
import sys
from pathlib import Path

# Ensure src path is available when running from repo root
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from fetch_news import fetch_ai_news
from deduplicate import deduplicate_articles
from hype_filter import hype_filter
from extract_structured import extract_structured
from save_output import save_to_csv

from tqdm import tqdm


def run_pipeline(max_pages=1):
    print("MAIN.PY STARTED")

    print("🔍 Fetching AI startup news...")
    articles = fetch_ai_news(page_size=100, max_pages=max_pages)
    print(f"Fetched {len(articles)} articles.")

    print("\n🧹 Deduplicating articles...")
    unique = deduplicate_articles(articles)
    print(f"Remaining after dedupe: {len(unique)}")

    print("\n📊 Applying hype filter (quality)...")
    filtered = [a for a in unique if hype_filter(a)]
    print(f"Remaining after hype filter: {len(filtered)}")

    print("\n🤖 Extracting structured JSON with Gemini...")
    results = []
    for art in tqdm(filtered):
        text = art.get('content') or art.get('description') or art.get('title') or ""
        extracted = extract_structured(text)
        if extracted:
            extracted['_source_title'] = art.get('title')
            extracted['_source_url'] = art.get('url')
            extracted['_publishedAt'] = art.get('publishedAt')
            results.append(extracted)

    print(f"\nStructured records: {len(results)}")

    print("\n💾 Saving to CSV...")
    df = save_to_csv(results)
    print(f"Saved cleaned CSV with {len(df)} rows to data/cleaned_output.csv")


if __name__ == '__main__':
    pages = 1
    if len(sys.argv) > 1:
        try:
            pages = int(sys.argv[1])
        except Exception:
            pages = 1

    run_pipeline(max_pages=pages)
