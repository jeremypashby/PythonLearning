def addings(num1, num2, num3):
	number = num1 + num2 + num3

	if num1 == num2 or num1 == num3:
		number = 0
		return number
	else:
		return number


def main():
	print addings(2,2,3)

if __name__ == "__main__":
    main()
