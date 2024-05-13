import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Sachin_Tendulkar"

resp = requests.get(url)


soup = BeautifulSoup(resp.content, "html.parser")
images = soup.select("img")

for image in images:
    src = image.get("src")
    print(src)