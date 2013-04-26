# FIGHT Implemenation File
#import necessary modules
import sys, errors, time, os, fileinput, re, random, string, game, robnrest

fighters = ('Louie','Bob','Darren','Big Boy Bruno','Tyrone','Pedro','Hilter','Martin','Hobo Martin','Fat Joe','Oscar','Alfonso','Swollen Lou','Butter Knife Pietro','Busted Kneecaps Fabrizio','Petty Crime Salvatore') #Fighter's names

#Description: Function for the fight scene
def fight(fighter, hp1=100, hp2=120):
	os.system("clear")
	#displays fighter
	game.displayfile("Images/ascii_bad_guy_with_gun.txt")
	# If it is a stranger, choose stranger
	if fighter == "street":
		fighter = fighters[random.randrange(len(fighters))]
	# Determine fighter health
	fighterHealth = int(game.parse("Level"))*random.randrange(hp1, hp2)
	print(fighter+" wants to throw some punches!")
	print(fighter+"'s health is "+str(fighterHealth))
	time.sleep(4)
	os.system("clear")
	#fight portion
	processFight(fighter,fighterHealth)

#Description: Function for the fight scene
def missionfight(mission,fightNumber):
	os.system("clear")
	#displays fighter
	game.displayfile("Images/ascii_bad_guy_with_gun.txt")
	# Determine fighter
	if mission == 1: #Mission 1
		if fightNumber == 0: #Fight 1
			fighter = "Los Rochos Scrub"
		elif fightNumber == 1: #Fight 2
			print(hilight("Dang Bro, fight this dawg!",'31',1))
			fighter = "Los Rochos Dog"
		elif fightNumber == 2: #Fight 3
			print(hilight("O SNAP YALL, THERE BE A CLOWN IN THIS HOUSE",'31',1))
			fighter = "Los Rochos Clown"
	elif mission == 11: 
		fighter = "Los Rochos Boss: Tank Sartov" #Boss fight for mission 1
	elif mission == 2: #Mission 2
		if fightNumber == 0: #Fight 1
			fighter = "Unknown Hooligan" 
		elif fightNumber == 1: #Fight 2
			print(hilight("Here comes another one!",'31',1))
			fighter = "Unknown Skinny Guy"
		elif fightNumber == 2: #Fight 3
			print(hilight("They just don't make gangsters like they used to!",'31',1))
			fighter = "Unknown guy with a ruler"
	elif mission == 12: #Mission 2 BOSS
		fighter = "Unknown Big Boss"
	elif mission == 3:
		fighter = "Mission 3 henchmen"
	elif mission == 13:
		fighter = "Mission 3 Boss"
	#mission health even is boss
	if mission>10 == 0:
		fighterHealth = int(game.parse("Level"))*random.randrange(150,200) + 200
	else:
		fighterHealth = int(game.parse("Level"))*random.randrange(20,100) + 150
	print(fighter+": You'll regret messing with us!")
	print(fighter+"'s health is "+str(fighterHealth))
	time.sleep(4)
	os.system("clear")
	# Fight and move selection
	processFight(fighter,fighterHealth)

#Description: Processed the events in a fight
def processFight(fighter, fighterHealth):
	damage = 0
	# Fight and move selection
	myHealth = int(game.parse("Health"))
	
	# Fight - While someone is still alive
	while myHealth>0 and fighterHealth>0:
		# Prints Health of both
		printHealth(myHealth)
		print(hilight(fighter+"'s health is  "+str(fighterHealth),'31',1))
		
		# Determine my move and damage I do
		damage = userFightMove(fighter)
		if damage>0:
	                time.sleep(2)
        	        os.system("clear")
			fighterHealth=fighterHealth - damage
			if fighterHealth<=0: # Check if this hit knocked him out
				break
			print(hilight(fighter+"'s health is now "+str(fighterHealth),'34',1))
		elif damage==-1:# User Ran from Battle!
			return

		time.sleep(2)
		os.system("clear")
		print(fighter+"'s Move..")
		# Fighter's Move
		damage = attack("Fighter",5)
		if damage>0: # If hit, calculate my health
			myHealth=myHealth-damage
			if myHealth<=0:
				break # I Lost!
		printHealth(myHealth)
		game.changeAttr(2, str(myHealth))
		time.sleep(4)
		os.system("clear")
	# After Fight has finished, check for winner
	if fighterHealth<=0:
		#displays ascii image for victory
		game.displayfile("Images/ascii_dead_person.txt")
		print(hilight("You won!",'32',1))
		robnrest.addmoney(20,70) # Add money
		robnrest.incexp(20, 100) # Add Experience
		time.sleep(2)
		return 1 # Success
	
	elif myHealth<=0:
		#displays ascii image for death
		game.displayfile("Images/ascii_you_dead.txt")
		time.sleep(2)
		print(hilight("You lost loser...",'31',1))
		#Calculate the amoutn of money and experience lost
		moneyLost = str(int(game.parse("Money"))-int(int(game.parse("Money"))*.1))
		expLost = str(int(game.parse("Experience")) -  int(int(game.parse("Experience"))*.2))
		game.changeAttr(3, moneyLost)
		game.changeAttr(7, expLost)
		#displays amount lost
		print(hilight("You lost " + moneyLost + " dollas and " + expLost + " experience! Pick on someone you can take dawg", '31',1))		    
		# Trying to Rob Clerk, Exit now
		if fighter=="Clerk":
			return 0
		continueGame= raw_input("Continue the game? " + hilight("[Y to continue and anything else to return to main menu]", '33',1)).lower()
		if continueGame == 'y': #continue game from last stop point
			robnrest.rest()
			game.continuegame()
		else: #sends back to game menu
			health = int(game.parse("Level"))*50 + 100
			game.changeAttr(2, str(health))
			game.greetings()
	time.sleep(5)

