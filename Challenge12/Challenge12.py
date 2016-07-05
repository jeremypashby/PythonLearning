def histogram(numbers):
    result = []
    for number in numbers:
        result.append(number * '*')
    return result


def printresult(results):
    for result in results:
        print result


def main():
    NUMS = [4, 9, 7, 10]
    printresult(histogram(NUMS))


if __name__ == "__main__":
    main()
