


#print consonant
def translate():

	#while True:
	StartWord = ("tt")
	consonant = ("bcdfghjklmnpqrstvwxyz")
    	for char in StartWord:
        	if char in consonant:
        		#print char
        		StartWord = StartWord.replace(char, char + 'o' + char)
    	print StartWord
	
if __name__ == "__main__":
	translate()
