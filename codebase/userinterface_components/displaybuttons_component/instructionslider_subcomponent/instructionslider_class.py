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

		self.slidermin["Hour"] = 0
		self.slidermax["Hour"] = 23
		self.sliderstep["Hour"] = 1
		self.sliderposition["Hour"] = hoursliderposition
		self.slidersize["Hour"] = hourslidersize
		self.stepsize["Hour"] = 11
		self.selectedstepsize["Hour"] = 27
		self.direction["Hour"] = False


		self.slidermin["Min"] = 0
		self.slidermax["Min"] = 55
		self.sliderstep["Min"] = 5
		self.sliderposition["Min"] = minsliderposition
		self.slidersize["Min"] = minslidersize
		self.stepsize["Min"] = 20
		self.selectedstepsize["Min"] = 60
		self.direction["Min"] = False


		self.slidermin["Temp"] = 3
		self.slidermax["Temp"] = 27
		self.sliderstep["Temp"] = 1
		self.sliderposition["Temp"] = tempsliderposition
		self.slidersize["Temp"] = tempslidersize
		self.stepsize["Temp"] = 10
		self.selectedstepsize["Temp"] = 40
		self.direction["Temp"] = True



	def calcslidermetrics(self, mode, displayedvalue, selectedvalue):

		extrashift, effectivevalue = self.calcselectedshift(mode, displayedvalue, selectedvalue)

		verticalstart = int(effectivevalue / self.sliderstep[mode]) * self.stepsize[mode]
		if extrashift == True:
			verticalstart = verticalstart + self.selectedstepsize[mode] - self.stepsize[mode]

		if displayedvalue == selectedvalue:
			verticalsize = self.selectedstepsize[mode]
		else:
			verticalsize = self.stepsize[mode]

		position = Vector.add(self.sliderposition[mode], Vector.createfromvalues(0, verticalstart))
		size = Vector.createfromvalues(self.slidersize[mode].getx(), verticalsize)
		indexlabel = mode + " " + str(displayedvalue)
		if mode == "Hour":
			background = str(displayedvalue + 3)
		elif mode == "Min":
			background = str(4 + int(displayedvalue / 5))
		else:
			background = str(displayedvalue)
		return position, size, indexlabel, background



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