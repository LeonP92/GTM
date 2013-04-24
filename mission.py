import sys, errors, time, os, fileinput, re, random, string, game, robnrest, fight

def mission(missionNum):
	os.system('clear')
	print(fight.hilight("Going into a mission...", '30',1))
	time.sleep(2) #Wait 2 seconds
	file_name = "Mission"+str(missionNum)+".txt"
	file = open("Missions/"+file_name, 'r')
	fights = 0
	#Automatic resting before the mission
	robnrest.rest()
	for lines in file:
		print lines.rstrip('\n')
		time.sleep(2)
	raw_input("Press any button to start the mission" + fight.hilight("[Remember once you start a mission you can't stop!]",'31',1))
	game.changeAttr(6, "3")
	#fights
	print(fight.hilight("You try to be sneaky but man you're a gangster not some ninja... get ready to fight!",'31',1))
	while fights != 3:
		fight.missionfight(missionNum)
	print(fight.hilight("Voice: Oi Oi Oi, What's going on...",'31',1))
	raw_input(fight.hilight("PREPARE FOR THE BOSS FIGHT! [Press any key to start]", '33',1))
	fight.missionfight(missionNum+10)
	#Increase mission in character file once mission is completed
	mission_number = str(missionNum + 1)
	game.changeAttr(5, mission_number)
	#end mission scene
	endMission(missionNum)
#The story end scene for mission 1
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
		raw_input(fight.hilight("CONGRATULATIONS MAN! YOU BEAT MISSION 1!!",'32',1) + fight.hilight("[Press any key to continue]",'33',1))