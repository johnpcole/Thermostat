from ...common_components.vector_datatype import vector_module as Vector



class DefineButtonMetrics:

	def __init__(self):

		# Buttons

		self.textoffset = Vector.createfromvalues(25, 5)

		self.filloffset = Vector.createfromvalues(1, 1)

		self.fillresize = Vector.createfromvalues(-2, -2)

		self.slideroutlineoffset = Vector.createfromvalues(-1, -1)
		self.sliderendreduction = Vector.createfromvalues(-1, 0)
		self.sliderendshift = Vector.createfromvalues(1, 0)

		# Temperature Slider

		self.tempsliderposition = Vector.createfromvalues(40, 25)

		self.tempslidersize = Vector.createfromvalues(400, 78)

		self.tempsliderstepsize = Vector.createfromvalues(self.tempslidersize.getx() / 25, 0)
		self.tempslidertextoffset = Vector.createfromvalues(0, 19)

		self.tempslidercurrenttextoffset = Vector.createfromvalues(0, 33)

		self.origin = Vector.createfromvalues(0, 0)

		# Timeline Slider

		self.timesliderposition = Vector.createfromvalues(24, 24)

		self.timeslidersize = Vector.createfromvalues(432, 80)

		self.timeslidernormstepsize = Vector.createfromvalues(16, 0)
		self.timesliderzoomstepsize = Vector.createfromvalues(40, 0)


		# Timeline Slider - Timings

		self.timesliderhourlineheight = Vector.createfromvalues(0, 15)
		self.timesliderzoomlineheight = Vector.createfromvalues(0, 30)
		self.timeslidermarkeroffset = Vector.createfromvalues(5, 6)
		self.timesliderzoommarkeroffset = Vector.createfromvalues(5, 3)

		self.timesliderhourtextoffset = Vector.createfromvalues(2, 1)
		self.timesliderzoomtextoffset = Vector.createfromvalues(2, 5)

		self.timeslidermajorsubmarkheight = Vector.createfromvalues(0, 4)
		self.timesliderminorsubmarkheight = Vector.createfromvalues(0, 2)

		# Timeline Slider - Temperatures

		self.timeslidertempmarkeroffset = Vector.createfromvalues(5, 24)
		self.timeslidertempmarkeroneheight = Vector.createfromvalues(0, 10)
		self.timeslidertempmarkertwoheight = Vector.createfromvalues(0, 30)

		self.tempslidertemptextoffset = Vector.createfromvalues(0, 19)


	def calctimeslidertimemetrics(self, hourindex, subindex, sliderhour):

		sliderminutes = sliderhour * 60
		instructionminutes = (hourindex * 60) + (subindex * 15)

		boxposition = Vector.add(self.timesliderposition, self.calctimeslideroffset(instructionminutes, sliderminutes))
		fontsize = "Snooze"
		textoffset = self.timesliderhourtextoffset
		lineheight = self.timesliderhourlineheight
		lineoffset = self.timeslidermarkeroffset
		colour = "Grey"
		if (hourindex == sliderhour) or (hourindex == sliderhour + 1):
			fontsize = "Timeline Hours"
			textoffset = self.timesliderzoomtextoffset
			lineheight = self.timesliderzoomlineheight
			colour = "White"
			lineoffset = self.timesliderzoommarkeroffset
		else:
			if hourindex == 24:
				fontsize = "Hide"
		if subindex != 0:
			fontsize = "Hide"
			if (subindex % 2) == 0:
				lineheight = self.timeslidermajorsubmarkheight
			else:
				lineheight = self.timesliderminorsubmarkheight

		markertop = Vector.add(boxposition, lineoffset)
		markerbottom = Vector.add(markertop, lineheight)
		sanitisedhour = hourindex % 12
		if sanitisedhour == 0:
			sanitisedhour = 12
		hourlabelposition = Vector.add(markertop, textoffset)

		return markertop, markerbottom, hourlabelposition, str(sanitisedhour), str(instructionminutes), fontsize, colour



	def calctimeslidertempmetrics(self, instructiontime, instructiontemp, sliderhour):

		sliderminutes = 60 * sliderhour
		instructionminutes = int(instructiontime / 60)

		boxposition = Vector.add(self.timesliderposition, self.calctimeslideroffset(instructionminutes, sliderminutes))

		marker1top = Vector.add(boxposition, self.timeslidertempmarkeroffset)
		marker1bottom = Vector.add(marker1top, self.timeslidertempmarkeroneheight)
		marker2top = marker1bottom
		marker2bottom = Vector.add(marker2top, self.timeslidertempmarkertwoheight)

		labelposition = Vector.createorigin()
		templabel = str(instructiontemp)
		indexer = str(instructiontime)
		fontsize = "Snooze"
		colour = "Grey"

		return marker1top, marker2bottom, labelposition, templabel, indexer, fontsize, colour



	def calculatemarkrange(self, hourindex, sliderhourvalue):

		if hourindex == sliderhourvalue:
			if hourindex == 0:
				minval = 0
			else:
				minval = -1
			maxval = 4
		elif hourindex == sliderhourvalue + 1:
			minval = 0
			if hourindex == 24:
				maxval = 1
			else:
				maxval = 2
		else:
			minval = 0
			maxval = 1

		return minval, maxval



	def calctimeslideroffset(self, instructiontimeminutes, slidervalueminutes):

		zoomstartminutes = slidervalueminutes - 15
		zoomendminutes = zoomstartminutes + 90

		partoneminutes = min(instructiontimeminutes, zoomstartminutes)
		parttwominutes = min(90, max(0, instructiontimeminutes - zoomstartminutes))
		partthreeminutes = max(0, instructiontimeminutes - zoomendminutes)

		normoffset = self.timeslidernormstepsize.getscaled(partoneminutes + partthreeminutes)
		zoomoffset = self.timesliderzoomstepsize.getscaled(parttwominutes)
		overalloffset = Vector.add(normoffset, zoomoffset)

		return overalloffset.getscaled(1.0/60.0)



	def calctempslidermetrics(self, displaytemp, selectedtemp):

		if displaytemp > selectedtemp:
			step = displaytemp - 2
		else:
			step = displaytemp - 4

		if displaytemp == selectedtemp:
			boxwidth = self.tempsliderstepsize.getscaled(3)
		else:
			boxwidth = self.tempsliderstepsize


		boxsize = Vector.createfromvalues(boxwidth.getx(), self.tempslidersize.gety())
		boxposition = Vector.add(self.tempsliderposition, self.tempsliderstepsize.getscaled(step))
		centreoffset = Vector.add(boxposition, boxwidth.getscaled(0.5))


		if displaytemp == selectedtemp:
			boxcentre = Vector.add(centreoffset, self.tempslidertextoffset)
			font = "Button Temps"
		else:
			boxcentre = Vector.add(centreoffset, self.tempslidercurrenttextoffset)
			font = "Snooze"

		if (displaytemp == 27) or (displaytemp == 3):
			boxsize = Vector.add(boxsize, self.sliderendreduction)

		if displaytemp == 3:
			boxposition = Vector.add(boxposition, self.sliderendshift)

		return str(displaytemp), boxposition, boxsize, boxcentre, font



	def calcbuttonmetrics(self, control, buttonname, selectorvalue):

		buttonlocation = control.getbuttonposition(buttonname)
		buttonsize = control.getbuttonsize(buttonname)
		buttonoverlaylocation = Vector.add(buttonlocation, self.filloffset)
		buttonoverlaysize = Vector.add(buttonsize, self.fillresize)
		buttoncolour = "Grey"
		buttonoutline = "button_outline"

		if buttonname[:9] == "Override ":
			timing = buttonname[9:]
			imagename = "timer_" + timing
			if selectorvalue == timing:
				buttoncolour = "Selected"
		elif buttonname[:5] == "Temp ":
			imagename = "c" + buttonname[6:]
		elif buttonname == "Exit":
			imagename = "return"
		elif buttonname[:16] == "Schedule Select ":
			buttonoutline = "large_button_outline"
			imagename = "Hide"
		else:
			imagename = "configure"

		return buttonlocation, buttonsize, buttonoverlaylocation, buttonoverlaysize, imagename, buttoncolour, buttonoutline



	def calcschedulebuttonmetrics(self, buttonposition, buttonsize, selectordata, buttonname):

		timetext, temptext = selectordata.getbuttonmeaningbylabel(buttonname[-1:])

		timeposition = Vector.add(buttonposition, Vector.createfromvalues(int(buttonsize.getx() / 2), 0))

		tempposition = Vector.add(timeposition, Vector.createfromvalues(0, 37))

		return timetext.getsecondlesstext(), str(temptext), timeposition, tempposition