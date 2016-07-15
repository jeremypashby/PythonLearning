def is_check():
	sen = "Is it good today?"

	if sen.startswith("Is"):
		return sen
	else: 
		return "Is {0}".format(sen)


print is_check()
