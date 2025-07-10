import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def get_live_metrics(ticker):
    try:
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": ticker,
            "apikey": API_KEY
        }
        response = requests.get(url, params=params)
        data = response.json()

        if "Global Quote" in data:
            quote = data["Global Quote"]
            price = quote.get("05. price", "N/A")
            pe = quote.get("08. PERatio", "N/A")
            return f"{ticker} is trading at ${price}. P/E ratio is {pe}."
        elif "Note" in data:
            return "Rate limit exceeded. Please wait."
        else:
            return "Unexpected API response."
    except Exception as e:
        return f"Error: {str(e)}"
