y = ['Jeremy', 'James', 'Kate']
z = ['Germain', 'Jeremy', 'Kat', "Jay"]

def overlapping():
	for name1 in y:
		for name2 in z:
			if name1 in name2:
				return True
	return False	

def main():
	print overlapping()


if __name__ == "__main__":
    main()
