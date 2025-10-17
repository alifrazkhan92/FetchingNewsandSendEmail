import requests
import send_email

# Replace 'your_api_key' with your actual NewsAPI key
api_key = "fc55eaae28354336b0790e65d5fc7765"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-09-17&sortBy=publishedAt&apiKey=fc55eaae28354336b0790e65d5fc7765"

#
headers = {"User-Agent": "Mozilla/5.0"}
request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    if article['title'] is None or article["description"] is None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"


body = body.encode("utf-8")
send_email(body)