#!/bin/python3

# This script was made by Lmmp04 and uploaded to github.com
# Created in 2022 to practice learning simple python coding

print ("[A]ddition")
print ("[S]ubtraction")
print ("[M]ultiplication")
print ("[D]ivision")
print ("")
	
ans = input("Which of these operations would you like to use? : ").strip().lower()

if ans == "a":
	print ('\n')
	ans1 = float(input("What is the first number you would like to add? : "))
	print ('\n')
	ans2 = float(input("What is the second number you would like to add? : "))
	adding = ans1 + ans2
	print ('\n')
	print ("The sum is : ")
	print (adding)
	
if ans == "s":
	print ('\n')
	ans1 = float(input("What is the first number you would like to subtract? : "))
	print ('\n')
	ans2 = float(input("What is the second number you would like to subtract? : "))
	subtracting = ans1 - ans2
	print ('\n')
	print ("The difference is : ")
	print (subtracting)

if ans == "m":
	print ('\n')
	ans1 = float(input("What is the first number you would like to multiply : "))
	print ('\n')
	ans2 = float(input("What is the second number you would like to multiply : "))
	multiplying = ans1 * ans2
	print ('\n')
	print ("The product is : ")
	print (multiplying)

if ans == "d":
	print ('\n')
	ans1 = float(input("What is the first number you would like to divide? : "))
	print ('\n')
	ans2 = float(input("What is the second number you would like to divide? : "))
	dividing = ans1 / ans2
	print ('\n')
	print ("The quotient is : ")
	print (dividing)

	
