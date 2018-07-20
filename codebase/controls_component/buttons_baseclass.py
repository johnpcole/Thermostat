from ..common_components.appinput_framework import appinput_module as AppInput
from ..common_components.vector_datatype import vector_module as Vector



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

		# Manage Defender Overlay position
		#self.managedefenderoverlayposition = Vector.createblank()



	def setupbuttons(self):

		self.definebutton("Start Menu",          0, 0, 480, 320, [])

		for x in range(0, 5):
			for y in range(0, 4):
				if y == 0:
					buttonvalue = "Set Temp " + str(4 + (x * 2))
				else:
					buttonvalue = "Set Temp " + str(8 + (y * 5) + x)
				self.definebutton(buttonvalue,
									65 + (x * 60) + (y * 20),
									30 + (y * 70),
									50, 50, ["Set Temp"])

		#for x in range(0, 6):
		#	for y in range(0, 4):
		#		buttonvalue = "Set Temp " + str(3 + (y * 6) + x)
		#		self.definebutton(buttonvalue,
		#							35 + (x * 60) + (y * 20),
		#							30 + (y * 70),
		#							50, 50, ["Set Temp"])

		self.definebutton("Home",          415, 15, 50, 50, ["Set Temp"])
		self.definebutton("Configure",     15, 255, 50, 50, ["Set Temp"])





	def definebutton(self, buttonname, along, down, width, height, groupmembership):

		self.inputobject.createarea(buttonname, Vector.createfromvalues(along, down),
															Vector.createfromvalues(width, height), groupmembership)





	# ==========================================================================================
	# Perform Actions
	# ==========================================================================================



	# -------------------------------------------------------------------
	# Update Manage Defender Overlay fauxbutton
	# -------------------------------------------------------------------

	# def updatemanagedefenderoverlaylocation(self, newlocation):
	#
	# 	self.managedefenderoverlayposition.setfromvector(newlocation)
	#
	#
	#
	# # -------------------------------------------------------------------
	# # Update Add/Upgrade/Cancel buttons
	# # -------------------------------------------------------------------
	#
	# def updatemanagedefenderbuttons(self, managemode, game, defenderarmy):
	#
	# 	if managemode == "Add":
	# 		buttonlist = ["Soldier", "Archer", "Wizard", "Cancel"]
	# 	elif managemode == "Upgrade":
	# 		buttonlist = ["Upgrade", "Cancel"]
	# 	else:
	# 		buttonlist = ["Cancel"]
	# 		assert managemode == "Upgrade", "Unrecognised field-hover-mode"
	#
	# 	buttonoffset = -30
	#
	# 	for buttontype in buttonlist:
	#
	# 		if buttontype == "Cancel":
	# 			buttonname = buttontype
	# 			buttoncost = -999
	# 		elif buttontype == "Upgrade":
	# 			buttonname = "Upgrade Defender"
	# 			buttoncost = defenderarmy.getdefenderupgradecost()
	# 		else:
	# 			buttonname = "Add - " + buttontype
	# 			buttoncost = defenderarmy.getnewdefendercost(buttontype)
	#
	# 		buttonoffset = buttonoffset + 40
	# 		self.updatemanagebuttonlocation(buttonname, buttonoffset)
	#
	# 		if buttoncost > game.getcoincount():
	# 			newstate = "Disabled"
	# 		else:
	# 			newstate = "Enabled"
	# 		self.inputobject.setareastate(buttonname, newstate)
	#


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



	# # -------------------------------------------------------------------
	# # Returns the manage defender overlay position
	# # -------------------------------------------------------------------
	#
	# def getmanagedefenderoverlayposition(self):
	#
	# 	return self.managedefenderoverlayposition
	#
