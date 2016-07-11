def make_3sg_form(word):
	suffix = ("o", "ch", "s", "sh", "x", "z")
	y = "y"
	ies = "ies"
	es = "es"
	s = "s"


	if word.endswith(suffix):
		return word+es
	if word.endswith(y):
		word = word.replace("y", "")
		return word+ies
	else:
		return word+s


def main():
	word = raw_input("enter word: ").lower()
	print make_3sg_form(word)


if __name__ == "__main__":
	main()

	