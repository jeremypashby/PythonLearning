number = 5
n1 = "%s" % number
n2 = ("%s%s" % (number, number))
n3 = ("%s%s%s" % (number, number, number))


result = int(n1) + int(n2) + int(n3)
print result