def is_palindrome():
	word = raw_input("Input your word: ").lower()
	x = word[::-1]

	if word == x:
		print "It is a palindrome"
	else:
		print "It is not a palindrome"

if __name__ == "__main__":
	is_palindrome()
