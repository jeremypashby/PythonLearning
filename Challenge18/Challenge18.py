word = "The quick brown fox jumps over the lazy dog"
nospaceword = word.replace(" ", "")
alpha = "abcdefghijklmnopqrstuvwxyz"
alphanumber = 26
check = 0
#print nospaceword
if nospaceword < alphanumber:
    print "nope!"
else:
    #print "maybe!"
    for i in alpha:
        if i in nospaceword:
            check = check+1
            #print check
    if check == 26:
        print check
        print "true"
    else:
        print  check
        print "false"