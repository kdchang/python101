import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

res = requests.get('https://www.ptt.cc/man/Beauty/DF7B/D111/M.1400913738.A.BD8.html', headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

images = soup.select('a[href^=http://i.imgur]')

for image in images:
	print(image['href'])
	filename = image['href'].split('/')[3]
	img = urlopen(image['href'])
	with open('./images/' + str(filename), 'wb') as f:
		f.write(img.read())