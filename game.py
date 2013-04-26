# GAME.py file
import sys, errors, time, os, fileinput, re, random, string,fight, shop, robnrest, mission

possibleChoice = ('a', 'b', 'c', 'd', 'e', 'q', 'i') #used for basic choices
listOfAtts = ("Name","Level", "Health","Money","Items","Mission","Progress", "Experience")
#Description: This will display the original display/ introduction screen for the GTA game
#Inputs: None
#Outputs: Greetings
def greetings():
	toReturn = 0 #return var
	#Greeting part
	sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=130))
	os.system("clear")
	for line in open("Greeting.txt", "r"): #output lines
		sys.stdout.write(fight.hilight(line,'36',1)) #print line
		time.sleep(.3)#sleep for 0.5 second
	time.sleep(3)
	toReturn = initopts()
	return toReturn
#Description: Initial options allows user to choose if they would like to start a new game or continue
def initopts():
	toReturn = 0
	print(fight.hilight("		Welcome to Grand Theft Manual!		", '31',1))
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
		choice = raw_input(fight.hilight("A file already exists, would you like to overwrite the current game?\nPress Y for yes and anything else for no: ",'31',1)).lower()
		if choice == "y":
			print(fight.hilight("Overwriting files..." ,'33',1))
			time.sleep(3)
			file = open("character.txt","w")
			file = open("character.txt", "a+")
			intro(file, 0)
			file.close()
		else:
			print("\n")
			initopts()
	else:
		file = open("character.txt", "a+")
		intro(file, 0)
		file.close()
#Description: This will continue a game  if one is already saved if not it will return the user to the main menu
def continuegame():
	os.system("clear")
	fileExists = errors.filecheck('character.txt')
	if fileExists == 0:
		print("Resuming saved game...")
		time.sleep(1)
		print(fight.hilight("Welcome back " + parse("Name") + "\n", '32',1))
		time.sleep(2) #Give some time
		if int(parse("Progress")) == 1:
			file = open("character.txt", "a+")
			intro(file, 1)
			file.close()
		elif int(parse("Progress")) == 3:
			mission.mission(int(parse("Mission")))
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
#Description: This is when user name and such will be recorded , prog is to display original message or no
def intro(file, prog): 
	#waking up
	if prog == 0:
		os.system("clear")
		print(".....")
		time.sleep(2)
		print(".... Ugh... My head hurts... Where am I?")
		time.sleep(2)
		#Stranger encountered
		print(fight.hilight("Stranger: Hey buddy, you okay?",'32',1))
		print(fight.hilight("Stranger: You looked pretty roughed up man... the gangs around get ya?",'32',1))
		time.sleep(3)
		print(fight.hilight("Stranger: Not much of a talker eh? What's your name??",'32',1))
		username = raw_input(fight.hilight("You: Uh.... I'm... [Type in your name]\n",'36',1))
		time.sleep(2)
		print(fight.hilight("Stranger: Well " + username + " it's not safe to lay around here... what do you want to do??",'32',1))
		#Writes in character file
		file.write("Name: "+ username +"\nLevel: 1\nHealth: 150\nMoney: 0\nItems: none\nMission: 1\nProgress: 1\nExperience: 0")	
		file.close()
	#Give user the choices / Action taken on choices
	if prog == 1:
		print("Well... What do you want to do??")
	userChoice = usermove(["A) Fight Stranger", "B) Rob Stranger", "C) Talk to Stranger", "D) Shop", "E) Rest"],0)
	if userChoice == 'a':
		print (fight.hilight("Stranger: Hey what are you trying to do??!?!?!",'31',1)) #Fight stranger
		print("Prepare to fight the stranger!")
		time.sleep(2)
		fight.fight("Stranger")
		changeAttr(6, "2")
	elif userChoice == 'b': #Rob Stranger
		print("You just met the poor guy... but okay..")
		robnrest.rob("stranger") #Rob him
		changeAttr(6, "2")
	elif userChoice == 'c': #Talking to stranger
		print("You: Hey....") 
		changeAttr(6, "2")
	elif userChoice == 'd': #Going to the shop
		print(fight.hilight("Stranger: You want to go to the shop? Alright, I'll take you there G, but I gotta dip after",'32',1))
		changeAttr(6, "2")
		shop.showshop(0)
	elif userChoice == 'e': #Rest but you don't need it
		print(fight.hilight("\nYou just woke up! You don't need a rest yet...",'31',1))
		file = open("character.txt", "a+")
		intro(file, 1)
		file.close()
	elif userChoice == 'i':
		print(fight.hilight("Stranger: Checking yourself out?? You is a weird one aren't ya?", '32',1))
		displayfile("character.txt")
		file = open("character.txt", "a+")
		intro(file, 1)
		file.close()
	else:
		print(fight.hilight("Stranger: I guess you're leaving! be safe, peace out homie", '32',1))
		print(fight.hilight("... You left the stranger\n", '33', 1))
		changeAttr(6, "2")
#Description this will be the basic user move, when they are not in the missions or fights
# *** Input numbers=0 uses ABC numbers=1 uses 1,2,3
def usermove(optionList,numbers):
	possible = 0
	i = 0 #temporary variable
	for items in optionList:
		print(items)
	userChoice=raw_input("Choose your option "+fight.hilight("[Hint: Hit Q to quit and I to view character info]: ",'33',1)).lower()
	
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

#Description: Gets the money from text file
def parse(getItem):
        file = open("character.txt","r")
        for i, line in enumerate(file):
                if re.match(getItem,line):
                        return line.replace(getItem+": ","")
	file.close()
#Description: Changes the value of the desire character attribute in the file
#For line,  0 = Name, 1 = Level, 2 = Health, 3 = Money, 4 = items, 5= mission, 6 = progress, 7= Experience
def changeAttr(line, text):
	lines = open("character.txt", 'r').readlines()
	if line == 4: #if item is being changed then don't remove all items...
		if lines[4].split()[1] == 'none': #no item then remove whole line
			lines[line] = listOfAtts[line] + ": " + text +"\n"
		else:
			lines[line] = lines[line].rstrip('\n')  + " " + text + "\n" #adds item
	else: #if it's not item change entire line
		lines[line] = listOfAtts[line] + ": " + text + "\n"
	out = open("character.txt", 'w')
	out.writelines(lines)
	out.close()
#displays a file, used mainly for showing info when user press i
def displayfile(file):
	file = open(file, 'r')
	print("")
	for lines in file:
		print fight.hilight(lines.rstrip('\n'),'35',1)
	print("")
