#coding:utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = 'http://www.tse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU.php'

def parseTSE(year, month, no):
	year = str(year)
	month = str(month)
	no = str(no)

	payload = {
		'myear': year,
		'mmon': month,
		'STK_NO': no,
		'login_btn': '%ACd%B8%DF'
	}

	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	}

	res = requests.post(url, headers=headers, data=payload)

	data = res.text.encode('latin1', 'ignore').decode('big5')
	soup = BeautifulSoup(data, 'html.parser')

	content = soup.select('.board_trad')[0]

	with open(year + month + '_tse_' + no + '.html', 'w') as f:
		f.write(str(content))

	table = pd.read_html('./' + year + month + '_tse_' + no + '.html', encoding='utf-8')[0]
	table = table.drop(table.columns[0:2])
	print(table.to_csv(header=False, index=False))

	with open('./' + year + '_tse_' + no + '.csv', 'a') as f: # a 是寫在檔案最後面，不會覆寫
		f.write(str(table.to_csv(header=False, index=False)))

for m in range(1, 13):
	time.sleep(5)
	parseTSE(2015, m, 2301)

