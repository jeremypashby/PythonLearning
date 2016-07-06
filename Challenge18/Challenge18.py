def is_panagram(Sentance):

    nospaceword = Sentance.replace(" ", "")
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alphanumber = 26
    check = 0

    if nospaceword < alphanumber:
        print "nope!"
    else:
        for i in alpha:
            if i in nospaceword:
                check = check+1
        if check == 26:
            print check
            print "true"
        else:
            print  check
            print "false"


def main():
    word = "The quick brown fox jumps over the lazy dog"
    is_panagram(word)


if __name__ == "__main__":
    main()
