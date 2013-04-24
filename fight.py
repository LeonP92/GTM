import sys, errors, time, os, fileinput, re, random, string, game, robnrest

fighters = ('Louie','Bob','Darren','Big Boy Bruno','Tyrone','Pedro','Hilter','Martin','Hobo Martin','Fat Joe',\
'Oscar','Alfonso','Swollen Lou','Butter Knife Pietro','Busted Kneecaps Fabrizio','Petty Crime Salvatore') #Fighter's names
#Description: Function for the fight scene
def fight(environment):
	os.system("clear")
	# Determine fighter
	if environment == "store":
		fighter = "Clerk"
	elif environment == "street":
		fighter = fighters[random.randrange(len(fighters))]
	elif environment == "bank":
		fighter = "Cop"
	elif environment == "stranger":
		fighter = "Stranger"
	fighterHealth = int(game.parse("Level"))*random.randrange(60,120)
	print(fighter+" wants to throw some punches!")
	print(fighter+"'s health is "+str(fighterHealth))
	time.sleep(2)
	os.system("clear")
	damage = 0
	# Fight and move selection
	myHealth = int(game.parse("Health"))

	while myHealth>0 and fighterHealth>0:
		printHealth(myHealth)
		print(hilight(fighter+"'s health is  "+str(fighterHealth),'31',1))
		damage = userFightMove(fighter)
		if damage>0:
	                time.sleep(2)
        	        os.system("clear")
			fighterHealth=fighterHealth - damage
			if fighterHealth<=0:
				break
			print(hilight(fighter+"'s health is now "+str(fighterHealth),'34',1))
		elif damage==-1:
			break
		time.sleep(2)
		os.system("clear")
		print(fighter+"'s Move..")
		# Fighter's Move
		damage = attack("Fighter",5)
		if damage>0:
			myHealth=myHealth-damage
			if myHealth<=0:
				break
			else:
				printHealth(myHealth)
				game.changeAttr(2, str(myHealth))
		time.sleep(4)
		os.system("clear")
	if fighterHealth<=0:
		print(hilight("You won!",'32',1))
		robnrest.addmoney(20,70)
		robnrest.addexp(20, 100)
		time.sleep(2)
	elif myHealth<=0:
		print(hilight("You lost loser...",'31',1))
		#Calculate the amoutn of money and experience lost
		moneyLost = str(int(game.parse("Money"))-int(int(game.parse("Money"))*.1))
		expLost = str(int(game.parse("Experience")) -  int(int(game.parse("Experience"))*.2))
		game.changeAttr(3, moneyLost)
		game.changeAttr(7, expLost)
		#displays amount lost
		print(hilight("You lost " + moneyLost + " dollas and " + expLost + " experience! Pick on someone you can take dawg", '31',1))
		tempvar= raw_input("Continue the game? " + hilight("[Y to continue and anything else to return to main menu]", '33',1)).lower()
		if tempvar == 'y': #continue game from last stop point
			robnrest.rest()
			game.continuegame()
		else: #sends back to game menu
			health = int(game.parse("Level"))*50 + 100
			game.changeAttr(2, str(health))
			game.greetings()
	time.sleep(5)
#Description: Function for the fight scene
def missionfight(mission):
	os.system("clear")
	# Determine fighter
	if mission == 1:
		fighter = "Los Rochos Scrub" #Los Rochos scrub
	elif environment == 11: 
		fighter == "Los Rochos Boss: Tank Sartov"
	elif environment == 2:
		fighter = 4
	elif environment == 12:
		fighter = 6
	#mission health even is boss
	if mission>10 == 0:
		fighterHealth = int(game.parse("Level"))*random.randrange(100,200) + 200
	else:
		fighterHealth = int(game.parse("Level"))*random.randrange(20,100) + 100
	print(fighter+": You'll regret messing with us!")
	print(fighter+"'s health is "+str(fighterHealth))
	time.sleep(2)
	os.system("clear")
	damage = 0
	# Fight and move selection
	myHealth = int(game.parse("Health"))
	while myHealth>0 and fighterHealth>0:
		printHealth(myHealth)
		print(hilight(fighter+"'s health is  "+str(fighterHealth),'31',1))
		damage = userFightMoveMission(fighter)
		if damage>0:
	                time.sleep(2)
        	        os.system("clear")
			fighterHealth=fighterHealth - damage
			if fighterHealth<=0:
				break
			print(hilight(fighter+"'s health is now "+str(fighterHealth),'34',1))
		elif damage==-1:
			break
		time.sleep(2)
		os.system("clear")
		print(fighter+"'s Move..")
		# Fighter's Move
		damage = attack("Fighter",5)
		if damage>0:
			myHealth=myHealth-damage
			if myHealth<=0:
				break
			else:
				printHealth(myHealth)
				game.changeAttr(2, str(myHealth)) #Updates health in character file
		time.sleep(4)
		os.system("clear")
	if fighterHealth<=0:
		print(hilight("You won!",'32',1))
		print
		robnrest.addmoney(50,120)
		robnrest.addexp(70, 150)
		time.sleep(2)
	elif myHealth<=0:
		print(hilight("You lost loser...",'31',1))
		#Calculate the amoutn of money and experience lost
		moneyLost = str(int(game.parse("Money"))-int(int(game.parse("Money"))*.1))
		expLost = str(int(game.parse("Experience")) -  int(int(game.parse("Experience"))*.2))
		game.changeAttr(3, moneyLost)
		game.changeAttr(7, expLost)
		#displays amount lost
		print(hilight("You lost " + moneyLost + " dollas and " + expLost + " experience! Take a mission you can handle dude...", '31',1))
		tempvar= raw_input("Continue the game? " + hilight("[Y to continue and anything else to return to main menu]", '33',1)).lower()
		if tempvar == 'y': #Restarts the game from check point
			robnrest.rest()
			game.continuegame()
		else: #Game
			#Resets health
			health = int(game.parse("Level"))*50 + 100
			game.changeAttr(2, str(health))
			game.greetings()
	time.sleep(5)
