# Check if the substring is a rotation substring of the given substring

def isRotationSubstring(str1, str2):
	str3 = str1+str1
	if str2 in str3:
		print "Yes, its a substring"
	else:
		print "no, its not a substring"

isRotationSubstring("waterbottle","bottlwater")