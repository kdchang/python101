import requests
from bs4 import BeautifulSoup

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Reffer': 'https://www.cmoney.tw/finance/f00040.aspx?s=1101'
}


cookies = {
	'AspSession': 'uifdfx0hnnxd1aebbwupkgpb'
}

payload = {
	'action': 'GetBalanceSheet',
	'stockId': '1101',
	'season': 4,
	'cmkey': 'vsJ6f5A7DPXPSg/T1bjQxw=='
}

res = requests.get('https://www.cmoney.tw/finance/ashx/mainpage.ashx', params=payload, cookies=cookies, headers=headers)

