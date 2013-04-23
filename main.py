#!/usr/bin/env python2

import game, errors, time, fight, shop

#default choice list
defchoice = ["A) Fight", "B) Rob", "C) Mission", "D) Shop", "E) Rest"] 

def main():
	userChoice = ""
	gameOn = 0
	gameOn = game.greetings()
	while gameOn==0: 
		userChoice = game.usermove(defchoice, 0)
		if userChoice == 'd':
			shop.showshop(0)
		if userChoice == 'q':
			break
	print("Thanks for playing!")
if __name__ == "__main__":
	main()
