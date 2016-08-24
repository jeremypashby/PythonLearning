def is_palindrome():
    word = raw_input("Input your word: ").lower()
    y = word.replace(" ", "")
    x = y[::-1]
    print y
    print x
    if y == x:
        print "It is a palindrome"
    else:
        print "It is not a palindrome"


def main():
    is_palindrome()


if __name__ == "__main__":
    main()
