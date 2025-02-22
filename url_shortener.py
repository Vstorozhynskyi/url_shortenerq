# URL Shortener (bit.ly API required)
import requests
TOKEN = "YOUR_BITLY_TOKEN"
url = input("Enter URL: ")
res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"long_url": url}, headers={"Authorization": f"Bearer {TOKEN}"}).json()
print("Shortened URL:", res.get("link", "Error"))
