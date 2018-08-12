

class DefineSelector():

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================


	def __init__(self):

		# Specifies whether the temp slider is being dragged
		self.sliderstate = False

		# Specifies the temp slider position
		self.slidervalue = -999

		# Specifies the minimum and maximum values
		self.minimum = 0
		self.maximum = ((24 * 60) - 1) * 60

		# Specifies the slider granularity / speed
		self.speed = 60 * 3


	# ==========================================================================================
	# Perform Actions
	# ==========================================================================================



	# -------------------------------------------------------------------
	# Updates the slider on the configure menu
	# -------------------------------------------------------------------

	def updateslider(self, mode, mousepositionchange, newmousearea):

		if mode == "Click: Timeline Slider":
			self.sliderstate = True
		elif mode == "Release: Timeline Slider":
			self.sliderstate = False

		if self.sliderstate == True:
			if newmousearea == "Timeline Slider":
				sliderchange = mousepositionchange.getx() * self.speed
				self.slidervalue = min(self.maximum, max(self.minimum, self.slidervalue + sliderchange))
			else:
				self.sliderstate = False



	# -------------------------------------------------------------------
	# Updates the slider on the main menu
	# -------------------------------------------------------------------

	def resetcontrols(self):

		# Set the slider value to be the current time
		self.slidervalue = 12 * 60 * 60



	# -------------------------------------------------------------------
	# Returns the current UNCOMMITTED desired time on the slider
	# -------------------------------------------------------------------

	def getslidervalue(self):

		return (60 * int(self.slidervalue / 60))


