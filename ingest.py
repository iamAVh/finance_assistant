import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Alpha Vantage API key
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def get_stock_summary(ticker_symbol):
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': ticker_symbol,
        'apikey': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    if 'Time Series (Daily)' in data:
        latest_data = list(data['Time Series (Daily)'].values())[0]
        close_price = latest_data['4. close']
        pe_ratio = data.get('P/E ratio', 'N/A')  # Adjust based on available data
        return f"{ticker_symbol} stock closed at {close_price}. P/E ratio is {pe_ratio}."
    else:
        return f"Could not retrieve data for {ticker_symbol}."

def run_ingestion():
    print("Ingesting data...")
    summaries = [get_stock_summary("AAPL")]  # Example: Get summary for AAPL
    print(summaries)

if __name__ == "__main__":
    run_ingestion()
