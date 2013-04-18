def __tripple_to_dict(string):
	dic = {}
	pref = []
	index = []
	value = []

	string = string.replace('$', '')
	arr = string.split(';')
	arr = list(map(lambda x: x.split('='), arr))
	for n in arr:
		n[0] = n[0].split('.')
	del(arr[-1])
	for x in range(len(arr)):
		n = arr[x]
		pref.append(n[0][0])
		index.append(n[0][1])
		value.append(n[1])
	# tup = list(zip(index, value))
	dic = dict(zip(list(zip(pref,index)), value))
	# dic = sorted(dic.items())
	return dic


def __dict_to_tripple(dict):
	string = ''
	for x in dict:
		string += '$' + x[0] + '.' + x[1] + '=' + dict[x] + ';'
	return string


def add_to_tripple(item, string):
	dic = __tripple_to_dict(string)
	new_item = __tripple_to_dict(item)
	res = dict(list(dic.items()) + list(new_item.items()))
	# res = sorted(res.items())
	# result = dict_to_tripple(dic)
	return __dict_to_tripple(res)


# print(dict_to_tripple(tripple_to_dict('$D.L=14.0;$E.D=20.5;')))
print(add_to_tripple('Z.Q=12.5;A.M=12.5;Q.T=12.5;', '$D.L=14.0;$E.D=20.5;$D.L=14.4;'))
# print(tripple_to_dict('$D.L=14.0;$E.D=20.5;'))