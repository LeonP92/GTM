# Authors: Leon Pham, Grant Spence, Eric Owen, Martin Anilang 
# SHOP Implementation File

import game, sys, errors, time, os, fileinput, re, random, string, fight

items = ('bat', 'knife', 'bow', 'pistol', 'rifle') #Used for shop info

#Description: This will be show the items in the shop should always take in the parameter of 0 if being called by other functions
def showshop(toShow):
	possible = 0
	money = int(game.parse("Money"))
	itemCost = 0
	if toShow==0:
		f = open("items.txt", "r")
		data = f.read()
		print(fight.hilight("\nWelcome to the weapon shop!",'33',1) + fight.hilight(" BETTER NOT STEAL ANYTHING...", '31',1))
		print data
		f.close()
	userinput = raw_input("What do you need from me??" +fight.hilight(" [Hint: Type in what you want, you can also type 'steal [item name]' but be prepared to fight the shop keeper! Also hit Q to quit and I for character info]\n",'33',1)).lower()
	for item in items:
		if possible == 0:
			if userinput == item.lower(): #item match without stealing
					possible = 2
			elif userinput.split()[0] == 'steal': #If first word was steal... then possible = 2
					possible = 1
					stealing = userinput.split()[1]
			elif userinput == "q":# to leave
				possible = 3
			elif userinput =="i":# to see info
				possible = 4
		else:
			break;
		itemCost = itemCost+1
	if possible == 0:
		print("What was that? I couldn't understand you.... Try again or leave...")
		showshop(1)
	elif possible == 1: #shop keeper fight
		print fight.hilight("HEY... HEY PUNK, TRYING TO STEAL STUFF? WELL I HOPE YOU CAN FIGHT!",'31',1)
		time.sleep(2)
		fight.fight("shop", int(game.parse("Level"))*220, int(game.parse("Level"))*250)
		canSteal = checkItem(stealing)
		# if you did stole something
		if canSteal == 0:
			print(fight.hilight("NICE WORK MAN! You just stole a "+stealing,'32',1))
			game.changeAttr(4,stealing)
		else: 
			print(fight.hilight("Home slice... you just beat up the poor sucker for no reason. You got this item", '33', 1))
		print(fight.hilight("You: Woops... I guess I went too hard on the fool! Better run!", '36', 1))
		time.sleep(2)
	elif possible == 3:
		print("Alright... come again soon!")
	elif possible == 4:
		game.displayfile("character.txt")
		showshop(1)
	else:
		# see if you can buy an item
		if money >= (itemCost*300) :
			canBuy = checkItem(userinput)
			if canBuy == 0: # can buy
				game.changeAttr(3, str(money - (itemCost*300)))
				game.changeAttr(4, items[itemCost-1])
				print("\nItem Purchased! You bought: " + items[itemCost-1] +". You now have: $" + game.parse("Money"))
			else:
				print(fight.hilight("Man you have that item! You don't want it again!",'31',1))
			print("Can I do anything else for ya?")
		# if the user doesn't have enough money to buy the item
		else:
			print("\nHey That item costs: " + str(itemCost*300) + "!")
			print("You don't have enough money for that punk! You trying to pull a quick one on me???? EHH???")
		showshop(1)
#Prevent user from buying multiple of the same item!
def checkItem(item):
	exists = 0
	text = game.parse("Items")
	text = text.rstrip('\n')
	words = text.split()
	for items in words:
		if exists == 0:
			if item == items.lower():
				exists = 1
		else:
			break
	return exists
		
