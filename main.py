#!/usr/bin/env python2
#Main file for the GTM game!
import game, errors, time, fight, shop, robnrest, mission

#default choice list
defchoice = ["A) Fight", "B) Rob", "C) Mission", "D) Shop", "E) Rest"] 

def main():
	userChoice = ""
	gameOn = 0
	gameOn = game.greetings()
	while gameOn==0: 
		print(fight.hilight("\nWhat are you trying to do home boy??",'36',1))
		userChoice = game.usermove(defchoice, 0)
		if userChoice == 'a':
			fight.fight("street", int(game.parse("Level"))*80, int(game.parse("Level"))*150)
		elif userChoice == 'b':
			robnrest.rob("street")
		elif userChoice == 'c':
			sure = raw_input(fight.hilight("Are you sure you want to go into the mission? Most mission are hard unless you're a certain level... Check the help for more info ",'31',1)+fight.hilight("[Press Y if you want to start the mission and any other key to run away like a wimp] ",'33',0)).lower()
			if sure == 'y':
				mission.mission(int(game.parse("Mission")))
			time.sleep(2)
		elif userChoice == 'd':
			shop.showshop(0)
		elif userChoice == 'e':
			robnrest.rest()
		elif userChoice == 'i':
			game.displayfile("character.txt")
		elif userChoice == 'q':
			gameOn = game.initopts()
	print(fight.hilight("I see the hood was too much for you... Come back when you is a man enough to handle it. PEACE",'32',1))
if __name__ == "__main__":
	main()