#Description: Determines User move on thier input
def userFightMove(fighter):
	while(1):
		print(hilight("What do you want to do?",'34',1))
		# Your Move
		userMove = game.usermove(["A) Use Item","B) Punch","C) Kick","D) Run"],0)
		os.system("clear")
		if userMove=='a':
			itemList = getitems()
			if itemList[0]=="A) none\n":
				print(hilight("You have no items bro!",'31',1))
			else:
				print("Choose your item")
				userMove = game.usermove(getitems(),1)
				os.system("clear")
				damage = itemAttack(userMove)
				if not damage == -1:
					return damage
		elif userMove=='b':
			print("You threw a punch at "+fighter)
			return attack("me",5)
		elif userMove=='c':
			print("You threw a kick at "+fighter)
			return attack("me",5)
		elif userMove=='d':
			if random.randrange(0,11)>8:
				print(hilight("WHEW! You got out of this joker's way",'32',1))
				return -1
			else:
				print(hilight(fighter+" grabbed you so you wouldn't run!",'31',1))
				return 0
	return 0
#This is a mission fight so you c
def userFightMoveMission(fighter):
	while(1):
		print(hilight("What do you want to do?",'34',1))
		# Your Move
		userMove = game.usermove(["A) Use Item","B) Punch","C) Kick","D) Run"],0)
		os.system("clear")
		if userMove=='a':
			itemList = getitems()
			if itemList[0]=="A) none\n":
				print(hilight("You have no items bro!",'31',1))
			else:
				print("Choose your item")
				userMove = game.usermove(getitems(),1)
				os.system("clear")
				damage = itemAttack(userMove)
				if not damage == -1:
					return damage
		elif userMove=='b':
			print("You threw a punch at "+fighter)
			return attack("me",5)
		elif userMove=='c':
			print("You threw a kick at "+fighter)
			return attack("me",5)
		elif userMove=='d':
			print(hilight(fighter+": WHERE YOU THINK YOU'RE GOING PUNK!??!",'31',1))
			print(hilight("This is a mission fight! You can't run!" ,'33',1))
			time.sleep(2)
			return 0
	return 0
#Description: Determines the power of an attack
# DamageRange is first value a decent hit will randomize at
def attack(whichFighter,damageRange):
	if whichFighter=="me":
		level = int(game.parse("Level"))
	else:
		level = 0
	for i in range(level+1):
		hitType = random.randrange(0,3)
		if hitType==0 or hitType==1:
			break
	damage = 0
	if hitType==0:
		if whichFighter=="me":
			print(hilight("Whoops. Miss!",'31',1))
		else:
			print(hilight("Whew! He missed!",'32',1))
		return 0
	elif hitType==1:
		damage = random.randrange(damageRange,damageRange+10)
		if whichFighter=="me":
			print(hilight("Cool, a decent Hit of "+str(damage),'33',1))
		else:
			print(hilight("Ouch man, decent hit of "+str(damage),'33',1))
		return damage
	elif hitType==2:
		damage= random.randrange(damageRange+11,damageRange+20)
		if whichFighter=="me":
			print(hilight("HECK YA! Critical Hit of "+str(damage),'32',1))
		else:
			print(hilight("OUCCHHHHH!!!!! Critical Hit of "+str(damage),'31',1))
		return damage
#Description: Determines attack when using an item
def itemAttack(item):
	itemList = getitems()
	if item>len(itemList):
		print("Incorrect selection")
		time.sleep(2)
		os.system("clear")
		return -1
	item = itemList[item-1]
	item = item.replace(") ","")
	item = item.replace("\n","")
	item = item[1:]
	
	if item=="bat":
		return attack("me",10)
	elif item=="knife":
		return attack("me",15)
	elif item=="bow":
		return attack("me",25)
	elif item=="pistol":
		return attack("me",35)
	elif item=="rifle":
		return attack("me",60)
	else:
		print("ERROR: FILE TAMPER")
		return 0
#Description: Returns items user have, uses string to append letters for selection
def getitems():
	allTheLetters = string.uppercase
	returnList = []
	file = open("character.txt","r")
	for i, line in enumerate(file):
		if re.match("Items:",line):
			line = line.replace("Items: ","")
			items = line.split(",")
	for i, item in enumerate(items):
		 returnList.append(allTheLetters[i]+") "+item)
	return returnList
#Description: Changes the color of the string, USE COLOR CHART, bold=1
def hilight(string, color, bold):
	attr = []
	attr.append(color)
	if bold:
		attr.append('1')
	return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
def printHealth(myHealth):
	
	if myHealth>=80:
		print("Your health is "+hilight(str(myHealth),'32',1))
	elif myHealth<80 and myHealth>=30:
		print("Your health is "+hilight(str(myHealth),'33',1))
	elif myHealth<30:
		print("Your health is "+hilight(str(myHealth),'31',1))
	
