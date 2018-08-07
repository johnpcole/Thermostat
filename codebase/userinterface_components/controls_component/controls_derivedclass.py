from ...common_components.vector_datatype import vector_module as Vector
from ...common_components.enumeration_datatype import enumeration_module as Enumeration
from . import buttons_baseclass as Buttons
from tempselector_subcomponent import tempselector_module as TempSelector


class DefineController(Buttons.DefineButtons):

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================


	def __init__(self):

		# Get the input controller and configure buttons using baseclass method
		Buttons.DefineButtons.__init__(self)

		# Specifies whether the user has requested to close the application in this cycle
		self.quitstate = False

		# Temperature Selector (Slider and option buttons combination)
		self.temperatureselector = TempSelector.createselector()

		# Mouse location
		self.mouselocation = Vector.createblank()

		# Specifies what the user has done this cycle
		self.useraction = Enumeration.createenum(["None", "Override Temperature"], "None")

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
		self.useraction.set("None")

		if self.inputobject.getmouseaction() == True:

			clickedbutton = self.getdetailedmouseaction()

			mousechange = self.updatemouseposition()

			self.temperatureselector.updateslider(clickedbutton, mousechange, self.inputobject.getcurrentmousearea())

			if clickedbutton == "Release: Start Menu":
				self.showmainmenu(currentdesiredtemperature)

			elif clickedbutton[:17] == "Release: Override":
				self.temperatureselector.updatebuttonselection(clickedbutton[18:])

			elif clickedbutton == "Release: Temp Cancel":
				self.quitmainmenu()

			elif clickedbutton == "Release: Temp Commit":
				self.setdesiredtemp()

		return self.useraction


	# -------------------------------------------------------------------
	# Updates the slider on the main menu
	# -------------------------------------------------------------------

	def getdetailedmouseaction(self):

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
	# Shows the main menu
	# -------------------------------------------------------------------

	def showmainmenu(self, currentdesiredtemperature):

		# Set Start Menu to Hidden
		self.updatebutton("Start Menu", "Hidden")

		# Set main menu buttons to displayed and enabled
		self.updatebutton("Set Temp", "Enabled")

		# Set the slider value to be the current boiler temperature
		self.temperatureselector.resetcontrols(currentdesiredtemperature)



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

		self.useraction.set("Override Temperature")



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

	def gettempselectordata(self):

		return self.temperatureselector


	# -------------------------------------------------------------------
	# Returns the current UNCOMMITTED desired temperature on the slider
	# -------------------------------------------------------------------

	def getuseraction(self):

		return self.useraction
