import sys, errors, time, os

possibleChoice = ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'Q', 'q')

#Description: This will display the original display/ introduction screen for the GTA game
#Inputs: None
#Outputs: Greetings
def greetings():
	print("********************************************************")
	time.sleep(1) #sleeps for 1 seconds
	print("*    _________       ____________     _____________    *")
	time.sleep(1) 
	print("*    |                    |           |     |     |    *")
	time.sleep(1) 
	print("*    |     ___            |           |     |     |    *")
	time.sleep(1)
	print("*    |       |            |           |     |     |    *")
	time.sleep(1) 
	print("*    |_______|            |           |     |     |    *")
	time.sleep(1) 
	print("*                                                      *")
	time.sleep(1) 
	print("********************************************************")
	time.sleep(3)
	os.system('clear')
	initopts()
#Description: Initial options allows user to choose if they would like to start a new game or continue
def initopts():
	print("		Welcome to Grand Theft Manual!		\n")
	print("1) Start a new game \n2) Continue \n3) Help ")
	userinput = input("Please choose one of the options by pressing 1, 2, or 3...\n")
	
	if userinput == 1: 
		print("Starting a new game!")
	elif userinput == 2:
		print("Continuing an old game!")
	elif userinput == 3: 
		print("Help!")
	else: 
		print("Your input was incorrect! Please try again!")
		initopts()
def usermove(userChoice):
	possible = 0
	print("Test input")
	userChoice=raw_input("Choose your option: \n")
	
	for choice in possibleChoice:
		if possible == 0: 
			if choice == userChoice:
				possible = 1;
		else:
			break
	if possible == 1:
		userChoice = userChoice.lower()
		return userChoice
	else:
		errors.badChoice()
	
