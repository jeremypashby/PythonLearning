import random

FirstDice = (random.randint(1,6))
SecondDice = (random.randint(1,6))
Guess = int(raw_input('what is your guess?'))


print FirstDice
print SecondDice

total = FirstDice + SecondDice
print total

#if (total % 2 ==0):
if total == Guess:
	print "Good Guess"
else:
	print "Wrong!"