import requests

r = requests.get('https://www.pathofexile.com/api/trade/data/leagues')

league = r.json()

p = requests.post("https://www.pathofexile.com/api/trade/search/YOUR_LEAGUE")
print(r.text);