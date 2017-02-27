from urllib.parse import urlparse

url = 'https://tw.movies.yahoo.com/movie_intheaters.html?p=2'
o = urlparse(url)
print(o)

print('scheme={}'.format(o.scheme))
print('netloc={}'.format(o.netloc))
print('port={}'.format(o.port))
print('path={}'.format(o.path))
print('query={}'.format(o.query))