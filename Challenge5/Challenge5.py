


#print consonant
def translate():

	#while True:
	StartWord = ("tt")
	consonant = ("bcdfghjklmnpqrstvwxyz")
    	for char in StartWord:
        	if char in consonant:
        		FinishWord = StartWord.replace(char, char + 'o' + char)
    			print FinishWord
	
if __name__ == "__main__":
	translate()
