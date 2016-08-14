#!/bin/bash

SEPARATOR=" "
PASSPHRASE=""

for i in {1..10}
do
#	Generate a number between 11111 and 66666
	RANDOMNUMBER=$(cat /dev/urandom | LC_ALL=C tr -dc '1-6' | fold -w 5 | head -n 1)
	
#	Lookup number in the diceware wordlist
	PASSPHRASE="$PASSPHRASE""$SEPARATOR""$(cat diceware.wordlist.asc |grep $RANDOMNUMBER | awk '{print $2}')"
done

echo $PASSPHRASE
