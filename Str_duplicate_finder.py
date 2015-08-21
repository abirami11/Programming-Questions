def duplicates_finder(str):
	i = 0
	for e in str:
		chkstr = str[:i] + str[i+1:]
		if chkstr.find(e) != -1:
			print "duplicate is present"
			return 
		i += 1
	print "No duplicates"

def duplicates_finder_efficient(str):
	i = [0] * 256
	for e in str:
		val = ord(e)
		if i[val] == 1:
			return "duplicates present"
		i[val] = 1

#duplicates_finder("moneyss")
print duplicates_finder_efficient("moneys")