import requests 
from bs4 import BeautifulSoup
import pandas as pd

# 

headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
res = requests.get('http://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=IS_M_QUAR_ACC&STOCK_ID=1101', headers=headers)
res.encoding = 'Big-5'
print(res.text)


table = pd.DataFrame(pd.read_html(res.text, attrs={"class": "solid_1_padding_3_4_tbl"})[0])
table = table.drop(table.index[[1, 3, 5, 7]])

print(table)

