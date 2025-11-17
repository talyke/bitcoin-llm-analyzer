import argparse
from fetch_bcoin import fetch_bitcoin_metrics, summarize_bitcoin_trends
from fetch_news import fetch_llm_news
from llm_summary import summarize_llm_news

def run_bitcoin_mode():
    metrics = fetch_bitcoin_metrics()
    summary = summarize_bitcoin_trends(metrics)
    print("\n🪙 Bitcoin Market Summary:\n")
    print(summary)

def run_both_mode():
    metrics = fetch_bitcoin_metrics()
    news_items = fetch_llm_news()
    summary = summarize_bitcoin_trends(metrics)
    news_summary = summarize_llm_news(news_items)

    print("\n🪙 Bitcoin Market Summary:\n")
    print(summary)
    print("\n🧠 LLM News Summary:\n")
    print(news_summary)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bitcoin Buzz: LLM-powered crypto summarizer")
    parser.add_argument("--mode", choices=["bitcoin", "both"], default="bitcoin", help="Choose summary mode")
    args = parser.parse_args()

    if args.mode == "bitcoin":
        run_bitcoin_mode()
    elif args.mode == "both":
        run_both_mode()