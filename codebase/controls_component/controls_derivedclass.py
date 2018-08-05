from ..common_components.vector_datatype import vector_module as Vector
from . import buttons_baseclass as Buttons


class DefineController(Buttons.DefineButtons):

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================


	def __init__(self):

		# Get the input controller and configure buttons using baseclass method
		Buttons.DefineButtons.__init__(self)

		# Specifies whether the user has requested to close the application in this cycle
		self.quitstate = False

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

	def processinput(self, currentdesiredtemperature):

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
				self.showmainmenu(currentdesiredtemperature)

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

	def showmainmenu(self, currentdesiredtemperature):

		# Set Start Menu to Hidden
		self.updatebutton("Start Menu", "Hidden")

		# Set main menu buttons to displayed and enabled
		self.updatebutton("Set Temp", "Enabled")

		# Set the slider value to be the current boiler temperature
		self.temperatureslidervalue = currentdesiredtemperature * 100



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
