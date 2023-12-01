#!/bin/python3

# This script was made by Lmmp04 and uploaded to github

import random
import sys

ans = input("Would you like to roll [1] or [2] dice? : ").strip()

numbers = [1, 2, 3, 4, 5, 6]

if ans == "1":
	print ("Rolling the die...")
	print ("It landed on : ")
	print (random.sample(numbers,1))
	exit()

if ans == "2":
	print ("Rolling the dice...")
	print ("They landed on : ")
	print (random.sample(numbers,2))
	exit()

else:
	print ("Invalid Option")
	exit()
