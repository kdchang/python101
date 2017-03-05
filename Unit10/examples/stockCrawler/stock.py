import requests

url = 'https://tw.quote.finance.yahoo.net/quote/q?type=ta&perd=m&mkt=10&sym=5388&callback=jQuery111307171241853896984_1488710083323&_=1488710083325'
res = requests.get(url)

print(res.text)