#!/usr/bin/env python2
#Main file for the GTM game!
import game, errors, time, fight, shop, robnrest, mission

#default choice list
defchoice = ["A) Fight", "B) Rob", "C) Mission", "D) Shop", "E) Rest"] 
#Main message that includes the main while loop to run the game
def main(): 
	userChoice = "" #User choice variable
	game.greetings() #Starts off th game
	while 1:  #Main while loop
		print(fight.hilight("\nWhat are you trying to do home boy??",'36',1)) 
		userChoice = game.usermove(defchoice, 0) #Gets user choice
		if userChoice == 'a': #Gets into a random fight 
			fight.fight("street", int(game.parse("Level"))*80, int(game.parse("Level"))*150)
		elif userChoice == 'b': #Robs chances could also lead into a fight
			robnrest.rob("street")
		elif userChoice == 'c': #Misison
			#Makes sure user really wants to go into a mission
			sure = raw_input(fight.hilight("Are you sure you want to go into the mission? Most mission are hard unless you're a certain level... Check the help for more info ",'31',1)+fight.hilight("[Press Y if you want to start the mission and any other key to run away like a wimp] ",'33',0)).lower()
			if sure == 'y': #If user is sure call on the mission function
				mission.mission(int(game.parse("Mission")))
			time.sleep(2)
		elif userChoice == 'd': #Shows shop
			shop.showshop(0)
		elif userChoice == 'e': #Rests and restores hp
			robnrest.rest()
		elif userChoice == 'i': #Shows character info
			game.displayfile("character.txt")
		elif userChoice == 'q':
			game.initopts() #Quits out of the game 
if __name__ == "__main__":
	main()
