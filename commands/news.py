import requests

NEWS_API_KEY = "your_api_key"

def get_top_headlines():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        return [(article['title'], article['url']) for article in articles[:5]]
    else:
        return []
