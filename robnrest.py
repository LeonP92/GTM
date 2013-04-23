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
		fight.fight(environment)
		return 0
#Restores all HP
def rest():
	temp = 0
	Rest = "Resting"
	health = int(game.parse("Level"))*50 + 100
	game.changeAttr(2, health)
	while temp != 10: #Displays a screen
		os.system("clear")
		print(Rest)
		if Rest == "Resting....":
			Rest = "Resting"
		else:
			Rest = Rest + "."
		temp = temp + 1
		time.sleep(1) #Waits 1 second
	print(fight.hiilight("You've rest and your health has been recovered!", '32', 1))
#Adds money tdepending on a random int
def addmoney(int1, int2):
	earned = randrange(int1, int2)
	money = int(game.parse("Money")) + earned #random amount of money
	print(fight.hilight("You got " + str(earned) + " cash money homie!",'32',1))
	game.changeAttr(3, str(money)) #changes money in character file
#Adds experience depending on random ints parameter
def incexp(int1, int2):
	level = int(game.parse("Level"))
	earned = randrange(int1, int2)
	currentExp = int(game.parse("Experience")) + earned
	print(fight.hilight("You gained " + earned + " street cred!"))
	if level*500 <= currentExp:
		level = level + 1
		print(fight.hilight("YOU LEVELED UP IN DA HOOD! You're now level " + str(level), '32',1))
		game.changeAttr(1, str(level)) #Increase level
		currentExp = currentExp - (level*500)
	game.changeAttr(7, str(earned + currentExp)) #Change exp 
