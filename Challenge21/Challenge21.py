def char_freq(string):
	freq = {}
	for c in string:
		freq[c] = freq.get(c, 0) + 1
	return freq
	

def main():
	charaters = raw_input("Enter in your characters: ")
	print(char_freq(charaters))


if __name__ == "__main__":
    main()
