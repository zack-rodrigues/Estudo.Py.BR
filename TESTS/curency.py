import requests

url = 'https://v6.exchangerate-api.com/v6/12c1f9546740da028b8708e4/latest/USD'
response = requests.get(url)
data = response.json()

print(data["conversion_rates"]["BRL"])
