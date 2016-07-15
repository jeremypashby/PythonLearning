def number_check(n):

	if n % 2 == 0:
		print "yeap, {0} is an even number".format(n)
	else:
		print "nope, {0} not an even number".format(n)



def main():
 	number = input("Enter your number")
 	number_check(number)



if __name__ == "__main__":
 	main()