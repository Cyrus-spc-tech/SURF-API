import requests

api = "019684471d894dd898639151ae78c8b6"
base_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api}"

def news():
    response = requests.get(base_url)
    data = response.json()
    articles = data.get('articles', [])

    for article in articles:
        title = article.get('title', 'No title available')
        source = article.get('source', {}).get('name', 'Unknown source')
        description = article.get('description', 'No description available')
        url = article.get('url', '#')

        print(f"\nArticle {i}:")
        print(f"Source: {source}")
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"URL: {url}")    
