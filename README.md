nalyst Agent — News Intelligence Automation 

This repository contains my solution for the AI/ML & Automation Internship 

The system automatically:

Fetches the latest AI startup news

Performs de-duplication across different websites

Applies a “Hype Filter” to remove low-information articles

Extracts structured JSON metadata using Google Gemini

Saves the final results into a clean CSV dataset

🚀 Features
Component	Description
News Fetching	Pulls articles from NewsAPI (AI Startup–related keywords)
De-duplication	Uses similarity + source-title keys to eliminate duplicates
Hype Filter	Removes marketing fluff articles (low information density)
LLM Extraction	Extracts company_name, category, sentiment_score, is_funding_news
Output	Saves structured results to data/cleaned_output.csv
🗂 Folder Structure
analyst-agent/
│
├── src/
│   ├── main.py
│   ├── fetch_news.py
│   ├── deduplicate.py
│   ├── hype_filter.py
│   ├── extract_structured.py
│   └── save_output.py
│
├── data/
│   ├── raw_articles.json
│   └── cleaned_output.csv
│
├── diagrams/
│   └── workflow.png (optional)
│
├── requirements.txt
├── .env (ignored)
└── README.md

🔧 Installation

Clone the repository:

git clone https://github.com/your-username/analyst-agent
cd analyst-agent


Create a virtual environment:

python -m venv venv


Activate it:

Windows:

venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Create a .env file:

NEWS_API_KEY=your_newsapi_key
GEMINI_API_KEY=your_gemini_key

▶️ Running the Pipeline

To fetch 100 articles:

python src/main.py


To fetch multiple pages:

python src/main.py 2


Output visible under:

data/cleaned_output.csv

🧠 Model Used

Using the official supported Gemini model:

models/gemini-flash-latest

📊 Workflow Diagram

                ┌────────────────────────┐
                │      Start Pipeline     │
                └────────────┬───────────┘
                             │
                             ▼
     ┌──────────────────────────────────────────────┐
     │        1. Fetch AI News (NewsAPI)            │
     │ - Query: "AI startup", "AI company"          │
     │ - Multiple pages                             │
     │ - Store raw data → raw_articles.json         │
     └───────────────────────┬──────────────────────┘
                             │
                             ▼
     ┌──────────────────────────────────────────────┐
     │           2. De-duplication Logic            │
     │ - Title similarity using SequenceMatcher      │
     │ - Remove duplicates across sources            │
     │ - Result: unique articles                     │
     └───────────────────────┬──────────────────────┘
                             │
                             ▼
     ┌──────────────────────────────────────────────┐
     │            3. Hype Filter (Quality)          │
     │ - Remove low-information “marketing fluff”    │
     │ - min word count                              │
     │ - blacklist keywords                          │
     │ - capitalized tokens heuristic                │
     │ - Result: high-quality articles only          │
     └───────────────────────┬──────────────────────┘
                             │
                             ▼
     ┌──────────────────────────────────────────────┐
     │   4. LLM Extraction (Gemini Flash Latest)     │
     │ - Extract JSON fields:                        │
     │   • company_name                              │
     │   • category                                  │
     │   • sentiment_score                           │
     │   • is_funding_news                           │
     │ - Error-safe fallback                         │
     │ - Add source info for traceability            │
     └───────────────────────┬──────────────────────┘
                             │
                             ▼
     ┌──────────────────────────────────────────────┐
     │            5. Save Output to CSV             │
     │ - cleaned_output.csv                         │
     │ - Can be imported into Google Sheets         │
     │ - End of pipeline                            │
     └───────────────────────┬──────────────────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │        End Pipeline     │
                └────────────────────────┘

🎥 Demo Video

Add Loom or YouTube link here.

Deliverables Checklist

 Clean, structured code

 Hype filter

 LLM JSON extraction

 CSV export

 Workflow diagram

 Video demo

 README.md

 GitHub repository
