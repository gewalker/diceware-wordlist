#!/usr/bin/python
import os

n_words = 10
separator = ' '
passphrase = []

#	Generate a list of numbers between 11111 and 66666
seed = [str().join(str(int(int(os.urandom(1).encode('hex'), 16)*(6/256.0))+1) for _ in range (5)) for i in range(n_words)]
print seed

#	Import wordlist
wordlist = {}
with open('diceware.wordlist.asc', 'r') as infile:
	for i, rawline in enumerate(infile):
		if 2 <= i <= 7777:
			line = rawline.replace('\n','').split('\t')
			number, word = line[0], line[1]
			wordlist.update({number: word})

#	Lookup number in the diceware wordlist
passphrase = ' '.join([wordlist[x] for x in seed])
print passphrase
	
