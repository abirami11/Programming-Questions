def chk_permutation(str1,str2):
	if len(str1) != len(str2):
		print "Not a permuation"
		return
	i = [0] * 256
	for e in str1:
		i[ord(e)] += 1
	for e in str2:
		i[ord(e)] -= 1
		if i[ord(e)] < 0:
			print "Not a permuatation"
			return
	print "Its a permuation"
chk_permutation("moon","oonm")