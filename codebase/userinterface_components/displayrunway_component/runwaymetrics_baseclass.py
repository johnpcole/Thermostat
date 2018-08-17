from ...common_components.vector_datatype import vector_module as Vector
from ...common_components.clock_datatype import clock_module as Clock
from .. import display_sharedfunctions as DisplayFunction
from time import localtime as LocalTime



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
		self.astrotop = 0
		self.astrobottom = 3



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



	def calculateastrometrics(self, astroobject, currenttime):

		blocktype = astroobject.gettype()
		blockcolour = "Sky " + blocktype

		if astroobject.getdate() == "Tomorrow":
			timevalueadd = 24 * 3600
			suffix = "2"
			blockcolour = "Sky " + blocktype
		elif astroobject.getdate() == "Yesterday":
			timevalueadd = -24 * 3600
			suffix = "3"
			blockcolour = "Red " + blocktype
		else:
			timevalueadd = 0
			suffix = "1"
			blockcolour = "Yel " + blocktype

		if LocalTime().tm_isdst == 1:
			timevalueadd = timevalueadd + 3600

		endtime = astroobject.getendtime()
		if endtime.getsecond() > 0:
			endvalue = endtime.getvalue() + timevalueadd + 1
		else:
			endvalue = endtime.getvalue() + timevalueadd

		pixelstart = self.calculaterunwayitemoffset(astroobject.getstarttime().getvalue() + timevalueadd, currenttime, False)
		pixelend = self.calculaterunwayitemoffset(endvalue, currenttime, False)
		blockposition = Vector.createfromvalues(pixelstart + 1, self.astrotop)
		blocksize = Vector.createfromvalues(pixelend - pixelstart - 2, self.astrobottom)

		lineblockposition = Vector.createfromvalues(pixelstart, self.astrotop)
		lineblocksize = Vector.createfromvalues(pixelend - pixelstart, self.astrobottom)


		if blocktype == "Day":
			blocklabel = "E" + suffix
		elif blocktype == "Civ":
			blocklabel = "D" + suffix
		elif blocktype == "Nau":
			blocklabel = "C" + suffix
		elif blocktype == "Ast":
			print blocktype, astroobject.getstarttime().gettext(), endtime.gettext(), pixelstart, pixelend
			blocklabel = "B" + suffix
		else:
			blocklabel = "Z" + suffix


		return blockposition, blocksize, blockcolour, blocklabel, lineblockposition, lineblocksize

