import os
filename = 'hello.txt'

if os.path.exists(filename):
	os.remove(filename)
else:
	with open(filename, 'w') as f:
		f.write('hello world!!')