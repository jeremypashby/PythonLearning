def translate(transword):

    consonant = "bcdfghjklmnpqrstvwxyz"
    finishword = ""
    for char in transword:
        if char in consonant:
            finishword += char + 'o' + char
        else:
            finishword += char
    return finishword


def main():
    TRANSWORD = "this is fun"
    TRANSWORD2 = "this is not fun"
    print translate(transword=TRANSWORD)
    print translate(transword=TRANSWORD2)


if __name__ == "__main__":
    main()