#Description: Determines User move on thier input
# Returns:	0 = A miss (No Damage)
#		>0 = A Hit (Damage)
#		-1 = User Ran from battle successfully
def userFightMove(fighter):
	# Loop Until user gets it right
	while(1):
		# Inquire Move
		print(hilight("What do you want to do?",'34',1))
		userMove = game.usermove(["A) Use Item","B) Punch","C) Kick","D) Run"],0)
		os.system("clear")
		
		if userMove=='a': # Use Item
			#Check if User has items
			itemList = getitems()
			if itemList[0]=="A) none\n":
				print(hilight("You have no items bro!",'31',1))
			else:
				# Another While loop for selecting item
				while(1):
					print("Choose your item")
					userMove = game.usermove(getitems(),1)
					os.system("clear")
					game.displayfile("Images/ascii_BAM.txt")
					print("Using your item!")
					time.sleep(2)
					damage = itemAttack(userMove)
					if not damage == -1: # Return Success
						return damage
					# If it gets here, User Failed to select actual item
					print(hilight("Dawg choose an actually item ya dig?",'31',1))
		elif userMove=='b': # Punch
			game.displayfile("Images/ascii_fist.txt")
			print("You threw a punch at "+fighter)
			time.sleep(2)
			return attack("me",5)
		elif userMove=='c': # Kick
			game.displayfile("Images/ascii_kick.txt")
			print("You threw a kick at "+fighter)
			time.sleep(2)
			return attack("me",5)
		elif userMove=='d': # Run Attempt
			if int(game.parse("Progress"))==3:
				print(hilight(fighter+": WHERE YOU THINK YOU'RE GOING PUNK!??!",'31',1))
				print(hilight("This is a mission fight! You can't run!" ,'33',1))
				time.sleep(2)
				return 0
			if random.randrange(0,11)>8: # Determine Success
				print(hilight("WHEW! You got out of this joker's way",'32',1))
				return -1 # SUCCESS!
			else:
				print(hilight(fighter+" grabbed you so you wouldn't run!",'31',1))
				return 0 # Failure, No damage
		elif userMove=='i': # Look at chacter file
			game.displayfile("character.txt")
			print(hilight("Hey dude, stop checking yourself out and focus on the fight!", '31',1))
		# Anything else, Incorrect button
		else:
			print(hilight("Hey man what you trying to do?? Pick legit move dawg", '33', 1))
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
		if hitType==1:
			break
	damage = 0
	if hitType==0:
		game.displayfile("Images/ascii_Miss.txt")
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
#Description: Determines attack when User uses an item
# Returns: 	-1 = No Items in list
#		 0 = Items, but incorrect selection
#		>0 = Damage Done by item
def itemAttack(item):
	itemList = getitems()
	if not item>=0 or item>len(itemList):
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
		print(hilight("Dawg, what you doing messing with the character file?!", '31',1))
		print("ERROR: No item found by that name")
		return 0
#Description: Returns items user have, uses string to append letters for selection
def getitems():
	allTheLetters = string.uppercase
	returnList = []
	file = open("character.txt","r")
	for i, line in enumerate(file):
		if re.match("Items:",line):
			line = line.replace("Items: ","")
			items = line.split(" ")
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

#Description: Prints the health of the user
def printHealth(myHealth):
	# Green = Good, Yellow = Ok, Red = Bad
	if myHealth>=80:
		print("Your health is "+hilight(str(myHealth),'32',1))
	elif myHealth<80 and myHealth>=30:
		print("Your health is "+hilight(str(myHealth),'33',1))
	elif myHealth<30:
		print("Your health is "+hilight(str(myHealth),'31',1))

