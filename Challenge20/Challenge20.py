def translate(transword):
	WORDS = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
	finalwords = transword.split(" ")
	result = []
	for x in finalwords:
		if x not in WORDS:
			print '- sorry, "{0}" cannot be translated'.format(x)
			break
		else:
			result.append(WORDS[x])
	return result #(WORDS[x]),

def printresult(results):
    for result in results:
        print result,


def main():
	wordinput = raw_input('Input your word: ')
	printresult(translate(wordinput))


if __name__ == "__main__":
    main()

