def replace_str_spaces(str):
	length = len(str)
	strlist = list(str)
	count = 0
	for e in str:
		if e == ' ':
			count += 1
	newlen = len(str) + count * 3
	i = 0
	for e in strlist:
		if e == ' ':
			strlist[i] = '%20'
		i += 1
	return ''.join(strlist)

print replace_str_spaces("Hello World")