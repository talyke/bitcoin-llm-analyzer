import requests
import openai

from secrets import config
openai.api_key = config.OPENAI_API_KEY
openai.base_url = "https://api.deepseek.com/v1"


def fetch_bitcoin_news():
    url = f"https://newsapi.org/v2/everything?q=bitcoin&sortBy=publishedAt&apiKey={config.NEWS_API_KEY}"
    response = requests.get(url)
    articles = response.json().get("articles", [])[:5]
    return [article["title"] for article in articles]

def fetch_bitcoin_metrics():
    url = f"https://financialmodelingprep.com/stable/quote?symbol=BTCUSD&apikey={config.FMP_API_KEY}"
    response = requests.get(url)
    data = response.json()[0]
    return {
        "price": data["price"],
        "change": data["change"],
        "changePercentage": data["changePercentage"],
        "volume": data["volume"],
        "dayHigh": data["dayHigh"],
        "dayLow": data["dayLow"],
        "yearHigh": data["yearHigh"],
        "yearLow": data["yearLow"],
        "marketCap": data["marketCap"]
    }

def summarize_bitcoin_trends(headlines, metrics):
    prompt = f"""Summarize the sentiment and key themes from these Bitcoin news headlines and market data:

News Headlines:
{chr(10).join(f"- {h}" for h in headlines)}

Market Data:
- Current Price: ${metrics['price']:,}
- 24h Change: {metrics['change']} ({metrics['changePercentage']}%)
- Volume: {metrics['volume']:,}
- Day Range: ${metrics['dayLow']:,} – ${metrics['dayHigh']:,}
- Year Range: ${metrics['yearLow']:,} – ${metrics['yearHigh']:,}
- Market Cap: ${metrics['marketCap']:,}

Respond with a short summary of the market sentiment and any notable trends.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    headlines = fetch_bitcoin_news()
    metrics = fetch_bitcoin_metrics()
    summary = summarize_bitcoin_trends(headlines, metrics)

    print("\n Bitcoin Buzz Summary:\n")
    print(summary)
