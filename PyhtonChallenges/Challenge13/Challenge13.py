def max_in_list(inputList):
 
    sortedList = sorted(inputList)
 
    return sortedList[-1]


def main():
	List = [21,54,3456,6,12,2342,2345,10037,21,666,999]
	max_in_list(List)
	print("The list is: "+str(List)) 
	print("The max in the list is: " +str(max_in_list(List)))


if __name__ == "__main__":
	main()
