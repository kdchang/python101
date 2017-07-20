import json
import csv
import requests

# 台灣證交所個股本益比、殖利率及股價淨值比 http://www.twse.com.tw/zh/page/trading/exchange/BWIBBU.html

# define http header
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

data_list = []

def get_stock_data(date, stock_no):
    '''
    crawler data from http://www.twse.com.tw/zh/page/trading/exchange/BWIBBU.html
    '''
    url = 'http://www.twse.com.tw/exchangeReport/BWIBBU?response=json&date={}&stockNo={}&_=1500590822750'.format(date, stock_no)

    res = requests.get(url, headers=headers)

    raw_data = json.loads(res.text)

    fields = raw_data['fields']
    data = raw_data['data']

    for value in data:
        data_list.append({
            fields[0]: value[0],
            fields[1]: value[1],
            fields[2]: value[2],
            fields[3]: value[3],
            fields[4]: value[4],
            fields[5]: value[5]
        })

get_stock_data('20170721', '2330')
print(data_list)

keys = data_list[0].keys()
with open('stock.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data_list)
