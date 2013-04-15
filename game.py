import sys, errors

possibleChoice = ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'Q', 'q')

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
	
