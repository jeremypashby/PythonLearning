def details():

	name = 'Jeremy Pashby'
	age = '23'
	address = '123 home, england, UK'

	return("name: {0} \nage: {1} \naddress: {2}").format(name,age,address)






def main():
	print details()	


if __name__ == "__main__":
    main()
