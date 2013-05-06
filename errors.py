#For simple errors: May or may not use
import sys, os

def badChoice():
	print("Error: The choice you chose is not a possible choice")
def filecheck(filename):
	fileVar = 0
	if os.path.isfile(filename):
		fileVar = 0#don't have to do anything
	else:
		fileVar = 1
	return fileVar
