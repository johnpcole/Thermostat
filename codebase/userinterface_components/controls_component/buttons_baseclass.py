from ...common_components.appinput_framework import appinput_module as AppInput
from ...common_components.vector_datatype import vector_module as Vector



class DefineButtons:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================


	def __init__(self):

		# Initialises the pygame input controller
		self.inputobject = AppInput.createappinput()

		# Sets up the buttons
		self.area = {}
		self.setupbuttons()



	def setupbuttons(self):

		self.definebutton("Start Menu",           0,   0, 480, 320, [])
		self.definebutton("Temp Slider",         24, 24,  432,  80, ["Set Temp"])
		self.definebutton("Override Next",       30, 150,  50,  50, ["Set Temp"])
		self.definebutton("Override 30",        104, 150,  50,  50, ["Set Temp"])
		self.definebutton("Override 60",        178, 150,  50,  50, ["Set Temp"])
		self.definebutton("Override 120",       252, 150,  50,  50, ["Set Temp"])
		self.definebutton("Override 180",       326, 150,  50,  50, ["Set Temp"])
		self.definebutton("Override Lock",      400, 150,  50,  50, ["Set Temp"])
		self.definebutton("Temp Cancel",         15, 255,  50,  50, ["Set Temp"])
		self.definebutton("Temp Commit",        415, 255,  50,  50, ["Set Temp"])





	def definebutton(self, buttonname, along, down, width, height, groupmembership):

		self.inputobject.createarea(buttonname, Vector.createfromvalues(along, down),
															Vector.createfromvalues(width, height), groupmembership)





	# ==========================================================================================
	# Perform Actions
	# ==========================================================================================



	# -------------------------------------------------------------------
	# Update button states
	# -------------------------------------------------------------------

	def updatebutton(self, buttonname, buttonstate):

		self.inputobject.setareastate(buttonname, buttonstate)



	# -------------------------------------------------------------------
	# Update button positions
	# -------------------------------------------------------------------

	#def updatemanagebuttonlocation(self, buttonname, offsetvalue):

	#	newbuttonlocation = Vector.createfromvalues(self.managedefenderoverlayposition.getx() + offsetvalue,
	#												self.managedefenderoverlayposition.gety() + 160)
	#	self.inputobject.setareadimensions(buttonname, newbuttonlocation,
	#																	self.inputobject.getareadimensions(buttonname))



	# ==========================================================================================
	# Get Information
	# ==========================================================================================



	# -------------------------------------------------------------------
	# Returns the hover state of the button
	# -------------------------------------------------------------------

	def getbuttonhoverstate(self, buttonname):

		if buttonname == self.inputobject.getcurrentmousearea():
			outcome = True
		else:
			outcome = False

		return outcome



	# -------------------------------------------------------------------
	# Returns the set of buttons in a group
	# -------------------------------------------------------------------

	def getbuttoncollection(self, groupname):

		return self.inputobject.getbuttoncollection(groupname)



	# -------------------------------------------------------------------
	# Returns the button's state
	# -------------------------------------------------------------------

	def getbuttonstate(self, buttonname):

		return self.inputobject.getareastate(buttonname)



	# -------------------------------------------------------------------
	# Returns the button's position
	# -------------------------------------------------------------------

	def getbuttonposition(self, buttonname):
		return self.inputobject.getareaposition(buttonname)



	# -------------------------------------------------------------------
	# Returns the button's size
	# -------------------------------------------------------------------

	def getbuttonsize(self, buttonname):

		return self.inputobject.getareadimensions(buttonname)



