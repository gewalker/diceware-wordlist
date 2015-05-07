#!/usr/bin/python
import random

separator = " "
passphrase = ""

for i in range(10):
#	Generate a number between 11111 and 66666
	randomnumber = str().join(random.SystemRandom().choice('123456') for _ in range(5))

#	Lookup number in the diceware wordlist
	for line in open("diceware.wordlist.asc"):
		if randomnumber in line:
			passphrase = passphrase + separator + line[6:-1]
			
print passphrase
