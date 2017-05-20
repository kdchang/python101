import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = 'http://www.twse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU.php'

def parseTSE(year, month, no):
	year = str(year)
	month = str(month)
	no = str(no)

	payload = {
		'query_year': year,
		'query_month': month,
		'CO_ID':no,
		'query-button': '查詢'
	}

	headers = {
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
	}

	res = requests.post(url, headers=headers, data=payload)
	data = res.text
	soup = BeautifulSoup(data, 'html.parser')

	content = soup.select('table')[0]

	with open('./' + year + month + '_tse_' + no + '.html', 'w') as f:
		f.write(str(content))

	table = pd.read_html('./' + year + month + '_tse_' + no + '.html', encoding='utf-8')[0]
	table = table.drop(table.index[0:2])
	#print(table)
	print(table.to_csv(header=False, index=False))

	with open('./' + year + '_tse_' + no + '.csv', 'a') as f:
		f.write(str(table.to_csv(header=False, index=False)))
	#print(content)

for m in range(1, 13): # [1, 2, 3... 12]
	time.sleep(5)
	parseTSE(2015, m, 2317)

	