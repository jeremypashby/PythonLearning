def workings(num1, num2):

	if num1 == num2:
		return True
	if abs(num1 - num2) == 5:
		return True
	if num1 + num1 == 5:
		return True
	else:
		return False
def main():
	print workings(10, 12)


if __name__ == "__main__":
    main()
