import requests 
from urllib.request import urlopen

image_name = 'http://i.imgur.com/S3YRNNl.jpg'

image = urlopen(image_name)

with open('./' + 'S3YRNNl.jpg', 'wb') as f:
	f.write(image.read())
