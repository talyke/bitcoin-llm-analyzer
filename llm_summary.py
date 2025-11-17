import openai
from secrets import config

openai.api_key = config.DEEPSEEK_API_KEY
openai.base_url = "https://api.deepseek.com/v1"

def summarize_llm_news(news_items):
    prompt = "Summarize the following LLM-related news headlines:\n\n"
    for item in news_items:
        prompt += f"- {item['title']}: {item['description']}\n"

    response = openai.ChatCompletion.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def summarize_bitcoin_trends(metrics):
    prompt = f"""Summarize the sentiment and trends from this Bitcoin market data:

- Current Price: ${metrics['price']:,}
- 24h Change: {metrics['change']} ({metrics['changePercentage']}%)
- Volume: {metrics['volume']:,}
- Day Range: ${metrics['dayLow']:,} – ${metrics['dayHigh']:,}
- Year Range: ${metrics['yearLow']:,} – ${metrics['yearHigh']:,}
- Market Cap: ${metrics['marketCap']:,}

Respond with a short summary of market sentiment and notable trends.
"""
    response = openai.ChatCompletion.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()