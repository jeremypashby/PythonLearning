def main():
	element = "Spenglerium"
	sym = raw_input("enter in symbol: ")
	finalsym = []
	for i in sym:
		if len(sym) != 2:
			print "invalid!"
			break
		# if i in element:
		#  	finalsym += i
		#  	#return True
		#  	print finalsym
		if i not in element:
			#return False
		 	print "nope! not in here"
			return False
		else:
		 	finalsym += i
		 	#print finalsym
		 	return True
		

print main()