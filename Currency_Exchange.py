!/bin/python3

import sys

equal = "="
p = "Pounds "
e = "Euros "
y = "Yen "
c = "CAD "
a = "AUD "

print ("Currency_Converter.py by Lmmp04")
print ("This application converts $USD to its equivalent in foreign currency.")
print ("Keep in mind this applications conversion rates are based on the market as of 2/25/2021")
print ("-"*75)
print ("[P]ounds")
print ("[E]uros")
print ("[Y]en")
print ("[C]anadian Dollar")
print ("[A]ustralian Dollar")
print ("")
ans = input("What currency would you like to convert USD to? : ").lower().strip()
USD = int(input("What is the amount of USD currency you would like to convert? : "))

if ans == "p":
    conversion1 = str(USD * .71)
    print (p + conversion1)
    exit()

if ans == "e":
    conversion2 = str(USD * .82)
    print (e + conversion2)
    exit()

if ans == "y":
    conversion3 = str(USD * 105.92)
    print (y + conversion3)
    exit()
   
if ans == "c":
    conversion4 = str(USD * 1.26)
    print (c + conversion4)
    exit()
   
if ans == "a":
    conversion5 = str(USD * 1.27)
    print (a + conversion5)
    exit()
