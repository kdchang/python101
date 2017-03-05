import requests

url = 'http://taqm.epa.gov.tw/pm25/tw/PM25A.aspx?area=4'
html = requests.get(url)
html.encoding = 'utf-8'
print(html.text.splitlines())
