from ....common_components.vector_datatype import vector_module as Vector



class DefineSlider:

	def __init__(self, sliderposition, slidersize):

		self.sliderendreduction = Vector.createfromvalues(-1, 0)
		self.sliderendshift = Vector.createfromvalues(1, 0)

		self.sliderposition = Vector.add(sliderposition, Vector.createfromvalues(16, 1)) #To get to 40, 25

		self.slidersize = Vector.subtract(slidersize, Vector.createfromvalues(32, 2)) #To get to 400, 78

		self.sliderstepsize = Vector.createfromvalues(self.slidersize.getx() / 25, 0)
		self.slidertextoffset = Vector.createfromvalues(0, 19)

		self.slidercurrenttextoffset = Vector.createfromvalues(0, 33)

		self.slidertemptextoffset = Vector.createfromvalues(0, 19)

		self.linkstart = Vector.createfromvalues(30, 175)
		self.linkend = Vector.createfromvalues(450, 175)


	def calcslidermisc(self):

		return self.linkstart, self.linkend



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

