import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import json


def parseTSE(year, month, no):
	print(year, month, no)
	url = 'http://www.twse.com.tw/exchangeReport/BWIBBU?response=json&date=20170501&stockNo=2880&_=1496411050617'

	headers = {
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
	}

	res = requests.post(url, headers=headers)
	data = res.text

	print(json.loads(data)['data'])

for m in range(1, 13): # [1, 2, 3... 12]
	time.sleep(5)
	parseTSE(2015, m, 2880)

	