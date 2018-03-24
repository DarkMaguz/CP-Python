#!/usr/bin/python3.6

import random

score = 0
NPCscore = 0

handOptions = {"Rock":1,"Paper":2,"Scissor":3}
handPowers = {1:3, 2:1, 3:2}

def clearScreen():
	print("\n" * 100)

clearScreen()
print("Welcome!\nLets play Rock Paper Scissor!")

while True:
	print("Here are your options:")
	for hand, number in handOptions.items():
		print("%d: %s" % (number, hand))

	while True:
		try:
			choice = int(input("Make your move: "))
			if choice < 1 or choice > 3:
				print("Please type in a number between 1 and 3.")
				continue
		except ValueError:
			print("Please type in a number between 1 and 3.")
		else:
			break

	NPCchoice = int(random.randint(1,3))

	clearScreen()
	print("%d vs. %d" % (choice, NPCchoice))
	if NPCchoice == choice:
		print("Draw!")
	elif handPowers[choice] == NPCchoice:
		print("You won this hand!")
		score += 1
	else:
		print("You lost this hand!")
		NPCscore += 1

	print("The score is now %d to you and %d to the NPC." % (score,NPCscore))
