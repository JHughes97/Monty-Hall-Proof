"""This program proves the Monty Hall problem by way of Monte Carlo Simulation.
   In the Monty Hall problem you are presented with 3 closed doors. Behind one
   of the doors is a car and behind the other two are goats. You may select 1
   door, with the aim of finding the car. Once you have selected a door, one of
   the other doors behind which is a goat is opened. You then have the option to
   stay with the door you originally picked or switch to the other unclosed door.
   Do you have a better chance of finding the car if you stay or switch?"""

#Import door class, switch class, and random module
from Door import Door
from Switch import switch
import random

#set number of simulations
trials = 100000

#create variable to count number of times found the car when switch doors
switchWins = 0
#run the simulation a number of times
for i in range(trials):
	#create 3 door objectts
	doorOne = Door()
	doorTwo = Door()
	doorThree = Door()

	#put car behind a random door
	x = random.randint(1,3)
	for case in switch(x):
		if case(1):
			doorOne.setCar(True)
			break
		if case(2):
			doorTwo.setCar(True)
			break
		if case():
			doorThree.setCar(True)

	#select a random door
	y = random.randint(1,3)
	for case in switch(y):
		if case(1):
			doorOne.setSelected(True)
			break
		if case(2):
			doorTwo.setSelected(True)
			break
		if case():
			doorThree.setSelected(True)

	#open an unselected door with a goay
	if not doorOne.isCar() and not doorOne.isSelected():
		doorOne.setOpened(True)
	elif not doorTwo.isCar() and not doorTwo.isSelected():
		doorTwo.setOpened(True)
	else:
		doorThree.setOpened(True)

	#increase switch wins if switching door would result in finding the car
	if doorOne.isCar() and not doorOne.isSelected() and not doorOne.isOpened():
		switchWins+=1
	elif doorTwo.isCar() and not doorTwo.isSelected() and not doorTwo.isOpened():
		switchWins+=1
	elif doorThree.isCar() and not doorThree.isSelected() and not doorThree.isOpened():
		switchWins+=1

#calculate percentage of times won when switched door
switchWinPercentage = (switchWins/trials)*100
#print results
print("This is a proof of the Monty Hall Problem using Monte Carlo:")
print("___________________________________________________________________________________________")
print("There are three doors.\nBehind one is a car.\nBehind the othrer two are goats.\n")
print("You may select one door. You win if you find the car.\nThen one of the doors you didn't pick, behind which is a goat, is opened.\n")
print("You then have the option to stay with the door you selected or switch to the other unopened door.\n")
print("Chance of winning if you switch door = {}%".format(switchWinPercentage))
print("Chance of winning if you don't switch = {}%".format(100-switchWinPercentage))