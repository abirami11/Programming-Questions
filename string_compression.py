def string_compression(str1):
	strlist = []
	first = str1[0]
	count = 1 
	for e in str1[1:]:
		if e == first:
			count += 1
		else:
			strlist.append(first + str(count))
			count = 1
			first = e
	strlist.append(first + str(count))
	return ''.join(strlist)
print string_compression("aaaabbbcccd")