import os, time

FILE = 'X:\\1652\\A1-2.txt'


def file_exist(file):
	if os.path.exists(file):
		print('file exists')

		with open(file, 'r') as f:
			text = f.read()
		print(text + ' Petrova')
	else:
		print('not found')
		time.sleep(1)
		file_exist(file)

file_exist(FILE)