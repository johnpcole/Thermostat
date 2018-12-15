from ....common_components.vector_datatype import vector_module as Vector



class DefineSlider:

	def __init__(self, hoursliderposition, hourslidersize, minsliderposition, minslidersize, tempsliderposition, tempslidersize):

		self.slidermin = {}
		self.slidermax = {}
		self.sliderstep = {}
		self.sliderposition = {}
		self.slidersize = {}
		self.stepsize = {}
		self.selectedstepsize = {}
		self.direction = {}
		self.textoffset = {}
		self.textalignment = {}


		self.slidermin["Hour"] = 0
		self.slidermax["Hour"] = 23
		self.sliderstep["Hour"] = 1
		self.sliderposition["Hour"] = hoursliderposition
		self.slidersize["Hour"] = hourslidersize
		self.stepsize["Hour"] = 10
		self.selectedstepsize["Hour"] = 50
		self.direction["Hour"] = False


		self.slidermin["Min"] = 0
		self.slidermax["Min"] = 55
		self.sliderstep["Min"] = 5
		self.sliderposition["Min"] = minsliderposition
		self.slidersize["Min"] = minslidersize
		self.stepsize["Min"] = 21
		self.selectedstepsize["Min"] = 49
		self.direction["Min"] = False


		self.slidermin["Temp"] = 3
		self.slidermax["Temp"] = 27
		self.sliderstep["Temp"] = 1
		self.sliderposition["Temp"] = tempsliderposition
		self.slidersize["Temp"] = tempslidersize
		self.stepsize["Temp"] = 10
		self.selectedstepsize["Temp"] = 40
		self.direction["Temp"] = True


		self.textoffset["Hour"] = Vector.createfromvalues(70, 3)
		self.textoffset["Min"] = Vector.createfromvalues(10, 3)
		self.textoffset["Temp"] = Vector.createfromvalues(40, -1)
		self.textalignment["Hour"] = "Right"
		self.textalignment["Min"] = "Left"
		self.textalignment["Temp"] = "Centre"



	def calcslidermetrics(self, mode, displayedvalue, selectedvalue):

		extrashift, effectivevalue = self.calcselectedshift(mode, displayedvalue, selectedvalue)

		verticalstart = int(effectivevalue / self.sliderstep[mode]) * self.stepsize[mode]
		if extrashift == True:
			verticalstart = verticalstart + self.selectedstepsize[mode] - self.stepsize[mode]

		if displayedvalue == selectedvalue:
			verticalsize = self.selectedstepsize[mode]
			text = str(displayedvalue)
			if mode != "Temp":
				text = ("00" + text)[-2:]
		else:
			verticalsize = self.stepsize[mode]
			text = "NONE"

		position = Vector.add(self.sliderposition[mode], Vector.createfromvalues(1, verticalstart))
		size = Vector.createfromvalues(self.slidersize[mode].getx() - 2, verticalsize)
		indexlabel = mode + " " + str(displayedvalue)
		#if mode == "Hour":
		#	background = str(displayedvalue + 3)
		#elif mode == "Min":
		#	background = str(4 + int(displayedvalue / 5))
		if mode == "Temp":
			background = str(displayedvalue)
			textcolour = "Black"
		else:
			background = "Black"
			textcolour = "White"

		textpos = Vector.add(position, self.textoffset[mode])

		return position, size, indexlabel, background, text, textpos, self.textalignment[mode], textcolour



	def calcselectedshift(self, mode, displayedvalue, selectedvalue):

		extrashift = False
		if self.direction[mode] == True:
			effectivevalue = self.slidermax[mode] - displayedvalue
			if displayedvalue < selectedvalue:
				extrashift = True
		else:
			effectivevalue = displayedvalue - self.slidermin[mode]
			if displayedvalue > selectedvalue:
				extrashift = True

		return extrashift, effectivevalue



	def calculatesliderrange(self, mode):

		return self.slidermin[mode], self.slidermax[mode], self.sliderstep[mode]