import requests

api_key = "fc55eaae28354336b0790e65d5fc7765"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-09-17&sortBy=publishedAt&apiKey=fc55eaae28354336b0790e65d5fc7765"

headers = {"User-Agent": "Mozilla/5.0"}
request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])