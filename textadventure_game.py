#!/bin/python3

#-A Script by Leo Platti
# Made in 2021 to work on my if else statements in python

import sys
from colorama import Fore, Back, Style

answer = input("Would you like to play my survival game? (yes/no):")

if answer.lower().strip() == "yes":
	
	print("-"*150)
	answer = input("You awake in the middle of an open field along a dirt path, in the dead of winter. There is a fork in the path and you must choose which way to go. (left/right):").lower().strip()
	if answer == "left":
		answer = input("You follow the path into a wooded area and notice a figure standing within the trees. Do you approach it? (yes/no):").lower().strip()
		if answer == "no":
			answer = input("You continue to follow the trail and come across a small house, do you search it or leave the area? (search/leave):").lower().strip()
			if answer == "leave":
				print("You begin walking, when you step on a bear trap hidden in the dead leaves on the ground. You bleed out and die. GAME OVER")
				exit()
			else:
				answer = input("You walk up to the door and knock, looking to see if anyone may be home... no-one answers. Do you break in? (yes/no):").lower().strip()
				if answer == "yes":
					answer = input("Do you break in the front door or window? (Door/Window):").lower().strip()
					if answer == "door":
						print(Fore.YELLOW + "As you open the door your blinded by a bright light. It fades and you wake up at home in your warm bed. The whole thing was a dream... You Won!")
					else:
						print(Fore.RED + "You attempt to break the window but cut yourself and the smell of fresh blood attracts a horde of zombies. You are unable to escape and are eaten alive. GAME OVER")
						exit()
				else:
					print(Fore.RED + "You continue to follow the trail but fall ill and die of starvation and hypothermia. GAME OVER")
					exit()
	
		else:
			print(Fore.RED + "You approach the figure, but as you get close it turns around and bites a chunk of flesh out of your neck! GAME OVER")
			exit()
	else:
		print(Fore.RED + "You follow the trail along a stream. Eventually you fall on a patch of ice. You break your leg and become surrounded by the zombies, unable to escape. GAME OVER")
		exit()
else:
	print(Fore.RED + "Maybe another time...")
	exit()
