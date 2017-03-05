from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import fs

url = 'https://tw.movies.yahoo.com/movie_intheaters.html?p=1'
o = urlparse(url)
print(o) 
print('scheme: {}'.format(o.scheme))

html = requests.get(url)
html.encoding = 'utf-8'

bp = BeautifulSoup(html.text, 'html.parser')
movies = bp.select('.item')
movie_titles = [title.find('h4').find('a').text for title in movies]
movie_links = [title.find('h4').find('a').get('href') for title in movies]

print(movie_titles)
print(movie_links)