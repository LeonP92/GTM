import sys, errors, time, os, fileinput, re, random, string

possibleChoice = ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'Q', 'q') #used for basic choices
items = ('bat', 'knife', 'bow', 'pistol', 'rifle') #Used for shop info
fighters = ('Louie','Bob','Darren','Big Boy Bruno','Tyrone','Pedro','Hilter','Martin','Hobo Martin','Fat Joe',\
'Oscar','Alfonso','Swollen Lou','Butter Knife Pietro','Busted Kneecaps Fabrizio','Petty Crime Salvatore') #Fighter's names

#Description: This will display the original display/ introduction screen for the GTA game
#Inputs: None
#Outputs: Greetings
def greetings():
	toReturn = 0 #return var
	#Greeting part
	sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=130))
	os.system("clear")
	for line in open("Greeting.txt", "r"): #output lines
		sys.stdout.write(line) #print line
		time.sleep(.5)#sleep for 0.5 second
	time.sleep(3)
	toReturn = initopts()
	return toReturn
#Description: Initial options allows user to choose if they would like to start a new game or continue
def initopts():
	toReturn = 0
	print("		Welcome to Grand Theft Manual!		")
	print("1) Start a new game \n2) Continue \n3) Help \n4) Quit ")
	userinput = raw_input("Please choose one of the options by pressing 1, 2, 3, or 4...\n")
	if userinput == "1": 
		newgame()
	elif userinput == "2":
		continuegame()
	elif userinput == "3": 
		displayhelp()
	elif userinput == "4":
		toReturn = 1
	else: 
		print("Your input was incorrect! Please try again!")
		initopts()
	return toReturn
#Description: This will allow users to create a new game, if there is already a saved game then the user can choose to overwrite the current game or continue
def newgame():
	os.system("clear")
	fileExists = errors.filecheck('character.txt')
	if fileExists == 0:
		choice = raw_input("A file already exists, would you like to overwrite the current game?\nPress Y for yes and anything else for no: ").lower()
		if choice == "y":
			file = open("character.txt","w")
			file = open("character.txt", "a+")
			intro(file)
			file.close()
		else:
			print("\n")
			initopts()
	else:
		file = open("character.txt", "a+")
		intro(file)
		file.close()
#Description: This will continue a game  if one is already saved if not it will return the user to the main menu
def continuegame():
	os.system("clear")
	fileExists = errors.filecheck('character.txt')
	if fileExists == 0:
		print("Resuming saved game...")
		time.sleep(1)
		print("Welcome back " + parse("Name"))
	else:
		print("There is no saved game, please choose another option \n")
		initopts()
#Description: This will display the Help file
def displayhelp():
	os.system("clear")
	f = open("HELP.txt", "r")#opens up help text
	data = f.read() #Reads the entire file
	print data #displays the data
	f.close()
	raw_input("\nPress any key to return to the main menu...")
	initopts()
#Description: This is when user name and such will be recorded
def intro(file): 
	#waking up
	os.system("clear")
	print(".....")
	time.sleep(2)
	print(".... Ugh... My head hurts... Where am I?")
	time.sleep(2)
	#Stranger encountered
	print("Stranger: Hey buddy, you okay?")
	print("Stranger: You looked pretty roughed up man... the gangs around get ya?")
	time.sleep(3)
	print("Stranger: Not much of a talker eh? What's your name??")
	username = raw_input("You: Uh.... I'm... [Type in your name]\n")
	time.sleep(2)
	print("Stranger: Well " + username + " it's not safe to lay around here... what do you want to do??")
	#Writes in character file
	file.write("Name: "+ username +"\nLevel: 1\nHealth: 100\nMoney: 0\nItems: none\nMission: 0")	
#Description this will be the basic user move, when they are not in the missions or fights
# *** Input numbers=0 uses ABC numbers=1 uses 1,2,3
def usermove(optionList,numbers):
	possible = 0
	i = 0 #temporary variable
	for items in optionList:
		print(items)
	userChoice=raw_input("Choose your option [Hit Q to quit]: ")
	
	for choice in possibleChoice:
		if possible == 0: 
			if choice == userChoice:
				possible = 1;
		else:
			break
	if possible == 1:
		if numbers == 0:
			userChoice = userChoice.lower()
		elif numbers == 1:
			userChoice = ord(userChoice.lower()) - ord('a')+1
		return userChoice
	else:
		errors.badChoice()
