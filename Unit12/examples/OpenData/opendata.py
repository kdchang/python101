import requests
import json
import matplotlib.pyplot as plt

url = 'http://data.fda.gov.tw/cacheData/35_3.json;jsessionid=5C6805F7603C7BCB4695D63225A341F4'

res = requests.get(url)

items = json.loads(res.text)
data = [0, 0]

for item in items:
	if item[6]['負責人性別'] == '男':
		data[0] += 1
	else:
		data[1] += 1 

labels = ['man', 'woman']

plt.pie(data, labels=labels)
plt.show()