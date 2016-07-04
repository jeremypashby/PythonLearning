def find_longest_word():
	words = ['Hello','Goodbye','Afternoon']
	for word in words:
		word_length = str(len(word))
		sortedList = sorted(word_length)
		return str(sortedList) + word


def main():
	print find_longest_word()

if __name__ == "__main__":
	main()
