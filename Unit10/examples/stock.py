import requests
from bs4 import BeautifulSoup
import pandas as pd

print(tables)

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded'
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
	'year': 103

}

url = 'http://mops.twse.com.tw/mops/web/ajax_t163sb18'
res = requests.post(url, data=payload, headers=headers)

res.encoding = 'Big-5'

soup = BeautifulSoup(res.content, 'lxml')

for entry in soup.select('.odd'):
	print(entry.text)