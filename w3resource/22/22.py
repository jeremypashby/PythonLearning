def num_num(nums):

	#nums = [4,3,4,1,5,4]

	counter = 0

	for i in nums:
		if i == 4:
			counter += 1
	return counter



def main():
	print num_num([4,4,4,1,5,4,4])




if __name__ == "__main__":
 	main()

