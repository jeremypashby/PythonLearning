def convert(value):
	import math

	number = float(value[:-2])
	firstarg = value[-2]
	secondarg = value[-1]


	if firstarg == "r":
		x = math.degrees(number)
		x = round(x)
		return "{0:g}d".format(x) 
	if firstarg == "d":
		y = math.radians(number)
		y = round(y,2)
		return "{0:g}r".format(y) 


def main():
	value = raw_input("enter in value: ")
	print convert(value)



if __name__ == "__main__":
	main()
