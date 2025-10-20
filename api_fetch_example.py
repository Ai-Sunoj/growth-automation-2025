import requests

# Simple script to fetch Bitcoin price from Coindesk API
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

if response.status_code == 200:
    data = response.json()
    print("💰 Bitcoin Price (USD):", data["bpi"]["USD"]["rate"])
else:
    print("Error fetching data:", response.status_code)
