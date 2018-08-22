from ....common_components.enumeration_datatype import enumeration_module as Enumeration


class DefineSelector():

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================


	def __init__(self):

		# Specifies whether the slider is being dragged
		self.sliderstate = Enumeration.createenum(["Hour", "Min", "Temp", "None"], "None")

		# Specifies the slider position
		self.slidervalue = {}
		self.slidervalue["Hour"] = -999
		self.slidervalue["Min"] = -999
		self.slidervalue["Temp"] = -999

		# Specifies the minimum and maximum values
		self.minimum = {}
		self.maximum = {}
		self.minimum["Hour"] = 0
		self.maximum["Hour"] = 2300
		self.minimum["Min"] = 0
		self.maximum["Min"] = 5900
		self.minimum["Temp"] = 300
		self.maximum["Temp"] = 2700

		# Specifies the slider granularity / speed
		self.speed = {}
		self.speed["Hour"] = 5
		self.speed["Min"] = 5
		self.speed["Temp"] = 5


	# ==========================================================================================
	# Perform Actions
	# ==========================================================================================



	# -------------------------------------------------------------------
	# Updates the slider on the main menu
	# -------------------------------------------------------------------

	def updateslider(self, mode, mousepositionchange, newmousearea):

		modecheck = mode[:26]

		if modecheck == "Click: Instruction Slider ":
			self.sliderstate.set(mode[26:])
		elif modecheck == "Release: Instruction Slide":
			self.sliderstate.set("None")

		if self.sliderstate.get("None") == False:
			currentslider = self.sliderstate.displaycurrent()
			if newmousearea == "Instruction Slider " + currentslider:
				sliderchange = mousepositionchange.gety() * self.speed[currentslider]
				self.slidervalue[currentslider] = min(self.maximum[currentslider], max(self.minimum[currentslider], self.slidervalue[currentslider] + sliderchange))
			else:
				self.sliderstate.set("None")



	# -------------------------------------------------------------------
	# Updates the slider on the main menu
	# -------------------------------------------------------------------

	def resetcontrols(self, instructiontemperature, instructionclock):

		# Set the slider value to be the current boiler temperature
		self.slidervalue["Temp"] = instructiontemperature * 100
		self.slidervalue["Hour"] = instructionclock.gethour() * 100
		self.slidervalue["Min"] = instructionclock.getminute() * 100



	# -------------------------------------------------------------------
	# Returns the current UNCOMMITTED desired temperature on the slider
	# -------------------------------------------------------------------

	def getslidervalue(self, sliderselector):

		return int(self.slidervalue[sliderselector] / 100)
