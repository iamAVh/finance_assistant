import requests
from bs4 import BeautifulSoup

from dotenv import load_dotenv
import os
import yfinance as yf

# Load environment variables
load_dotenv()

def scrape_financial_news(query):
    try:
        url = f"https://finance.yahoo.com/search?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")

        articles = soup.find_all("h3", limit=3)
        if not articles:
            return "No recent news found."
        return "\n".join(f"- {article.get_text()}" for article in articles)
    except Exception as e:
        return f"Error scraping news: {str(e)}"
