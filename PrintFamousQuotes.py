import random
import time

Quotes = ["Creationists make it sound like a 'theory' is something you dreamt up after being drunk all night: Isaac Asimov" , \
 "I don't believe in God. My god is patriotism. Teach a man to be a good citizen and you have solved the problem of life.: Andrew Carnegie", \
 "All thinking men are atheists.: Ernest Hemingway", \
 "Lighthouses are more helpful then churches.: Benjamin Franklin", \
 "Faith means not wanting to know what is true.: Friedrich Nietzsche", \
"The fact that a believer is happier than a skeptic is no more to the point than the fact that a drunken man is happier than a sober one.: George Bernard Shaw", \
"Say what you will about the sweet miracle of unquestioning faith, I consider a capacity for it terrifying and absolutely vile.: Kurt Vonnegut", \
"I believe in God, only I spell it Nature.: Frank Lloyd Wright", \
"Man will never be free until the last king is strangled with the entrails of the last priest.: Denis Diderot", \
"A man is accepted into a church for what he believes and he is turned out for what he knows.: Samuel Clemens"
]

def main():
	while True:
		TimeWait = (random.randint(5,10))
		print (random.choice(Quotes))
		time.sleep(TimeWait)
		continue

main()