#!/usr/bin/env python2

import game, errors, time, fight, shop, robnrest

#default choice list
defchoice = ["A) Fight", "B) Rob", "C) Mission", "D) Shop", "E) Rest"] 

def main():
	userChoice = ""
	gameOn = 0
	gameOn = game.greetings()
	while gameOn==0: 
		userChoice = game.usermove(defchoice, 0)
		if userChoice == 'a':
			fight.fight("street")
		elif userChoice == 'b':
			robnrest.rob("street")
		elif userChoice == 'c':
			print("Going into a mission...")
			time.sleep(2)
		elif userChoice == 'd':
			shop.showshop(0)
		elif userChoice == 'e':
			robnrest.rest()
		elif userChoice == 'i':
			game.displayfile("character.txt")
		elif userChoice == 'q':
			break
	print(fight.hilight("Thanks for playing!",'32',1))
if __name__ == "__main__":
	main()
