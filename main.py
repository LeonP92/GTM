#!/usr/bin/env python2

import game, errors

def main():
	userChoice = ""
	gameOn = 0
	gameOn = game.greetings()
	while gameOn==0: 
		userChoice = game.usermove()
		if userChoice == 'q':
			break
	print("Thanks for playing!")

if __name__ == "__main__":
	main()
