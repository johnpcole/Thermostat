from ...common_components.vector_datatype import vector_module as Vector
from ...common_components.clock_datatype import clock_module as Clock
from .. import display_sharedfunctions as DisplayFunction
from . import displayrunway_privatefunctions as RunwayFunction



class DefineRunwayMetrics:

	def __init__(self):

		# Position of runway
		self.runwaytop = 5

		# Position of current time marker in the runway
		self.startline = 68

		# How many pixels make up an hour (36 or 48) in the runway
		self.timescale = 36

		# Height of runway (actually one pixel more!)
		self.height = 48 + self.runwaytop

		# Position of top of desired temp markers
		self.instructiontop = 18 + self.runwaytop
		self.instructionmiddle = 22 + self.runwaytop

		# Position of bottom of hour markers
		self.hourbottom = 15

		# relative offset of future desired temp text
		self.textoffset = Vector.createfromvalues(3, -29)

		# Dimensions of blanking out background for desired temperature
		self.backgroundposition = Vector.createfromvalues(self.startline - 1, self.runwaytop)
		self.backgroundsize = Vector.createfromvalues(self.startline + 2, 1 + self.height - self.runwaytop)

		# Zero line dimensions
		self.zerolinetop = Vector.createfromvalues(self.startline, self.runwaytop)
		self.zerolinebottom = Vector.createfromvalues(self.startline, self.height)

		# Dimensions of blanking out background for future desired temperatures
		self.futurebackgroundbuffer = 5
		self.futurebackgroundsize = Vector.createfromvalues(40, self.height - self.instructionmiddle)

		# Position of hour text
		self.hourtextoffset = Vector.createfromvalues(3, 1)

		# Position of daylight bars
		self.astrotop = 20
		self.astroheight = 30



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
		position = Vector.createfromvalues(positionalong, self.runwaytop - 3)

		colour = DisplayFunction.gettransitioncolour(displayedtemperature, transitionfraction)

		return displayedtemperature, transitionfraction, position, colour



	def calculatetimemarkermetrics(self, currenttime, hourindex, subindex):

		instructiontimevalue = (hourindex * 3600) - (subindex * 900)
		pixelposition = self.calculaterunwayitemoffset(instructiontimevalue, currenttime, True)

		if subindex == 0:
			height = self.hourbottom
		else:
			height = 3 * (subindex + 1) % 2

		markertop = Vector.createfromvalues(pixelposition, self.runwaytop)
		markerbottom = Vector.createfromvalues(pixelposition, self.runwaytop + height)
		textposition = Vector.add(markertop, self.hourtextoffset)
		textlabel = Clock.convert24hourtohuman(hourindex)

		instructionlabel = str(1000 + (hourindex * 10) + subindex)

		return markertop, markerbottom, textposition, textlabel, instructionlabel



	def calculaterunwayitemoffset(self, instructiontimevalue, currentaccuratetime, futuremode):

		currenttimevalue = currentaccuratetime.getvalue()

		timelineoffset = int((self.timescale * currenttimevalue) / 3600)

		if futuremode == True:
			futureinstructiontimevalue = Clock.getfuturetimevalue(instructiontimevalue, currenttimevalue)
		else:
			futureinstructiontimevalue = instructiontimevalue

		instructionoffset = int((self.timescale * futureinstructiontimevalue) / 3600)

		return self.startline + instructionoffset - timelineoffset



	def calculateastrometrics(self, astroobject, currenttime, indexer):

		blocktype = astroobject.gettype()
		blockcolour = "Sky " + blocktype

		timevalueadd = RunwayFunction.gettimeshiftervalue(indexer, astroobject.getdate())

		startborder = astroobject.getstartvalidity()
		endborder = astroobject.getendvalidity()

		starttimevalue = RunwayFunction.getsanitisedtimevalue(astroobject.getstarttime(), startborder, "Start")
		endtimevalue = RunwayFunction.getsanitisedtimevalue(astroobject.getendtime(), endborder, "End")

		pixelstart = self.calculaterunwayitemoffset(starttimevalue + timevalueadd, currenttime, False)
		pixelend = self.calculaterunwayitemoffset(endtimevalue + timevalueadd, currenttime, False)
		starttop = Vector.createfromvalues(pixelstart, self.astrotop)
		endtop = Vector.createfromvalues(pixelend, self.astrotop)
		startbottom = Vector.createfromvalues(pixelstart, self.astrotop + self.astroheight)
		endbottom = Vector.createfromvalues(pixelend, self.astrotop + self.astroheight)
		blocksize = Vector.add(Vector.subtract(endbottom, starttop), Vector.createfromvalues(1, 0))

		blocklabel = RunwayFunction.getblocklabel(blocktype, indexer)

		return blocksize, blockcolour, blocklabel, starttop, endtop, startbottom, endbottom, startborder, endborder


