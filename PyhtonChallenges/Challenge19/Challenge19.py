def bottles_of_beer():
	bottles = range(100, -1, -1)
	for bottle in bottles:
		nextbottle = bottle - 1
		if nextbottle > -1:
			print "{0} bottles of beer on the wall, {0} bottles of beer. Take one down, pass it around, {1} bottles of beer on the wall".format(bottle, nextbottle)



def main():
	bottles_of_beer()


if __name__ == "__main__":
	main()