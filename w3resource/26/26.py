def histo(numbers):


	result = []
	for i in numbers:
		result.append(i * "*")
	return result

def printresult(results):
    for result in results:
        print result


def main():
	
	printresult(histo([10, 2, 3, 5]))





if __name__ == "__main__":
	main()
