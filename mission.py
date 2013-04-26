# MISSION Implemenation File

import sys, errors, time, os, fileinput, re, random, string, game, robnrest, fight

def mission(missionNum):
	os.system('clear')
	if(missionNum != 5):
		print(fight.hilight("Going into a mission...", '30',1))
		time.sleep(2) #Wait 2 seconds
		file_name = "Mission"+str(missionNum)+".txt"
		file = open("Missions/"+file_name, 'r')
		fights = 0
		#Automatic resting before the mission
		print(fight.hilight("You gotta rest before going into a mission!",'33',1))
		time.sleep(2)
		robnrest.rest()
		for lines in file:
			print lines.rstrip('\n')
			time.sleep(2)
		raw_input("Press any button to start the mission" + fight.hilight(" [Remember once you start a mission you can't stop!]",'31',1))
		game.changeAttr(6, "3")
		#fights
		print(fight.hilight("You try to be sneaky but man you're a gangster not some ninja... get ready to fight!",'31',1))
		while fights != 2:
			fight.missionfight(missionNum,fights)
			fights = fights+1
		print(fight.hilight("Voice: Oi Oi Oi, What's going on...",'31',1))
		game.displayfile("Images/ascii_buff_dude.txt")
		raw_input(fight.hilight("PREPARE FOR THE BOSS FIGHT! [Press any key to start]", '33',1))
		fight.missionfight(missionNum+10,0)
		#Increase mission in character file once mission is completed
		mission_number = str(missionNum + 1)
		game.changeAttr(5, mission_number)
		#end mission scene
		endMission(missionNum)
		if missionNum == 4:
			endGame()			
	else:
		print(fight.hilight("You beat the game! Feel free to go around beating up and robbing strangers though, the hood is yours!", '32',1))
#The story end scene for missions
def endMission(missionNum):
	if missionNum == 1:
		print(fight.hilight("You: TELL ME WHAT YOU KNOW!!!!", '36', 1))
		time.sleep(1)
		print(fight.hilight("Tank Sartov: Man, dawg, dude, I don't know anything.. really... We're just a small gang hombre",'31',1))
		time.sleep(1)
		print(fight.hilight("You: Look you better tell chico! I didn't bust my @#@ to get nothing out of this!", '36', 1))
		time.sleep(1)
		print(fight.hilight("Tank Sartov: Okay okay man... I just heard that the big gangs were after a guy cause he had something they wanted... thats all! I SWEAR!",'31',1))
		time.sleep(1)
		print(fight.hilight("You: I had something they want? Damn... like I would remember... Well I should put you out before you can get revenge", '36', 1))
		time.sleep(1)
		print(fight.hilight("Tank Sartov: What the heck man?? HEY NOOOO!!!",'31',1))
		time.sleep(.5)
		os.system('clear')
		raw_input(fight.hilight("CONGRATULATIONS MAN! YOU BEAT MISSION 1!!",'32',1) + fight.hilight(" [Press any key to continue]",'33',1))
	elif missionNum == 2:
		print(fight.hilight("You: You better tell me why you took me and everything you know homie... or things are about to get real!", '36',1))
		time.sleep(1)
		print(fight.hilight("Unkown Boss: Alright, alright... I'm the leader of The Big Nasty, Big N, man... we just some small fries... ",'31',1))
		time.sleep(1)
		print(fight.hilight("Big N: We were told to kidnap you and get rid of you, the big gangs wanted you out dude! I don't know why I don't ask any questions homie!", '31',1))
		time.sleep(1)
		print(fight.hilight("You: Well you shoulda just done me in for when you can! Tell me who should I repay for these bruises?? If not you can always get the payment...",'36',1))
		time.sleep(1)
		print(fight.hilight("Big N: Whoa whoa dawg, not me thats for sure! If anything you should seek out Big Benny of the Grande Nachos! You can find their hangout under the bridge",'31',1))
		time.sleep(1)
		print(fight.hilight("You: Thanks bud... here's a good bye gift for alllll you've done for me",'36',1))
		time.sleep(1)
		print(fight.hilight("Big N: HEY MAN WHAT???? AHGHHHHHH!",'31',1))
		time.sleep(5)
		os.system('clear')
		raw_input(fight.hilight("CONGRATULATIONS MAN! YOU BEAT MISSION 2!!",'32',1) + fight.hilight(" [Press any key to continue]",'33',1))
	elif missionNum == 3:
		print(fight.hilight("You: Nobody messes with my girl and gets away with it!", '36',1))
		time.sleep(1)
		print(fight.hilight("Big Benny: ight homes, calm down... they made us do it ok?",'31',1))
		time.sleep(1)
		print(fight.hilight("You: CALM DOWN? Yo yous about to get a good taste of my boot if you don't start talkin", '36',1))
		time.sleep(1)
		print(fight.hilight("Big Benny: It was the Red Panthers man.. The baddest gang in town..",'31',1))
		time.sleep(1)
		print(fight.hilight("*Big Benny is bleeding all over the place and starting to loose conciousness",'30',1))
		time.sleep(1)
		print(fight.hilight("You: The Red Panthers!? Who are they?! Where's their base?!",'36',1))
		time.sleep(1)
		print(fight.hilight("Big Benny: *pant*... They.. Their base is over... *gasp*..",'31',1))
		time.sleep(1)
		print(fight.hilight("You: WHERE? WHERE ARE THEY?!",'36',1))
		time.sleep(1)
		print(fight.hilight("*Big Benny falls over and passes out. You turn around just in time to see lil'Barso getting up and driving away with Daisy tied up in the back seat...",'30',1))
		time.sleep(1)
		print(fight.hilight("*You break into a nearby car and hot wire it. You speed off in the direction lil'Barso went...",'30',1))
		time.sleep(5)
		os.system('clear')
		raw_input(fight.hilight("CONGRATULATIONS MAN! YOU BEAT MISSION 3!!",'32',1) + fight.hilight(" [Press any key to continue]",'33',1))
	elif missionNum == 4:
		print(fight.hilight("Big Cat: Congrats homes... .. You're now king of these streets.. ", '31',1))
		time.sleep(1)
		print(fight.hilight("*Big Cat falls over",'30',1))
		time.sleep(1)
		print(fight.hilight("*You rush over and untie Daisy", '30',1))
		time.sleep(1)
		print(fight.hilight("Daisy: Oh! I knew you would save me!",'33',1))
		time.sleep(1)
		print(fight.hilight("You: Of course I would doll",'36',1))
		time.sleep(1)
		print(fight.hilight("*Daisy hugs you and nuzzles under your arm",'30',1))
		time.sleep(1)
		print(fight.hilight("You: What do you say we get outta here, babe?",'36',1))
		time.sleep(1)
		print(fight.hilight("*Daisy nods",'33',1))
		time.sleep(5)
		os.system('clear')
		raw_input(fight.hilight("CONGRATULATIONS MAN! YOU BEAT MISSION 4!!",'32',1) + fight.hilight("[Press any key to continue]",'33',1))
	robnrest.incexp(int(game.parse("Level"))*100, int(game.parse("Level"))*150) # Add Experience
	time.sleep(2) 	
def endGame():
	endScene = 1 #Number scene 
	while endScene < 8:
		os.system('clear')
		game.displayfile("End/End"+str(endScene)+".txt")
		endScene = endScene + 1
		time.sleep(1)
	time.sleep(3)
	game.displayfile("End/End"+str(endScene)+".txt")
	print(fight.hilight("Congratulations on beating Grand Theft Manual! You can continue robbing and beating up people however you want!",'32',1))
	time.sleep(3)
	
