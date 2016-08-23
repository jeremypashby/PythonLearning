def add_if_int(num1, num2):

	if type(num1) == int and type(num2) == int:
		return (num1 + num2)
	else:
		return "nope not numbers"




def main():
	print add_if_int(10, 10)


if __name__ == "__main__":
    main()
