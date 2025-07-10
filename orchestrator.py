from agents.retriever_agent import retrieve_relevant_docs
from agents.api_agent import get_live_metrics
from agents.scraping_agent import scrape_financial_news
from agents.language_agent import synthesize_response

def orchestrate(query):
    docs = retrieve_relevant_docs(query)

    live_data = ""
    if any(keyword in query.lower() for keyword in ["price", "p/e", "stock", "share"]):
        live_data = get_live_metrics("AAPL")  # You can extract ticker from query with NLP if needed

    news_data = ""
    if "news" in query.lower() or "filing" in query.lower():
        news_data = scrape_financial_news(query)

    final_docs = docs + [live_data, news_data]
    return synthesize_response(query, final_docs)
