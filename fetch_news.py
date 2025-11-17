import requests

from secrets import config
api_key = config.NEWS_API_KEY
base_url = "https://newsdata.io/api/1/latest"

def fetch_llm_news():
    url = base_url
    params = {
        "apikey": api_key,
        "q": "llm"
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] != "success":
        raise Exception("Failed to fetch news")

    articles = data.get("results", [])[:5]  # limit to 5 headlines
    parsed = [
        {
            "title": article["title"],
            "description": article["description"],
            "link": article["link"]
        }
        for article in articles
    ]
    return parsed
