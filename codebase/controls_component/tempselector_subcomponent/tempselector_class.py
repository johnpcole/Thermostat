from ...common_components.vector_datatype import vector_module as Vector
from ...common_components.enumeration_datatype import enumeration_module as Enumeration


class DefineSelector():

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================


	def __init__(self):

		# Specifies whether the temp slider is being dragged
		self.sliderstate = False

		# Specifies the temp slider position
		self.slidervalue = -999

		# Specifies which override button is currently selected
		self.selectedtime = Enumeration.createenum(["Next", "30", "60", "120", "180", "Lock"], "Next")

		# Specifies the minimum and maximum values
		self.minimum = 300
		self.maximum = 2700

		# Specifies the slider granularity / speed
		self.speed = 5


	# ==========================================================================================
	# Perform Actions
	# ==========================================================================================


	# -------------------------------------------------------------------
	# Updates the override time selection buttons on the main menu
	# -------------------------------------------------------------------

	def updateoverrideselection(self, selecteditem):

		self.selectedtime.set(selecteditem)



	# -------------------------------------------------------------------
	# Updates the slider on the main menu
	# -------------------------------------------------------------------

	def updateslider(self, mode, mousepositionchange, newmousearea):

		if mode == "Click: Temp Slider":
			self.sliderstate = True
		elif mode == "Release: Temp Slider":
			self.sliderstate = False

		if self.sliderstate == True:
			if newmousearea == "Temp Slider":
				sliderchange = mousepositionchange.getx() * self.speed
				self.slidervalue = min(self.maximum, max(self.minimum, self.slidervalue + sliderchange))
			else:
				self.sliderstate = False



	# -------------------------------------------------------------------
	# Updates the slider on the main menu
	# -------------------------------------------------------------------

	def updatebuttonselection(self, selecteditem):

		self.selectedtime.set(selecteditem)



	# -------------------------------------------------------------------
	# Updates the slider on the main menu
	# -------------------------------------------------------------------

	def resetcontrols(self, currentdesiredtemperature):

		# Set the slider value to be the current boiler temperature
		self.slidervalue = currentdesiredtemperature * 100

		# Set the override to next button
		self.selectedtime.set("Next")


	# -------------------------------------------------------------------
	# Returns the current UNCOMMITTED desired temperature on the slider
	# -------------------------------------------------------------------

	def getslidervalue(self):

		return int(self.slidervalue / 100)



	# -------------------------------------------------------------------
	# Returns the current UNCOMMITTED desired time
	# -------------------------------------------------------------------

	def getselectedtime(self):

		return self.selectedtime.displaycurrent()
