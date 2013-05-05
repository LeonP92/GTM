# Authors: Leon Pham, Grant Spence, Eric Owen, Martin Anilang 
# ROBNREST Implemenation File

import sys, errors, time, os, fileinput, re, random, string, game, fight

#Rob function: Will give a chance to rob someone, if chances fail then you will have to fight them.
def rob(environment):
	if random.randrange(0,11)>8:
		print(fight.hilight("You successfully robbed someone!",'32',1))
		addmoney(1, 50)
		return -1
	else:
		print(fight.hilight("Uh oh...\nStranger: Hey punk, who do you think you're robbing?!... PREPARE TO GET YO KNEES BUSTED SON!",'31',1))
		time.sleep(2)
		# If you won the fight, get stuff from guy
		if fight.fight(environment, int(game.parse("Level"))*75, int(game.parse("Level"))*150):
			return -1
		else:
			return 0
#Restores all HP
def rest():
	temp = 0
	sleep = 0
	Rest = "Resting"
	health = int(game.parse("Level"))*50 + 100
	game.changeAttr(2, str(health))
	while temp != 7: #Displays a screen
		os.system("clear")
		if Rest == "Resting...":
			game.displayfile("Images/ascii_sleep.txt")
			Rest = "Resting"
			print(Rest)
			sleep = 0
		else:
			if sleep == 0:
				game.displayfile("Images/ascii_sleep1.txt")
			else:
				game.displayfile("Images/ascii_sleep2.txt")
			Rest = Rest + "."
			print(Rest)
			sleep = sleep + 1
		temp = temp + 1
		time.sleep(1) #Waits 1 second
	print(fight.hilight("You've rested and your health has been recovered!", '32', 1))
#Adds money depending on a random int
def addmoney(int1, int2):
	earned = random.randrange(int1, int2)
	money = int(game.parse("Money")) + earned #random amount of money
	print(fight.hilight("You got " + str(earned) + " cash money homie!",'32',1))
	game.changeAttr(3, str(money)) #changes money in character file
#Adds experience depending on random ints parameter
def incexp(int1, int2):
	level = int(game.parse("Level"))
	earned = random.randrange(int1, int2)
	currentExp = int(game.parse("Experience")) + earned
	print(fight.hilight("You gained " + str(earned) + " street cred!",'32',1))
	# depending on what the user experience is it has a chance to level up
	if level*500 <= currentExp:
		level = level + 1
		print(fight.hilight("YOU LEVELED UP IN DA HOOD! You're now level " + str(level), '32',1))
		game.changeAttr(1, str(level)) #Increase level
		# this is for rollover exp when the user levels
		currentExp = currentExp - ((level-1)*500)
	game.changeAttr(7, str(earned + currentExp)) #Change exp 
