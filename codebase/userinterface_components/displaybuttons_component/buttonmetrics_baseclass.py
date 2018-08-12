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

		stepsize = 16
		zoomstepsize = 40

		self.timesliderstepsize = Vector.createfromvalues(stepsize, 0)
		self.timesliderzoomstepsize = Vector.createfromvalues(zoomstepsize, 0)

		self.timesliderhourlineheight = Vector.createfromvalues(0, 15)
		self.timesliderzoomlineheight = Vector.createfromvalues(0, 20)
		self.timeslidermarkeroffset = Vector.createfromvalues(5, 3)

		self.timesliderhourtextoffset = Vector.createfromvalues(2, 1)
		self.timesliderzoomtextoffset = Vector.createfromvalues(2, 5)

		self.timesliderzoomfirstmarkeroffset = Vector.createfromvalues((zoomstepsize/4)-(stepsize/4), 0)
		self.timesliderzoomsecondmarkeroffset = Vector.subtract(self.timesliderzoomstepsize, Vector.createfromvalues(stepsize, 0))
		self.timesliderpostzoomoffset = Vector.createfromvalues((6*zoomstepsize/4)-(6*stepsize/4), 0)

		self.timesliderzoomsubstepsize = Vector.createfromvalues(zoomstepsize/4, 0)

		self.timeslidermajorsubmarkheight = Vector.createfromvalues(0, 4)
		self.timesliderminorsubmarkheight = Vector.createfromvalues(0, 2)


	def calctimeslidermetrics(self, hourindex, slidervalue):

		equivalentsliderhour = int(slidervalue / 3600)

		boxposition = Vector.add(self.timesliderposition, self.timesliderstepsize.getscaled(hourindex))
		fontsize = "Snooze"
		textoffset = self.timesliderhourtextoffset
		lineheight = self.timesliderhourlineheight
		colour = "Grey"
		zoom = False
		if (hourindex == equivalentsliderhour) or (hourindex == equivalentsliderhour + 1):
			boxposition = Vector.add(boxposition, self.timesliderzoomfirstmarkeroffset)
			fontsize = "Timeline Hours"
			textoffset = self.timesliderzoomtextoffset
			lineheight = self.timesliderzoomlineheight
			colour = "White"
			if hourindex == equivalentsliderhour + 1:
				boxposition = Vector.add(boxposition, self.timesliderzoomsecondmarkeroffset)
			else:
				zoom = True
		elif hourindex > equivalentsliderhour + 1:
			boxposition = Vector.add(boxposition, self.timesliderpostzoomoffset)
			if hourindex == 24:
				fontsize = "Hide"

		markertop = Vector.add(boxposition, self.timeslidermarkeroffset)
		markerbottom = Vector.add(markertop, lineheight)
		sanitisedhour = hourindex % 12
		if sanitisedhour == 0:
			sanitisedhour = 12
		hourlabelposition = Vector.add(markertop, textoffset)

		return markertop, markerbottom, hourlabelposition, str(sanitisedhour), str(hourindex), fontsize, colour, zoom



	def calctimeslidersubmetrics(self, subindex, hourmarkertopposition):

		submarkertop = Vector.add(hourmarkertopposition, self.timesliderzoomsubstepsize.getscaled(subindex))

		if (subindex % 2) == 0:
			height = self.timeslidermajorsubmarkheight
		else:
			height = self.timesliderminorsubmarkheight

		submarkerbottom = Vector.add(submarkertop, height)

		return submarkertop, submarkerbottom, str(subindex + 1000)


	def calctimesliderinstructionmetrics(self, instructiontime, slidervalue):

		equivalentsliderminutes = 60 * (int(slidervalue / 3600))
		instructionmins = int(instructiontime.getvalue() / 60)

















		if (instructionmins > equivalentsliderminutes - 15):
			if (instructionmins < equivalentsliderminutes + 75):
				x = postzoomcalcs
			else:
				x = zoomcalcs
		else:
			x = prezoomcalcs






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

		if buttonname[:9] == "Override ":
			timing = buttonname[9:]
			imagename = "timer_" + timing
			if selectorvalue == timing:
				buttoncolour = "Selected"
		elif buttonname[:5] == "Temp ":
			imagename = "c" + buttonname[6:]
		elif buttonname == "Exit":
			imagename = "return"
		else:
			imagename = "configure"

		return buttonlocation, buttonsize, buttonoverlaylocation, buttonoverlaysize, imagename, buttoncolour


