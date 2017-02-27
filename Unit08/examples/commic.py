import requests, os
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://v.comicbus.com/online/comic-103.html?ch=1'
html = requests.get(url)

html.encoding = 'utf-8'

sp = BeautifulSoup(html.text, 'html.parser')

images_dir = 'images/'
if not os.path.exists(images_dir):
	os.mkdir(images_dir)

all_links = sp.find_all(['a', 'img'])
for link in all_links:
	src = link.get('src')
	href = link.get('href')
	attrs = [src, src] 

print(attrs)