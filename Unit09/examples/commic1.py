import requests
from bs4 import BeautifulSoup

url = 'http://9gag.com/'
res = requests.get(url)

print(res.text)


