import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY not set in environment (.env)")

genai.configure(api_key=GEMINI_API_KEY)

# WORKING MODEL FOR YOUR API KEY
model = genai.GenerativeModel("models/gemini-flash-latest")



def _build_prompt(article_text: str) -> str:
    return f"""
You are an AI analyst that extracts structured JSON from news articles.

Return ONLY a valid JSON object with keys:
- company_name
- category
- sentiment_score
- is_funding_news

Article:
{article_text}

Respond with JSON only.
"""


def extract_structured(article_text: str):
    """Extract structured JSON using Gemini."""
    prompt = _build_prompt(article_text)

    try:
        response = model.generate_content(prompt)

        # Extract text safely
        raw = response.text.strip()

        # Remove ```json fences
        if raw.startswith("```"):
            lines = raw.split("\n")
            raw = "\n".join(lines[1:-1]).strip()

        start = raw.find("{")
        end = raw.rfind("}")
        if start != -1 and end != -1:
            raw = raw[start:end + 1]

        data = json.loads(raw)

        # Fix sentiment to float
        if "sentiment_score" in data:
            try:
                data["sentiment_score"] = float(data["sentiment_score"])
            except:
                data["sentiment_score"] = None

        # Fix boolean
        if isinstance(data.get("is_funding_news"), str):
            v = data["is_funding_news"].lower()
            data["is_funding_news"] = v in ("true", "yes")

        return data

    except Exception as e:
        print("Gemini extraction error:", e)
        return None