#Description: This will be show the items in the shop
def showshop(toShow):
	possible = 0
	if toShow==0:
		f = open("items.txt", "r")
		data = f.read()
		print("\nWelcome to the weapon shop! BETTER NOT STEAL ANYTHING...")
		print data
		f.close()
	userinput = raw_input("What do you need from me?? [Hint: Type in what you want, you can also type 'steal [item name]' but be prepared to fight the shop keeper! Also hit Q to quit]\n").lower()
	for item in items:
		if possible == 0:
			if userinput == item:
				possible = 1
			elif userinput == "q":
				possible = 2
		else:
			break;
	if possible == 0:
		print("What was that? I couldn't understand you.... Try again or leave...")
		showshop(1)
	elif possible != 2:
		print("Can I do anything else for ya?")
		showshop(1)
	else:
		print("Alright... come again soon!")
		
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
	fighterHealth = int(parse("Level"))*random.randrange(60,120)
	print(fighter+" has appeared and wants to throw some punches!")
	print(fighter+"'s health is "+str(fighterHealth))
	time.sleep(2)
	os.system("clear")
	damage = 0
	# Fight and move selection
	myHealth = int(parse("Health"))

	while myHealth>0 and fighterHealth>0:
		damage = userFightMove(fighter)
		time.sleep(2)
		os.system("clear")
		if damage>0:
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
			elif myHealth>=80:
				print("Your health is now "+hilight(str(myHealth),'32',1))
			elif myHealth<80 and myHealth>=30:	
				print("Your health is now "+hilight(str(myHealth),'33',1))
			elif myHealth<30:
				print("Your health is now "+hilight(str(myHealth),'31',1))
		time.sleep(4)
		os.system("clear")
	
	if fighterHealth<=0:
		print(hilight("You won!",'32',1))
	elif myHealth<=0:
		print(hilight("You lost loser...",'31',1))
	time.sleep(5)
#Description: Determines User move on thier input
def userFightMove(fighter):
	while(1):
		print("What do you want to do?")
		# Your Move
		userMove = usermove(["A) Use Item","B) Punch","C) Kick","D) Run"],0)
		os.system("clear")
		if userMove=='a':
			print("Choose your item")
			userMove = usermove(getitems(),1)
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
			if random.randrange(0,2)==1:
				print(hilight("WHEW! You got out of this joker's way",'32',1))
				return -1
			else:
				print(hilight(fighter+" grabbed you so you wouldn't run!",'31',1))
	return 0
#Description: Determines the power of an attack
# DamageRange is first value a decent hit will randomize at
def attack(whichFighter,damageRange):
	if whichFighter=="me":
		level = int(parse("Level"))
	else:
		level = 0
	for i in range(level+1):
		hitType = random.randrange(0,3)
		if hitType==0 or hitType==1:
			break
	damage = 0
	if hitType==0:
		print(hilight("Miss yo!",'31',1))
		return 0
	elif hitType==1:
		damage = random.randrange(damageRange,damageRange+10)
		print(hilight("Decent Hit of "+str(damage),'33',1))
		return damage
	elif hitType==2:
		damage= random.randrange(damageRange+11,damageRange+20)
		print(hilight("Critical Hit of "+str(damage),'32',1))
		return damage
#Description: Determines attack when using an item
def itemAttack(item):
	itemList = getitems()
	if not item:
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
#Description: Gets the money from text file
def parse(getItem):	
	file = open("character.txt","r")
	for i, line in enumerate(file):
		if re.match(getItem,line):
			return line.replace(getItem+": ","")
#Description: Changes the color of the string, USE COLOR CHART, bold=1
def hilight(string, color, bold):
	attr = []
	attr.append(color)
	if bold:
		attr.append('1')
	return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

#Description: Changes the value of the desire character attribute in the file
def changeFileValue(attribute,value):
	file = open("character.txt","r")
	
	#if attribute=="health":
		# Replace the health variable
