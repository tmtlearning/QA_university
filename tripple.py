def to_triple(string):
	dic = {}
	temp = []

	string = string.replace('$', '')
	arr = string.split(';')
	arr = list(map(lambda x: x.split('='), arr))
	for n in arr:
		n[0] = n[0].split('.') 
	for x in range(len(arr)):
		print(x)
	print(arr)
	
	


to_triple('$D.L=14.0;$E.D=20.5;')