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

		# Position of bottom of hour markers
		self.hourbottom = 15

		# Dimensions of blanking out background for desired temperature
		self.backgroundstart = Vector.createfromvalues(self.startline, 0)
		self.backgroundend = Vector.createfromvalues(self.startline * 2, self.height)

		# Dimensions of blanking out background for future desired temperatures
		self.futurebackgroundpositionoffset = Vector.createfromvalues(-2, 3)
		self.futurebackgroundsizeoffset = Vector.createfromvalues(4, -7)



	def calculateinstructionmetrics(self, scheduledtime, currenttime, textsize):

		# Position of marker
		houroffset = Clock.getfuturetimevalue(scheduledtime.getvalue(), currenttime.getvalue()) - (3600 * currenttime.gethour())
		pixelposition = self.startline + int(houroffset * self.timescale / 3600) - self.calculatemarkeroffsets(
			currenttime)

		# Marker & Text metrics
		markertop = Vector.createfromvalues(pixelposition, 18)
		markerbottom = Vector.createfromvalues(pixelposition, self.height)
		markertext = Vector.createfromvalues(pixelposition + 3, self.height - 29)

		# Work out the effective box the text sits on
		blankingposition = Vector.add(self.futurebackgroundpositionoffset, markertext)
		blankingsize = Vector.add(self.futurebackgroundsizeoffset, textsize)
		lastpixel = blankingposition.getx() + blankingsize.getx()



		return markertop, markerbottom, markertext, blankingposition, blankingsize, lastpixel



	def calculatemarkeroffsets(self, currenttime):

		# Number of pixels markers are shifted left
		return int(self.timescale * ((currenttime.getminute() * 60) + currenttime.getsecond()) / 3600)



	def calculatemarkerlineheight(self, subindex):

		if subindex == 0:
			return self.hourbottom
		else:
			return (3 * (subindex + 1) % 2)



	def calculatedesiredtempmetrics(self, desiredtemperature):

		displayedtemperature = desiredtemperature.getswitchedvalue()

		transitionfraction = desiredtemperature.gettransitionfraction()

		positionalong = DisplayFunction.getonewaytransitionposition(self.startline - 5, self.startline,
																	transitionfraction)
		position = Vector.createfromvalues(positionalong, -3)

		colour = DisplayFunction.gettransitioncolour(displayedtemperature, transitionfraction)

		return displayedtemperature, transitionfraction, position, colour



	def calculatemarkerposition(self, currenttime, hourindex, subindex):

		hourmarker = self.startline + (hourindex * self.timescale) - self.calculatemarkeroffsets(currenttime)

		if subindex > 0:
			return (hourmarker - int(subindex * self.timescale / 4))
		else:
			return hourmarker
