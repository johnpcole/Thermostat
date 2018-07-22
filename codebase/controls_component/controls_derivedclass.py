from ..common_components.vector_datatype import vector_module as Vector
#from ..common_components.enumeration_datatype import enumeration_module as Enumeration
from . import buttons_baseclass as Buttons


class DefineController(Buttons.DefineButtons):

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================


	def __init__(self):

		# Get the input controller and configure buttons using baseclass method
		Buttons.DefineButtons.__init__(self)

		# Specifies whether the game should "run" - enemies walk and defenders walk/combat, in this cycle
		#self.runstate = True

		# Specifies whether the user has requested to close the application in this cycle
		self.quitstate = False

		# Game speed
		#self.gamefast = False

		# Specifies whether the game is "between waves" mode
		#self.betweenwavesmode = False

		# Initialise game
		#self.startnextlevel()

		# Hover overlay offset & size - For display purpose only
		#self.selectiondisplaysize = Vector.createfromvalues(64, 72)
		#self.selectiondisplayoffset = Vector.createfromvalues(-16, -40)

		# Granularised hover location of the mouse on the field
		#self.fieldhoverlocation = Vector.createblank()

		# Specifies what would happen if the user clicked at the current field hover location
		#self.fieldhovermode = Enumeration.createenum(["Disabled", "Add", "Upgrade", "Unknown"], "Disabled")

		# Specifies whether the temp slider is being dragged
		self.temperaturesliderstate = False
		self.temperatureslidervalue = -999

		# Mouse location
		self.mouselocation = Vector.createblank()

		# Specifies what the user has done this cycle
		self.useraction = "None"

		# Get buttons in the correct state
		self.quitmainmenu()


	# ==========================================================================================
	# Perform Actions
	# ==========================================================================================



	# -------------------------------------------------------------------
	# Interprets input events for this cycle, setting flags that will
	# be read and interpreted by other methods later in the same cycle
	# Returns number of coins to spend, for any costly actions performed
	# -------------------------------------------------------------------

	def processinput(self, boilercontroller):

		# Loop over all events logged in this cycle and update all mouse properties
		self.inputobject.processinputs()

		# Default to no user action being specified
		self.useraction = "None"

		if self.inputobject.getmouseaction() == True:

			self.updateslider("Position")

			clickedbutton = self.getmouseaction()

			if clickedbutton[-11:] == "Temp Slider":
				self.updateslider(clickedbutton)

			elif clickedbutton == "Release: Start Menu":
				self.showmainmenu(boilercontroller)

			elif clickedbutton == "Release: Temp Slider":
				self.updateslider("Release")

			elif clickedbutton == "Release: Temp Cancel":
				self.quitmainmenu()

			elif clickedbutton == "Release: Temp Commit":
				self.setdesiredtemp()



	# -------------------------------------------------------------------
	# Updates the slider on the main menu
	# -------------------------------------------------------------------

	def getmouseaction(self):

		outcome = ""
		if self.inputobject.getcurrentmouseareastate() == "Enabled":
			clickedbutton = self.inputobject.getcurrentmousearea()
			if self.inputobject.getmouseclickaction() == 1:
				outcome = "Click: " + clickedbutton
			elif self.inputobject.getmouseclickaction() == -1:
				outcome = "Release: " + clickedbutton
			else:
				outcome = "Hover: " + clickedbutton
		return outcome



	# -------------------------------------------------------------------
	# Updates the slider on the main menu
	# -------------------------------------------------------------------

	def updateslider(self, mode):

		if mode == "Click: Temp Slider":
			self.temperaturesliderstate = True
			self.mouselocation = self.inputobject.getmouselocation()
		elif mode == "Release: Temp Slider":
			self.temperaturesliderstate = False

		if self.temperaturesliderstate == True:
			if self.inputobject.getcurrentmousearea() == "Temp Slider":
				newmouse = self.inputobject.getmouselocation()
				sliderchange = (newmouse.getx() - self.mouselocation.getx()) * 5
				self.mouselocation = newmouse
				self.temperatureslidervalue = min(2700, max(300, self.temperatureslidervalue + sliderchange))
			else:
				self.temperaturesliderstate = False



	# -------------------------------------------------------------------
	# Shows the main menu
	# -------------------------------------------------------------------

	def showmainmenu(self, boilercontroller):

		# Set Start Menu to Hidden
		self.updatebutton("Start Menu", "Hidden")

		# Set main menu buttons to displayed and enabled
		self.updatebutton("Set Temp", "Enabled")

		# Set the slider value to be the current boiler temperature
		self.temperatureslidervalue = boilercontroller.getdesiredtemperature() * 100



	# -------------------------------------------------------------------
	# Quits the main menu
	# -------------------------------------------------------------------

	def quitmainmenu(self):

		# Set Start Menu to Enabled
		self.updatebutton("Start Menu", "Enabled")

		# Set main menu buttons to hidden
		self.updatebutton("Set Temp", "Hidden")



	# -------------------------------------------------------------------
	# Shows the configuration menu
	# -------------------------------------------------------------------

	#def showconfiguremenu(self):

		# Set main menu buttons to hidden
	#	self.updatebutton("Set Temp", "Hidden")
	#	self.quitmainmenu()

	#	print "Showing configuration menu"



	# -------------------------------------------------------------------
	# Sets the desired temperature
	# -------------------------------------------------------------------

	def setdesiredtemp(self):

		self.quitmainmenu()

		self.useraction = "Set Temp = " + str(int(self.temperatureslidervalue / 100))

		print self.useraction



	# -------------------------------------------------------------------
	# Update mouse position
	# -------------------------------------------------------------------

	def updatemouseposition(self):

		newlocation = Vector.createfromvector(self.inputobject.getmouselocation())
		positionchange = Vector.subtract(newlocation, self.mouselocation)
		self.mouselocation = Vector.createfromvector(newlocation)

		return positionchange

	# # -------------------------------------------------------------------
	# # Sets game to fast or slow or stop mode
	# # -------------------------------------------------------------------
	#
	# def setgamespeed(self, speedlabel):
	#
	# 	if speedlabel == "Stop":
	# 		self.runstate = False
	# 		self.updatebutton("Field", "Enabled")
	# 	elif speedlabel == "Disable":
	# 		self.updatebutton("Speed", "Disabled")
	# 	else:
	# 		self.runstate = True
	# 		self.updatebutton("Field", "Hidden")
	# 		if speedlabel == "Fast":
	# 			self.gamefast = True
	# 		else:
	# 			self.gamefast = False
	#
	# 	# Update Go/Stop button states
	# 	self.updatebutton("Speed - " + speedlabel, "Disabled")
	# 	self.updatebutton("Non-" + speedlabel, "Enabled")
	#
	#
	#
	# # -------------------------------------------------------------------
	# # When user has clicked field, determine whether it should be add
	# # or upgrade defender, and invoke the correct mode
	# # -------------------------------------------------------------------
	#
	# def invokemanagedefender(self, game, defenderarmy):
	#
	# 	if self.useraction.get("Click Field") == True:
	#
	# 		# If it's possible to add a defender, put the game into add defender mode
	# 		if (self.fieldhovermode.get("Add") == True) or (self.fieldhovermode.get("Upgrade") == True):
	#
	# 			# Disable play
	# 			self.setgamespeed("Disable")
	#
	# 			# Disable Field selection
	# 			self.updatebutton("Field", "Hidden")
	#
	# 			# Update manage defender button states
	# 			self.updatemanagedefenderbuttons(self.fieldhovermode.displaycurrent(), game, defenderarmy)
	#
	#
	#
	#
	#
	# # -------------------------------------------------------------------
	# # Sets the game to "between waves" mode, and pauses the game
	# # -------------------------------------------------------------------
	#
	# def startnextlevel(self):
	#
	# 	# Stop the game (moving enemies and defenders)
	# 	self.runstate = False
	#
	# 	# Start inbetween wave mode
	# 	self.betweenwavesmode = True
	#
	# 	# Disable play
	# 	self.setgamespeed("Disable")
	#
	# 	# Update button states
	# 	self.updatebutton("Start Wave", "Enabled")
	#
	#
	#
	# # -------------------------------------------------------------------
	# # Exits "between waves" mode
	# # -------------------------------------------------------------------
	#
	# def playnextlevel(self):
	#
	# 	# Finish inbetween wave mode
	# 	self.betweenwavesmode = False
	#
	# 	# Update button states and game run mode
	# 	self.setgamespeed("Stop")
	#
	# 	# Update button states
	# 	self.updatebutton("Start Wave", "Hidden")
	#
	#
	#
	# # -------------------------------------------------------------------
	# # Returns whether the field selection should be updated
	# # on the field and defender objects
	# # -------------------------------------------------------------------
	#
	# def updatefieldselectionlocation(self, field):
	#
	# 	# If the field is enabled
	# 	if self.inputobject.getareastate("Field") == "Enabled":
	# 		outcome = True
	#
	# 		# If mouse is in field area, set fieldblocklocation to be granularised pixel location
	# 		if self.inputobject.getcurrentmousearea() == "Field":
	# 			self.fieldhoverlocation = field.calculatefieldselectionlocation(self.inputobject.getmouselocation())
	# 			self.updatemanagedefenderoverlaylocation(field.calculatefieldselectionquadrant(self.fieldhoverlocation))
	#
	# 		# If mouse is outside field area, set fieldhoverlocation to be dummy off field location
	# 		else:
	# 			self.fieldhoverlocation = Vector.createblank()
	#
	# 	else:
	# 		outcome = False
	#
	# 	return outcome
	#
	#
	#
	# # -------------------------------------------------------------------
	# # When user is hovering on the field, determine whether
	# # the hover should be add or upgrade defender
	# # -------------------------------------------------------------------
	#
	# def updatefieldselectionmode(self, field, defenderarmy):
	#
	# 	# If it's possible to add a defender
	# 	if field.isselectionvalidtoadddefender() == True:
	# 		self.fieldhovermode.set("Add")
	#
	# 	# If the current selection properly overlaps an existing defender
	# 	elif defenderarmy.getselecteddefender() is not None:
	# 		self.fieldhovermode.set("Upgrade")
	#
	# 	# None mode
	# 	else:
	# 		self.fieldhovermode.set("Disabled")
	#
	#
	#
	# # ==========================================================================================
	# # Get Information
	# # ==========================================================================================
	#
	#
	#
	# # -------------------------------------------------------------------
	# # Returns the pixel co-ordinates of the cursor within the field
	# # -------------------------------------------------------------------
	#
	# def getfieldselectionlocation(self):
	#
	# 	return self.fieldhoverlocation
	#
	#
	#
	# # -------------------------------------------------------------------
	# # Returns the game speed
	# # -------------------------------------------------------------------
	#
	# def getdisplayallframes(self):
	#
	# 	# Display all frames if the game is set to SLOW or the game is paused
	# 	if (self.gamefast == False) or (self.runstate == False):
	# 		outcome = True
	#
	# 	# Display only some frames if the game is set to FAST and the game is not paused
	# 	else:
	# 		outcome = False
	#
	# 	# Returns whether to display all frames or not
	# 	return outcome
	#
	#
	#
	# # -------------------------------------------------------------------
	# # Returns whether the wave should run (i.e. actors should animate)
	# # -------------------------------------------------------------------
	#
	# def getprocesswavestate(self):
	#
	# 	return self.runstate
	#
	#
	#
	# # -------------------------------------------------------------------
	# # Returns whether the game is between waves
	# # -------------------------------------------------------------------
	#
	# def getbetweenwavestate(self):
	#
	# 	return self.betweenwavesmode
	#
	#
	#
	# # -------------------------------------------------------------------
	# # Returns whether the user has requested to add or upgrade a defender
	# # -------------------------------------------------------------------
	#
	# def getmanagedefenderaction(self):
	#
	# 	return self.useraction.displaycurrent()
	#
	#
	#
	# # -------------------------------------------------------------------
	# # Returns whether the field hover overlay should be
	# # Add, Upgrade or Disabled (or None)
	# # -------------------------------------------------------------------
	#
	# def getfieldselectionoverlay(self):
	#
	# 	if self.fieldhoverlocation.getx() > -1:
	# 		outcome = self.fieldhovermode.displaycurrent()
	# 	else:
	# 		outcome = ""
	#
	# 	return outcome
	#
	#
	#
	# # -------------------------------------------------------------------
	# # Return field selection display location
	# # -------------------------------------------------------------------
	#
	# def getselectiondisplaylocation(self):
	# 	# Offset the pixel location to ensure the ground is in the right place
	# 	return Vector.add(self.fieldhoverlocation, self.selectiondisplayoffset)
	#
	#
	#
	# # -------------------------------------------------------------------
	# # Return field selection display size
	# # -------------------------------------------------------------------
	#
	# def getselectiondisplaysize(self):
	# 	# pixel size of display image, for erase purposes
	# 	return self.selectiondisplaysize



	# -------------------------------------------------------------------
	# Returns whether the user has requested the application to end
	# -------------------------------------------------------------------

	def getquitstate(self):

		return self.inputobject.getquitstate()


	# -------------------------------------------------------------------
	# Returns the current UNCOMMITTED desired temperature on the slider
	# -------------------------------------------------------------------

	def getslidervalue(self):

		return int(self.temperatureslidervalue / 100)
