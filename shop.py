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
		print(fight.hilight("\nWelcome to the weapon shop!",33,1) + fight.hiilight("BETTER NOT STEAL ANYTHING...", '31',1))
		print data
		f.close()
	userinput = raw_input("What do you need from me??" +fight.hilight("[Hint: Type in what you want, you can also type 'steal [item name]' but be prepared to fight the shop keeper! Also hit Q to quit and I for character info]\n",'33',1)).lower()
	for item in items:
		if possible == 0:
			if userinput == item: #item match without stealing
					possible = 2
			elif userinput.split()[0] == 'steal': #If first word was steal... then possible = 2
					possible = 1
			elif userinput == "q":
				possible = 3
			elif userinput =="i":
				possible = 4
		else:
			break;
		itemCost = itemCost+1
	if possible == 0:
		print("What was that? I couldn't understand you.... Try again or leave...")
		showshop(1)
	elif possible == 1: #shop keeper fight
		print fight.hiilight("HEY... HEY PUNK, TRYING TO STEAL STUFF? WELL I HOPE YOU CAN FIGHT!",'31',1)
		fight.fight("shop")
	elif possible == 3:
		print("Alright... come again soon!")
	elif possible == 4:
		game.displayfile("character.txt")
		showshop(1)
	else:
		if money >= (itemCost*300) :
			game.changeAttr(3, str(money - (itemCost*300)))
			game.changeAttr(4, items[itemCost-1])
			print("\nItem Purchased! You bought: " + items[itemCost-1] +". You now have: $" + game.parse("Money"))
			print("Can I do anything else for ya?")
		else:
			print("\nHey That item costs: " + str(itemCost*300) + "!")
			print("You don't have enough money for that punk! You trying to pull a quick one on me???? EHH???")
		showshop(1)