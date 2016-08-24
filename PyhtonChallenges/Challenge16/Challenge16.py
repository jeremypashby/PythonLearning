def filter_long_words():

	words = ['Hello','Goodbye','Afternoon']
	min_word_length = 6
	for word in words:
		word_length = (int(len(word)))
		if word_length > 6:
			print word




def main():
	filter_long_words()

if __name__ == "__main__":
	main()
