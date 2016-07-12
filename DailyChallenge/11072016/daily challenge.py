def main():
    element = "Spenglerium"
    sym = raw_input("Enter a symbol:")
    length = len(element)

    if len(sym) != 2:
        return False
    if sym[0] not in element:
        return False
    if sym[1] not in element:
        return False

    for i in range(0, length):
        if sym[0] == element[i]:
            for j in range(i + 1, length):
                if sym[1] == element[j]:
                    return True
    return False

print main()
