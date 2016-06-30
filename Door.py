"""This class represents a door object.
   It includes an initialisation method, as well as
   methods for setting whether the door holds a car,
   is selected or is opened, and methods to check if
   the door contains a car, is selected or is open"""

class Door:

	#initialisation method
	def __init__(self):
		self.car = False
		self.selected = False
		self.opened = False

	#set whether the door contains a car or not
	def setCar(self,boolean):
		self.car = boolean

	#set whether the door is selected or not
	def setSelected(self,boolean):
		self.selected = boolean

	#set whether the door is open or not
	def setOpened(self,boolean):
		self.opened = boolean

	#returns whether the door contains a car or not
	def isCar(self):
		return self.car == True

	#returns whether the door is selected or not
	def isSelected(self):
		return self.selected == True

	#returns whether the door is opened or not
	def isOpened(self):
		return self.opened == True