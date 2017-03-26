import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
import ast

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
)

url = 'http://ecapi.pchome.com.tw/ecshop/prodapi/v2/store/DSAA0K/prod&offset=1&limit=36&fields=Id,Nick,Pic,Price,Discount,isSpec,Name,isCarrier,isSnapUp,isBigCart&_callback=jsonp_prodlist?_callback=jsonp_prodlists'

headers = {
	'user-agenr': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

browser = webdriver.PhantomJS(desired_capabilities=dcap)
browser.maximize_window()
browser.get(url)

content = browser.page_source

result = re.findall(r'jsonp_prodlist\(\[(.+)\]\)\;\}catch\(e\)', content)[0]
items = ast.literal_eval(result)

for item in items:
	print(item['Name'], item['Price']['P'])
