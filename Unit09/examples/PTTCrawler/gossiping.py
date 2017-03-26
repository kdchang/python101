import requests
from bs4 import BeautifulSoup
import time
import json

payload = {
	'from': '/bbs/Gossiping/index.html',
	'yes': 'yes'
}

headers = {
	'user-agenr': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

url = 'https://www.ptt.cc/ask/over18'

rs = requests.Session()
res = rs.post(url, data=payload, headers=headers)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', data=payload, headers=headers)

next_page_url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
nurl = ''
post_list = []

def parseContent(res):
	global next_page_url, nurl, post_list
	soup = BeautifulSoup(res.text, 'html.parser')
	items = soup.select('.r-ent')
	for item in items:
		#pass
		print('日期：{}, 作者：{} {}'.format(item.select('.date')[0].text, item.select('.author')[0].text, item.select('.title')[0].text))
		# post_list.append({'日期': item.select('.date')[0].text }, {'作者': item.select('.author')[0].text}, {'文章': item.select('.title')[0].text})
		#print(item.select('.date')[0].text, item.select('.author')[0].text, item.select('.title')[0].select('a')[0].text)
	nurl = soup.select('.btn-group-paging')[0].select('a')[1].get('href')
	next_page_url = 'https://www.ptt.cc' + nurl

print('page: 1')
parseContent(res)	

#while(len(nurl) != 0):
for page in range(1): # [0, 1, 2, 3]
	print('page: ' + str(page + 2))
	time.sleep(5)
	resp = rs.get(next_page_url, headers=headers)
	parseContent(resp)

# with open('./ptt.dat', 'w', encoding='utf8') as f:
# 	f.write(json.dumps(post_list, ensure_ascii=False))