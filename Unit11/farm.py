import hashlib
import requests
import os
import json

url = 'http://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx'
html = requests.get(url).text.encode('utf-8')
old_md5 = None
data = json.loads(html)
cur_md5 = hashlib.md5(html).hexdigest()

if os.path.exists('old_md5.txt'):
	with open('old_md5.txt') as f:
		old_md5 = f.read()
	with open('old_md5.txt', 'w') as f:
		f.write(cur_md5)
else:
	with open('old_md5.txt', 'w') as f:
		f.write(cur_md5)

if cur_md5 != old_md5:
	print('資料已更新！')

else:
	print('資料未更新，從檔案資料讀取...')

print('農產品交易行情資料')

for value in data:
	print('作物名稱：{}, 平均價：{}'.format(value['作物名稱'], value['平均價']))

		