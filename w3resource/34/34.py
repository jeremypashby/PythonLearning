def number(num1, num2):
	number = num1 + num2

	if number >= 15 and number <= 20:
		number = 20
		return number
	else:
		return number


def main():
	print number(10,5)


if __name__ == "__main__":
    main()
