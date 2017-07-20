import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def post_stock_data(year, month, code):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    payload = {
        'query_year': year,
        'query_month': month,
        'CO_ID': code,
        'query-button': '查詢' 
    }

    res = requests.post('http://www.twse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU.php', headers=headers, data=payload)

    data = res.text

    soup = BeautifulSoup(data, 'lxml')

    content = soup.select('table')[0]

    with open('./data.html', 'w') as f:
        f.write(str(content))

    #print('table', pd.read_html('./data.html'))
    table = pd.read_html('./data.html')[0]

    print(table)
    with open('./' + code + '_' + year + '_' + month + '.csv', 'w') as f:
        f.write(str(table.to_csv(header=False)))

for month in range(1, 13):
    post_stock_data('2016', str(month), '2317')
    time.sleep(3)
    