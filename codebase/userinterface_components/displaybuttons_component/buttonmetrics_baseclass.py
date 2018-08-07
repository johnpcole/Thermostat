from ...common_components.vector_datatype import vector_module as Vector



class DefineButtonMetrics:

	def __init__(self):

		self.textoffset = Vector.createfromvalues(25, 5)

		self.filloffset = Vector.createfromvalues(1, 1)

		self.fillresize = Vector.createfromvalues(-2, -2)

		self.sliderposition = Vector.createfromvalues(40, 25)

		self.slidersize = Vector.createfromvalues(400, 78)

		self.sliderstepsize = Vector.createfromvalues(self.slidersize.getx() / 25, 0)
		self.slidertextoffset = Vector.createfromvalues(0, 19)

		self.slidercurrenttextoffset = Vector.createfromvalues(0, 33)

		self.origin = Vector.createfromvalues(0, 0)

		self.slideroutlineoffset = Vector.createfromvalues(-1, -1)
		self.sliderendreduction = Vector.createfromvalues(-1, 0)
		self.sliderendshift = Vector.createfromvalues(1, 0)



	def calcslidermetrics(self, displaytemp, selectedtemp):

		if displaytemp > selectedtemp:
			step = displaytemp - 2
		else:
			step = displaytemp - 4

		if displaytemp == selectedtemp:
			boxwidth = self.sliderstepsize.getscaled(3)
		else:
			boxwidth = self.sliderstepsize


		boxsize = Vector.createfromvalues(boxwidth.getx(), self.slidersize.gety())
		boxposition = Vector.add(self.sliderposition, self.sliderstepsize.getscaled(step))
		centreoffset = Vector.add(boxposition, boxwidth.getscaled(0.5))


		if displaytemp == selectedtemp:
			boxcentre = Vector.add(centreoffset, self.slidertextoffset)
			font = "Button Temps"
		else:
			boxcentre = Vector.add(centreoffset, self.slidercurrenttextoffset)
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
		else:
			imagename = "c" + buttonname[6:]

		return buttonlocation, buttonsize, buttonoverlaylocation, buttonoverlaysize, imagename, buttoncolour

