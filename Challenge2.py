import random

def max_of_three():
	Number1 = (random.randint(1,100))
	Number2 = (random.randint(1,100))
	Number3 = (random.randint(1,100))

	print(Number1)
	print(Number2)
	print str(Number3)

	print "Number1 =" + str(Number1) + ", Number2 =" + str(Number2) + ", Number3 =" + str(Number3)

	while True:
		if Number1 > Number2 and Number1 > Number3:
			print ("Number1 wins " + str(Number1))
			break
		elif Number2 > Number1 and Number2 > Number3:
			print ("Number2 wins " + str(Number2))
			break
		elif Number3 > Number1 and Number3 > Number2:
			print ("Number3 wins " + str(Number3))
			break

	 			

if __name__ == "__main__":
	max_of_three()