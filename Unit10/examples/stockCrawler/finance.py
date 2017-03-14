# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

payload = {
	'encodeURIComponent': 1,
	'step': 1,
	'firstin': 1,
	'off': 1,
	'queryName': 'co_id',
	't05st29_c_ifrs': 'N',
	't05st30_c_ifrs': 'N',
	'inpuType': 'co_id',
	'TYPEK': 'all',
	'isnew': 'false',
	'co_id': 2325,
	'year': 104

}

url = 'http://mops.twse.com.tw/mops/web/ajax_t163sb17'
res = requests.post(url, data=payload, headers=headers)

res.encoding = 'Big-5'

soup = BeautifulSoup(res.content, 'lxml')

co = soup.select('.hasBorder')

#print(BeautifulSoup(r.content, 'lxml').select('#currPrice'))
#tables = pd.read_html('http://www.cnyes.com/twstock/finratio2/5388.htm')[0]
#print(tables)

#for table in tables:
#print(tables.values[2])

with open('r.html', 'w') as f:
	f.write(str(co[0]))

tables = pd.read_html('./r.html', encoding='utf-8')[0]
print(tables[1][1])
