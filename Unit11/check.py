import hashlib
import requests
import os
import json

url = 'http://opendata.epa.gov.tw/ws/Data/RainTenMin/?format=json'
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

for value in data:
	print('地名：{}, 24hr 雨量：{}'.format(value['SiteName'], value['Rainfall24hr']))