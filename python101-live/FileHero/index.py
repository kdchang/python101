import os 

filename = 'hello_workd.txt'

with open(filename, 'r') as f:
	result = f.readlines()
	print(result)
