def generate_n_chars(num, letter):
        x = (xrange(num))
        n = ''.join([letter for s in x])
        return n 


def main():
     print generate_n_chars(5, 'x')


if __name__ == "__main__":
    main()
