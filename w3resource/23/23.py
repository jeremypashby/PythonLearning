def number_sen(sen):

	x = sen[0].lower()
	y = sen[1].lower()

	counterx = 0
	countery = 0
	counter = 0

	for i in sen[2:]:
		if i == x or i == y:
			counter += 1

	if counter < 2:
		return sen
	else:
		return counter







def main():
 	print number_sen("is a god")




if __name__ == "__main__":
	main()

