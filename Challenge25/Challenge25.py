def make_ing_form(word):


	suffix = ("o", "ch", "s", "sh", "x", "z")
	y = "y"
	ies = "ies"
	es = "es"
	s = "s"
	e = "e"
	ing = "ing"
	ie = "ie"
	ying = "ying"
	ee = "ee"

	if word.endswith(ie):
		word = word.replace("ie", "")
		return word+ying
	elif word.endswith(ee):
		return word+ing
	elif word.endswith(e):
		word = word.replace("e", "")
		return word+ing
	else:
		word = word + word[-1]
		return word+ing


def main():
	word = raw_input("enter word: ").lower()
	print make_ing_form(word)



if __name__ == "__main__":
	main()

		