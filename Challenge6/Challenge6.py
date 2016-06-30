import operator
x = [1,2,3,4,5,6]


def sum1():

	result = sum(x)
	print ("Addition =" + str(result))

if __name__ == "__main__":
	sum1()

def multiply1():

	result = reduce(operator.mul, x)
	print ("Multiply =" + str(result))
		

if __name__ == "__main__":
	multiply1()


