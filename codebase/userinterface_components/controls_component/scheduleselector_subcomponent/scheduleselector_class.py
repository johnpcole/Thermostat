from schedulebutton_subcomponent import schedulebutton_module as ScheduleButton


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

		# Specifies the scheduled instructions for the three buttons
		self.buttonmeaning = {}
		self.buttonmeaning[1] = ScheduleButton.createbutton()
		self.buttonmeaning[2] = ScheduleButton.createbutton()
		self.buttonmeaning[3] = ScheduleButton.createbutton()
		self.buttoncount = 0



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
	# Updates the slider buttons on the configure menu
	# -------------------------------------------------------------------

	def updatebuttonmeanings(self, schedule):

		selectedhour = self.getsliderhourvalue()
		rangemin = selectedhour * 3600
		rangemax = rangemin + 3600

		buttoncount = 0
		for time in schedule.getscheduledtimes():
			timevalue = time.getvalue()
			if (timevalue >= rangemin) and (timevalue < rangemax):
				buttoncount = buttoncount + 1
				if buttoncount < 4:
					self.buttonmeaning[buttoncount].updatebutton(time, schedule.getscheduledinstruction(time))

		self.buttoncount = buttoncount
		return buttoncount



	# -------------------------------------------------------------------
	# Updates the slider on the main menu
	# -------------------------------------------------------------------

	def resetcontrols(self, resetmode):

		# Set the slider value to be the current time
		if resetmode == False:
			self.slidervalue = 12 * 60 * 60
		self.buttoncount = 0



	# -------------------------------------------------------------------
	# Returns the current UNCOMMITTED desired time on the slider
	# -------------------------------------------------------------------

	def getsliderhourvalue(self):

		return int(self.slidervalue / 3600)



	# -------------------------------------------------------------------
	# Returns the number of buttons
	# -------------------------------------------------------------------

	def getbuttoncount(self):

		return self.buttoncount



	# -------------------------------------------------------------------
	# Returns the current button definition
	# -------------------------------------------------------------------

	def getbuttonmeaning(self, buttonindex):

		return self.buttonmeaning[buttonindex].gettime(), self.buttonmeaning[buttonindex].gettemp()



	# -------------------------------------------------------------------
	# Returns the current button definition based on button label
	# -------------------------------------------------------------------

	def getbuttonmeaningbylabel(self, buttonlabel):

		if (buttonlabel == "A") or (buttonlabel == "D") or (buttonlabel == "F"):
			buttonmapping = 1
		elif (buttonlabel == "B") or (buttonlabel == "E"):
			buttonmapping = 2
		else:
			buttonmapping = 3

		return self.getbuttonmeaning(buttonmapping)
