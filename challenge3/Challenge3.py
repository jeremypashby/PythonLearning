Word = raw_input("Input your word: ")


def StringLength():
	Length=0
	for Letter in Word:
		Length+=1

	print(Length)


if __name__ == "__main__":
	StringLength()