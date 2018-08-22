from ....common_components.vector_datatype import vector_module as Vector



class DefineSlider:

	def __init__(self):

		# Buttons

		self.textoffset = Vector.createfromvalues(25, 5)

		self.origin = Vector.createfromvalues(0, 0)

		# Timeline Slider

		self.sliderposition = Vector.createfromvalues(24, 24)

		self.slidersize = Vector.createfromvalues(432, 80)

		self.slidernormstepsize = Vector.createfromvalues(16, 0)
		self.sliderzoomstepsize = Vector.createfromvalues(40, 0)

		# Timeline Slider - Timings

		self.sliderhourlineheight = Vector.createfromvalues(0, 15)
		self.sliderzoomlineheight = Vector.createfromvalues(0, 30)
		self.slidermarkeroffset = Vector.createfromvalues(5, 6)
		self.sliderzoommarkeroffset = Vector.createfromvalues(5, 3)

		self.sliderhourtextoffset = Vector.createfromvalues(2, 1)
		self.sliderzoomtextoffset = Vector.createfromvalues(2, 5)

		self.slidermajorsubmarkheight = Vector.createfromvalues(0, 4)
		self.sliderminorsubmarkheight = Vector.createfromvalues(0, 2)

		# Timeline Slider - Temperatures

		self.slidertempmarkeroffset = Vector.createfromvalues(5, 24)
		self.slidertempmarkeroneheight = Vector.createfromvalues(0, 10)
		self.slidertempmarkertwoheight = Vector.createfromvalues(0, 30)



	def calcslidertimemetrics(self, hourindex, subindex, sliderhour):

		sliderminutes = sliderhour * 60
		instructionminutes = (hourindex * 60) + (subindex * 15)

		boxposition = Vector.add(self.sliderposition,
								 self.calcslideroffset(instructionminutes, sliderminutes))
		fontsize = "Snooze"
		textoffset = self.sliderhourtextoffset
		lineheight = self.sliderhourlineheight
		lineoffset = self.slidermarkeroffset
		colour = "Grey"
		if (hourindex == sliderhour) or (hourindex == sliderhour + 1):
			fontsize = "Timeline Hours"
			textoffset = self.sliderzoomtextoffset
			lineheight = self.sliderzoomlineheight
			colour = "White"
			lineoffset = self.sliderzoommarkeroffset
		else:
			if hourindex == 24:
				fontsize = "Hide"
		if subindex != 0:
			fontsize = "Hide"
			if (subindex % 2) == 0:
				lineheight = self.slidermajorsubmarkheight
			else:
				lineheight = self.sliderminorsubmarkheight

		markertop = Vector.add(boxposition, lineoffset)
		markerbottom = Vector.add(markertop, lineheight)
		sanitisedhour = hourindex % 12
		if sanitisedhour == 0:
			sanitisedhour = 12
		hourlabelposition = Vector.add(markertop, textoffset)

		return markertop, markerbottom, hourlabelposition, str(sanitisedhour), str(
			instructionminutes), fontsize, colour



	def calcslidertempmetrics(self, instructiontime, instructiontemp, sliderhour):

		sliderminutes = 60 * sliderhour
		instructionminutes = int(instructiontime / 60)

		boxposition = Vector.add(self.sliderposition,
								 self.calcslideroffset(instructionminutes, sliderminutes))

		marker1top = Vector.add(boxposition, self.slidertempmarkeroffset)
		marker1bottom = Vector.add(marker1top, self.slidertempmarkeroneheight)
		marker2top = marker1bottom
		marker2bottom = Vector.add(marker2top, self.slidertempmarkertwoheight)

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



	def calcslideroffset(self, instructiontimeminutes, slidervalueminutes):

		zoomstartminutes = slidervalueminutes - 15
		zoomendminutes = zoomstartminutes + 90

		partoneminutes = min(instructiontimeminutes, zoomstartminutes)
		parttwominutes = min(90, max(0, instructiontimeminutes - zoomstartminutes))
		partthreeminutes = max(0, instructiontimeminutes - zoomendminutes)

		normoffset = self.slidernormstepsize.getscaled(partoneminutes + partthreeminutes)
		zoomoffset = self.sliderzoomstepsize.getscaled(parttwominutes)
		overalloffset = Vector.add(normoffset, zoomoffset)

		return overalloffset.getscaled(1.0 / 60.0)



	def calcslideroverall(self):

		return self.sliderposition, self.slidersize

