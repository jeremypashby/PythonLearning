def correct():
	testing = "This   is  very funny  and    cool.Indeed!"
	final = testing.replace('.', '. ')
	fix = ' '.join(final.split())
	return fix


def main():
	print correct()


if __name__ == "__main__":
	main()