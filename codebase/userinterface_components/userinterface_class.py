from maindisplay_component import maindisplay_module as Display
from displayrunway_component import displayrunway_module as DisplayRunway
from displayboard_component import displayboard_module as DisplayBoard
from displaybuttons_component import displaybuttons_module as DisplayButtons
from controls_component import controls_module as Controller



class DefineUserInterface:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		# The object which processes user input (mouse)
		self.controls = Controller.createcontroller()

		# The object which renders the screen
		self.maindisplay = Display.createdisplay(self.controls)

		# The object which prepares the runway part of the screen
		self.displayrunway = DisplayRunway.createrunway()

		# The object which prepares the board part of the screen
		self.displayboard = DisplayBoard.createboard()

		# The object which prepares the buttons part of the screen
		self.displaybuttons = DisplayButtons.createbuttons(self.controls)



	# =========================================================================================

	# -------------------------------------------------------------------
	# Processes inputs
	# -------------------------------------------------------------------

	def processinputs(self, boilercontroller):

		return self.controls.processinput(boilercontroller.getcurrentdesiredtemperature(), boilercontroller.getschedule())


	# -------------------------------------------------------------------
	# Refreshes the screen
	# -------------------------------------------------------------------

	def refreshscreen(self, boilercontroller, currenttimeobject, astrodata):

		# Display the runway
		self.maindisplay.paintitems(self.displayrunway.buildrunway(boilercontroller, currenttimeobject.getaccurateclock(), self.maindisplay, astrodata))

		# Display the board
		self.maindisplay.paintitems(self.displayboard.buildboard(boilercontroller))

		# Display the buttons
		self.maindisplay.paintitems(self.displaybuttons.buildbuttons(boilercontroller, self.controls))

		# Flip the screen
		self.maindisplay.refreshscreen()



	# -------------------------------------------------------------------
	# Returns the quitstate of the application
	# -------------------------------------------------------------------

	def getquitstate(self):

		return self.controls.getquitstate()



	# -------------------------------------------------------------------
	# Manually overrides the desired temperature
	# -------------------------------------------------------------------

	def getoverridetemperatureinstruction(self):

		return self.controls.gettempselectordata()

