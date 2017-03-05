import requests
from bs4 import BeautifulSoup

payload = {
	'from': '/bbs/Gossiping/index.html',
	'yes': 'yes'
}

res = requests.post('https://www.ptt.cc/ask/over18', data=payload)

soup = BeautifulSoup(res.text, 'html.parser')
items = soup.select('.r-ent')

for item in items:
	print('日期：{}, 作者：{}, 文章標題：{}'.format(item.select('.date')[0].text, item.select('.author')[0].text, item.select('.title')[0].select('a')[0].text))
	#print(item.select('.date')[0].text, item.select('.author')[0].text, item.select('.title')[0].select('a')[0].text)