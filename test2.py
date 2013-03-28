import os, time

FILE = 'X:\\1652\\test.txt'


def file_exist(file):
	if os.path.exists(file):
		print('file exists')

		with open(file, 'w') as f:
			name = input('Enter name: ')
			f.write('$STUDENT.NAME=\''+ name + '\';$STUDENT.FAM=:;')
			
	else:
		print('not found')
		time.sleep(1)
		file_exist(file)

file_exist(FILE)