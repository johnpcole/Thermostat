from ...common_components.vector_datatype import vector_module as Vector
from ...common_components.clock_datatype import clock_module as Clock
from .. import display_sharedfunctions as DisplayFunction


class DefineRunwayMetrics:

	def __init__(self):

		# Position of current time marker in the runway
		self.startline = 68

		# How many pixels make up an hour (36 or 48) in the runway
		self.timescale = 36

		# Height of runway (actually one pixel more!)
		self.height = 48

		# Position of top of desired temp markers
		self.instructiontop = 18
		self.instructionmiddle = 22

		# Position of bottom of hour markers
		self.hourbottom = 15

		# relative offset of future desired temp text
		self.textoffset = Vector.createfromvalues(3, -29)

		# Dimensions of blanking out background for desired temperature
		self.backgroundstart = Vector.createfromvalues(self.startline, 0)
		self.backgroundend = Vector.createfromvalues(self.startline * 2, self.height)

		# Dimensions of blanking out background for future desired temperatures
		self.futurebackgroundbuffer = 5
		self.futurebackgroundsize = Vector.createfromvalues(40, self.height - self.instructionmiddle)

		# Position of hour text
		self.hourtextoffset = Vector.createfromvalues(3, 1)

		# Position of daylight bars
		self.astrotop = 0
		self.astrobottom = 2



	def calculateinstructionmetrics(self, scheduledtimevalue, currenttime, textsize, lastpixelposition, textoverwrite):

		# Position of marker
		pixelposition = self.calculaterunwayitemoffset(scheduledtimevalue, currenttime, True)

		# Marker & Text metrics
		markertop = Vector.createfromvalues(pixelposition, self.instructiontop)
		markerbottom = Vector.createfromvalues(pixelposition, self.instructionmiddle)
		marker2top = Vector.createfromvalues(pixelposition, self.instructionmiddle)
		marker2bottom = Vector.createfromvalues(pixelposition, self.height)
		markertext = Vector.add(marker2bottom, self.textoffset)

		gapfromprevious = pixelposition - lastpixelposition

		if (gapfromprevious < self.futurebackgroundbuffer) and (textoverwrite == False):
			offsetter = Vector.createfromvalues(self.futurebackgroundbuffer - gapfromprevious, 0)
			markertext = Vector.add(markertext, offsetter)
			marker2top = Vector.add(marker2top, offsetter)
			marker2bottom = Vector.add(marker2bottom, offsetter)

		newlastpixelposition = markertext.getx() + textsize.getx()

		return markertop, markerbottom, marker2top, marker2bottom, markertext, newlastpixelposition



	def calculatedesiredtempmetrics(self, desiredtemperature):

		displayedtemperature = desiredtemperature.getswitchedvalue()

		transitionfraction = desiredtemperature.gettransitionfraction()

		positionalong = DisplayFunction.getonewaytransitionposition(self.startline - 5, self.startline,
																	transitionfraction)
		position = Vector.createfromvalues(positionalong, -3)

		colour = DisplayFunction.gettransitioncolour(displayedtemperature, transitionfraction)

		return displayedtemperature, transitionfraction, position, colour



	def calculatetimemarkermetrics(self, currenttime, hourindex, subindex):

		instructiontimevalue = (hourindex * 3600) - (subindex * 900)
		pixelposition = self.calculaterunwayitemoffset(instructiontimevalue, currenttime, True)

		if subindex == 0:
			height = self.hourbottom
		else:
			height = 3 * (subindex + 1) % 2

		markertop = Vector.createfromvalues(pixelposition, 0)
		markerbottom = Vector.createfromvalues(pixelposition, height)
		textposition = Vector.add(markertop, self.hourtextoffset)
		textlabel = Clock.convert24hourtohuman(hourindex)

		instructionlabel = str(1000 + (hourindex * 10) + subindex)

		return markertop, markerbottom, textposition, textlabel, instructionlabel



	def calculaterunwayitemoffset(self, instructiontimevalue, currenttime, futuremode):

		if futuremode == True:
			visualinstructiontimevalue = Clock.getfuturetimevalue(instructiontimevalue, currenttime.getvalue())
		else:
			visualinstructiontimevalue = instructiontimevalue
		visualinstructionoffset = visualinstructiontimevalue - currenttime.getvalue()
		return self.startline + int((self.timescale * visualinstructionoffset) / 3600)



	def calculateastrometrics(self, astroobject, currenttime):

		if astroobject.gettomorrow() == True:
			timevalueadd = 24 * 3600
			suffix = "2"
		else:
			timevalueadd = 0
			suffix = "1"

		pixelstart = self.calculaterunwayitemoffset(astroobject.getstarttime().getvalue() + timevalueadd, currenttime, False)
		pixelend = self.calculaterunwayitemoffset(astroobject.getendtime().getvalue() + timevalueadd, currenttime, False)

		blockposition = Vector.createfromvalues(pixelstart, self.astrotop)
		blocksize = Vector.createfromvalues(pixelend - pixelstart, self.astrobottom)

		blocktype = astroobject.gettype()
		blockcolour = "Sky " + blocktype

		if blocktype == "Day":
			blocklabel = "D" + suffix
		elif blocktype == "Civ":
			blocklabel = "C" + suffix
		elif blocktype == "Nau":
			blocklabel = "B" + suffix
		elif blocktype == "Ast":
			blocklabel = "A" + suffix
		else:
			blocklabel = "Z" + suffix

		return blockposition, blocksize, blockcolour, blocklabel

