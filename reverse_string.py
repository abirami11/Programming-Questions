def reverse_string(str):
	end = len(str) - 1
	start = 0
	strlist = list(str)
	while end > start:
		strlist[start],strlist[end] = strlist[end], strlist[start]
		start += 1
		end -= 1
	print ''.join(strlist)

reverse_string("Hello")