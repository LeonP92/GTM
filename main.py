#!/usr/bin/env python2

import game, errors, time

def main():
	userChoice = ""
	gameOn = 0
	game.fight("street")
	gameOn = game.greetings()
	while gameOn==0: 
		userChoice = game.usermove(["A) Fight Stranger", "B) Rob Stranger", "C) Rest", "D) Shop", "E) Cry"],0)
		if userChoice == 'd':
			game.showshop(0)
		if userChoice == 'q':
			break
	print("Thanks for playing!")
if __name__ == "__main__":
	main()
