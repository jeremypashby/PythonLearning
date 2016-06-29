Letter = raw_input('Enter a Letter:').lower()

vowel = ("aeiou")
consonant = ("bcdfghjklmnpqrstvwxyz")



def VowelCheck():

	if len(Letter) == 0 or len(Letter) > 1:
		print 'too many or too little letters'
	if Letter in vowel:
		print 'vowel'
	if Letter in consonant:  
		print 'consonant'

if __name__ == "__main__":
	VowelCheck()
