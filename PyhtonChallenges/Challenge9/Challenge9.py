def is_member(list, value):
	try:
		list.index(value)
	except ValueError:
		print False
	else:
		print True


def main():
	listings = ['Jeremy', 'Mark', 'Kate']
	word = 'Kate'
	is_member(listings, word)


if __name__ == "__main__":
	main()