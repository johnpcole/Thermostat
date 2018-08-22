from ...common_components.vector_datatype import vector_module as Vector
from ...common_components.enumeration_datatype import enumeration_module as Enumeration
from . import buttons_baseclass as Buttons
from tempselector_subcomponent import tempselector_module as TempSelector
from scheduleselector_subcomponent import scheduleselector_module as ScheduleSelector
from instructionselector_subcomponent import instructionselector_module as InstructionSelector



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

		# Timeline Selector (Slider)
		self.timelineselector = ScheduleSelector.createselector()

		# Instruction Selector (Slider)
		self.instructionselector = InstructionSelector.createselector()

		# Mouse location
		self.mouselocation = Vector.createblank()

		# Specifies what the user has done this cycle
		self.useraction = Enumeration.createenum(["None", "Override Temperature"], "None")

		# Get buttons in the correct state
		self.showamenu("Configure") #"Quit"


	# ==========================================================================================
	# Perform Actions
	# ==========================================================================================



	# -------------------------------------------------------------------
	# Interprets input events for this cycle, setting flags that will
	# be read and interpreted by other methods later in the same cycle
	# Returns number of coins to spend, for any costly actions performed
	# -------------------------------------------------------------------

	def processinput(self, currentdesiredtemperature, schedule):

		# Loop over all events logged in this cycle and update all mouse properties
		self.inputobject.processinputs()

		# Default to no user action being specified
		self.useraction.set("None")

		if self.inputobject.getmouseaction() == True:

			clickedbutton = self.getdetailedmouseaction()

			mousechange = self.updatemouseposition()

			self.temperatureselector.updateslider(clickedbutton, mousechange, self.inputobject.getcurrentmousearea())

			self.timelineselector.updateslider(clickedbutton, mousechange, self.inputobject.getcurrentmousearea())

			self.instructionselector.updateslider(clickedbutton, mousechange, self.inputobject.getcurrentmousearea())

			self.updateconfiguremenu(schedule)

			if clickedbutton == "Release: Start Menu":
				self.showamenu("Main")
				self.temperatureselector.resetcontrols(currentdesiredtemperature)

			elif clickedbutton == "Release: Configure Schedule":
				self.showamenu("Configure")
				self.timelineselector.resetcontrols()

			elif clickedbutton[:17] == "Release: Override":
				self.temperatureselector.updatebuttonselection(clickedbutton[18:])

			elif (clickedbutton == "Release: Temp Cancel") or (clickedbutton == "Release: Exit"):
				self.showamenu("Quit")

			elif clickedbutton == "Release: Temp Commit":
				self.showamenu("Quit")
				self.useraction.set("Override Temperature")

			elif clickedbutton[:25] == "Release: Schedule Select ":
				self.selectaninstruction(clickedbutton[25:])

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
	# Shows the desired menu
	# -------------------------------------------------------------------

	def showamenu(self, menuselector):

		# Set Start Menu
		if menuselector == "Quit":
			self.updatebutton("Start Menu", "Enabled")
		else:
			self.updatebutton("Start Menu", "Hidden")

		# Set Configuration Menu
		if menuselector == "Configure":
			self.updatebutton("Schedule Config", "Enabled")
		else:
			self.updatebutton("Schedule Group", "Hidden")

		# Set main menu buttons
		if menuselector == "Main":
			self.updatebutton("Set Temp", "Enabled")
		else:
			self.updatebutton("Set Temp", "Hidden")

		# Set instruction setting buttons
		if menuselector == "Instruction":
			self.updatebutton("Instruction Config", "Enabled")
		else:
			self.updatebutton("Instruction Config", "Hidden")



	# -------------------------------------------------------------------
	# Updates the configuration menu
	# -------------------------------------------------------------------

	def updateconfiguremenu(self, schedule):

		if self.getbuttonstate("Timeline Slider") == "Enabled":

			self.updatebutton("Schedule Reset", "Hidden")

			buttoncount = self.timelineselector.updatebuttonmeanings(schedule)

			if buttoncount == 1:
				self.updatebutton("Schedule 1", "Enabled")
			elif buttoncount == 2:
				self.updatebutton("Schedule 2", "Enabled")
			elif buttoncount > 2:
				self.updatebutton("Schedule 3", "Enabled")



	# -------------------------------------------------------------------
	# Sets up the instruction menu
	# -------------------------------------------------------------------

	def selectaninstruction(self, clickedbuttonletter):

		instructiontime, instructiontemp = self.timelineselector.getbuttonmeaningbylabel(clickedbuttonletter)
		print clickedbuttonletter, instructiontime.gettext(), instructiontemp
		self.showamenu("Instruction")
		self.instructionselector.resetcontrols(instructiontemp, instructiontime)



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
	# Returns the current UNCOMMITTED desired schedule time on the slider
	# -------------------------------------------------------------------

	def gettimelineselectordata(self):

		return self.timelineselector



	# -------------------------------------------------------------------
	# Returns the latest user action
	# -------------------------------------------------------------------

	def getuseraction(self):

		return self.useraction

