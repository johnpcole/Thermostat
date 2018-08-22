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

		# Main Screen Areas
		self.definebutton("Start Menu",           0,   0, 480, 320, [])

		# Start Menu Areas
		self.definebutton("Temp Slider",         24,  24, 432,  80, ["Set Temp"])
		self.definebutton("Override Next",       24, 150,  50,  50, ["Set Temp"])
		self.definebutton("Override 30",        106, 150,  50,  50, ["Set Temp"])
		self.definebutton("Override 60",        179, 150,  50,  50, ["Set Temp"])
		self.definebutton("Override 120",       251, 150,  50,  50, ["Set Temp"])
		self.definebutton("Override 180",       324, 150,  50,  50, ["Set Temp"])
		self.definebutton("Override Lock",      406, 150,  50,  50, ["Set Temp"])
		self.definebutton("Configure Schedule",  24, 246,  50,  50, ["Set Temp"])
		self.definebutton("Temp Cancel",        333, 246,  50,  50, ["Set Temp"])
		self.definebutton("Temp Commit",        406, 246,  50,  50, ["Set Temp"])

		# Configuration Menu Areas
		self.definebutton("Timeline Slider",     24,  24, 432,  80, ["Schedule Config", "Schedule Group"])
		self.definebutton("Schedule Select A",   24, 130, 100,  80, ["Schedule 3", "Schedule Reset", "Schedule Group"])
		self.definebutton("Schedule Select B",  190, 130, 100,  80, ["Schedule 3", "Schedule Reset", "Schedule Group"])
		self.definebutton("Schedule Select C",  356, 130, 100,  80, ["Schedule 3", "Schedule Reset", "Schedule Group"])
		self.definebutton("Schedule Select D",  107, 130, 100,  80, ["Schedule 2", "Schedule Reset", "Schedule Group"])
		self.definebutton("Schedule Select E",  273, 130, 100,  80, ["Schedule 2", "Schedule Reset", "Schedule Group"])
		self.definebutton("Schedule Select F",  190, 130, 100,  80, ["Schedule 1", "Schedule Reset", "Schedule Group"])

		self.definebutton("Add Instruction",    403, 246,  50,  50, ["Schedule Config", "Schedule Group"])
		#self.definebutton("Delete Instruction", 406, 150,  50,  50, ["Schedule Config", "Schedule Group"])
		self.definebutton("Exit",               333, 246,  50,  50, ["Schedule Config", "Schedule Group"])

		# Configure Instruction Areas
		self.definebutton("Instruction Slider Hour",     24,  24, 80,  280, ["Instruction Config"])
		self.definebutton("Instruction Slider Min",      124,  24, 80,  280, ["Instruction Config"])
		self.definebutton("Instruction Slider Temp",     224,  24, 80,  280, ["Instruction Config"])






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



