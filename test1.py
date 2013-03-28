import os, time, re

FILE = 'X:\\1652\\test.txt'

db = {'Luba':'Petrova','Lena':'Sidorova','Gena':'Gena'}

def file_exist(file):
	if os.path.exists(file):
		#print('file exists')
		with open(file, 'r+') as f:
			name = f.read()
			match = re.search(r"'(.*)'", name)
			try:
				surname = match.group()
				surname = surname.replace('\'', '')
				with open(file, 'w') as f:
					f.write('$STUDENT.NAME=\''+ surname +'\';$STUDENT.FAM=:\''+ db[surname] +'\';\n')
				print('Name found')
			except KeyError:
				print('Name not found')
			except AttributeError:
				print('File is empty or incorrect')

	else:
		print('not found')
		time.sleep(1)
		file_exist(file)

file_exist(FILE)