import operator
x = [1,2,3,4,5,6]


def sum1():

	result = sum(x)
	print ("Addition =" + str(result))


def multiply1():

	result = reduce(operator.mul, x)
	print ("Multiply =" + str(result))
		


def main():
	sum1()
	multiply1()

if __name__ == "__main__":
	main()



