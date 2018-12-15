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
		self.useraction = Enumeration.createenum(["None", "Override Temperature", "Delete Instruction", "Modify Instruction"], "None")

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

			registeredaction = self.getdetailedmouseaction()

			mousechange = self.updatemouseposition()

			self.temperatureselector.updateslider(registeredaction, mousechange, self.inputobject.getcurrentmousearea())

			self.timelineselector.updateslider(registeredaction, mousechange, self.inputobject.getcurrentmousearea())

			self.instructionselector.updateslider(registeredaction, mousechange, self.inputobject.getcurrentmousearea())

			if registeredaction[:9] == "Release: ":
				clickedbutton = registeredaction[9:]

				if clickedbutton == "Start Menu":
					self.showamenu("Main")
					self.temperatureselector.resetcontrols(currentdesiredtemperature)

				elif (clickedbutton == "Configure Schedule") or (clickedbutton == "Instruction Cancel"):
					self.showamenu("Configure")
					if clickedbutton == "Configure Schedule":
						resetmode = False
					else:
						resetmode = True
					self.timelineselector.resetcontrols(resetmode)

				elif clickedbutton[:8] == "Override":
					self.temperatureselector.updatebuttonselection(clickedbutton[9:])

				elif clickedbutton == "Instruction Delete":
					self.useraction.set("Delete Instruction")
					self.showamenu("Configure")
					self.timelineselector.resetcontrols(True)

				elif clickedbutton == "Instruction Commit":
					self.useraction.set("Modify Instruction")
					self.showamenu("Configure")
					self.timelineselector.resetcontrols(True)

				elif (clickedbutton == "Temp Cancel") or (clickedbutton == "Exit"):
					self.showamenu("Quit")

				elif clickedbutton == "Temp Commit":
					self.showamenu("Quit")
					self.useraction.set("Override Temperature")

				elif clickedbutton[:16] == "Schedule Select ":
					self.selectaninstruction(clickedbutton[16:])

			self.updateconfiguremenu(schedule)

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
		self.showamenu("Instruction")
		self.instructionselector.resetcontrols(instructiontemp, instructiontime)



	# -------------------------------------------------------------------
	# Performs action on selected instruction
	# -------------------------------------------------------------------

	def modifyaninstruction(self, modifymode):

		updatedinstruction = self.instructionselector.getcurrentinstructiontime()


		instructiontime, instructiontemp = self.timelineselector.getbuttonmeaningbylabel(clickedbuttonletter)
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
	# Returns the current UNCOMMITTED desired schedule time on the slider
	# -------------------------------------------------------------------

	def getinstructionselectordata(self):

		return self.instructionselector



	# -------------------------------------------------------------------
	# Returns the latest user action
	# -------------------------------------------------------------------

	def getuseraction(self):

		return self.useraction

