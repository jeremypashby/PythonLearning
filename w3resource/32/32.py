from fractions import gcd

def get_lcm(n1, n2):
	return (n1 * n2) // gcd(n1,n2)


def main():
	print get_lcm(24, 54)

if __name__ == "__main__":
    main()
