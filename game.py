# GAME.py file
import sys, errors, time, os, fileinput, re, random, string,fight

possibleChoice = ('a', 'b', 'c', 'd', 'e', 'q') #used for basic choices
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
		print("Welcome back " + parse("Name") + "\n")
		if parse("Progress") == '1':
			fight.fight("stranger")
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
	file.write("Name: "+ username +"\nLevel: 1\nHealth: 100\nMoney: 0\nItems: none\nMission: 0\nProgress: 1")	

	#Give user the choices / Action taken on choices
	userChoice = usermove(["A) Fight Stranger", "B) Rob Stranger", "C) Talk to Stranger", "D) Shop", "E) Rest"],0)
	if userChoice == 'a':
			fight.fight("stranger")
	else:
		print "HELP"
#Description this will be the basic user move, when they are not in the missions or fights
# *** Input numbers=0 uses ABC numbers=1 uses 1,2,3
def usermove(optionList,numbers):
	possible = 0
	i = 0 #temporary variable
	for items in optionList:
		print(items)
	userChoice=raw_input("Choose your option [Hit Q to quit]: ").lower()
	
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
#Description: This will be show the items in the shop should always take in the parameter of 0 if being called by other functions
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
				if userinput.split()[0] == 'steal': #If first word was steal... then possible = 2
					possible = 1
				else:
					possible = 2
			elif userinput == "q":
				possible = 3
		else:
			break;
	if possible == 0:
		print("What was that? I couldn't understand you.... Try again or leave...")
		showshop(1)
	elif possible == 1: #shop keeper fight
		print "HEY... HEY PUNK, TRYING TO STEAL STUFF? WELL I HOPE YOU CAN FIGHT!"
		fight.fight("shop")
	elif possible != 3 or possible !=1:
		print("Can I do anything else for ya?")
		showshop(1)
	else:
		print("Alright... come again soon!")
#Description: Gets the money from text file
def parse(getItem):
        file = open("character.txt","r")
        for i, line in enumerate(file):
                if re.match(getItem,line):
                        return line.replace(getItem+": ","")

#Description: Changes the value of the desire character attribute in the file
def changeFileValue(attribute,value):
	file = open("character.txt","r")
	
	#if attribute=="health":
		# Replace the health variable
