#!/usr/bin/env python2

import game, errors

def main():
	userChoice = ""
	while True: 
		userChoice = game.usermove(userChoice)
		if userChoice == 'q':
			break
	print("Thanks for playing!")

if __name__ == "__main__":
	main()