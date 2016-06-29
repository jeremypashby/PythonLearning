import random

def max():
	Number1 = (random.randint(1,100))
	Number2 = (random.randint(1,100))

	while True:
		if Number1 > Number2:
			print ("Number1 wins " + str(Number1))
			break
		elif Number2 > Number1:
			print ("Number2 wins " + str(Number2))
			break

if __name__ == "__main__":
	max()