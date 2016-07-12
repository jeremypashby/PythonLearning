#def main():
element = "Spenglerium"
sym = raw_input("enter in symbol: ")
finalsym = []
for i in sym:
	if len(sym) != 2:
		print "invalid!"
		break
	elif i in element:
	  	finalsym += i
	  	#print finalsym
if len(finalsym) != 2:
	print "nope"
if len(finalsym) == 2:
	for j in finalsym:
		if j in element:
			print element.index(j)

			#print j
			#print "yes"

# print finalsym
# for x in finalsym:
# 	if x in element:
# 		print "yes"
# 		return True
# 	if len(finalsym) != 2:
# 		print "no"
# 		return False
# 	else:
# 		return False






		#  	#return True
		#  	print finalsym
		# if i not in element:
		# 	#return False
		#  	print "nope! not in here"
		# 	return False
		# else:
		#  	finalsym += i
		#  	#print finalsym
		#  	return True
		

#print main()