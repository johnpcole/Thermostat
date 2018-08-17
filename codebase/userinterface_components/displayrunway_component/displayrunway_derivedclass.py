from ...common_components.vector_datatype import vector_module as Vector
from ...common_components.transition_datatype import transition_module as Transition
from .. import display_sharedfunctions as DisplayFunction
from . import runwaymetrics_baseclass as Metrics
from schedulebuilder_subcomponent import schedulebuilder_module as ScheduleBuilder
from . import displayrunway_privatefunctions as RunwayFunction



class DefineRunway(Metrics.DefineRunwayMetrics):

	def __init__(self):

		# Get the metrics using baseclass method
		Metrics.DefineRunwayMetrics.__init__(self)

		# Data for capturing the animation of the desired temperature
		self.desiredtemperature = Transition.createoldnewtransition(500, 1000, 0)

		# The current runway display definition
		self.artefacts = {}

	# -------------------------------------------------------------------
	# Build the Runway
	# -------------------------------------------------------------------

	def buildrunway(self, boilercontroller, currenttime, currentdate, displayobject, astrodata):

		self.artefacts = {}

		# Display current desired temperature
		newitems = self.drawdesiredtemperature(boilercontroller.getcurrentdesiredtemperature())
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Runway A"))

		# Draw upcoming desired temperatures (from schedule)
		displayedschedule = ScheduleBuilder.createschedulebuilder(boilercontroller, currenttime)
		newitems = self.drawinstructions(currenttime, displayedschedule, displayobject)
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Runway B"))

		# Draw hour/half/quarter markers & labels
		newitems = self.drawtimelineitems(currenttime)
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Runway C"))

		# Draw astro
		newitems = self.drawastrodata(currenttime, currentdate, astrodata.getlibrary())
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Runway D"))

		return self.artefacts


	# -------------------------------------------------------------------
	# Paints the scheduled settings at the top of the screen
	# -------------------------------------------------------------------

	def drawinstructions(self, currenttime, schedule, displayobject):

		outcome = {}

		lastpixel = -999

		index = 1000

		previousactive = False

		# Loop over scheduled times
		for scheduledtimevalue in schedule.gettimings():

			# Get desired temperature
			temperature = schedule.gettemp(scheduledtimevalue)
			textsize = displayobject.calculatetextsize(str(temperature), "Timeline Temps")
			isactive = schedule.getactive(scheduledtimevalue)

			# Work out whether to overwrite text or not
			if isactive != previousactive:
				textoverwrite = True
			else:
				textoverwrite = False

			label = str(index) + " "

			# Get position of marker & text
			markertop, markerbottom, marker2top, marker2bottom, markertext, lastpixel = self.calculateinstructionmetrics(scheduledtimevalue, currenttime, textsize, lastpixel, textoverwrite)

			# Draw marker
			outcome[label + "Instruction Line Upper"] = ("Line", markertop, markerbottom, DisplayFunction.getactivecolour("Grey", isactive), 1, "")
			outcome[label + "Instruction Line Join"] = ("Line", markerbottom, marker2top, DisplayFunction.getactivecolour("Grey", isactive), 1, "")
			outcome[label + "Instruction Line Lower"] = ("Line", marker2top, marker2bottom, DisplayFunction.getactivecolour("Grey", isactive), 1, "")

			# Draw desired temperature number
			outcome[label + "Instruction Foreground"] = ("Text", str(temperature), markertext, "Left",
										DisplayFunction.getactivecolour(DisplayFunction.gettemperaturecolour(temperature), isactive), "Timeline Temps")

			# Draw desired temperature number blanking background
			if textoverwrite == True:
				outcome[label + "Instruction Background"] = ("Box", marker2top, self.futurebackgroundsize, "Black", "Black", 3)

			index = index + 1
			previousactive = isactive

		return outcome



	# -------------------------------------------------------------------
	# Paints the timeline hour/half/quarter items at the top of the screen
	# -------------------------------------------------------------------

	def drawtimelineitems(self, currenttime):

		outcome = {}

		outcome["Timeline Zero Line"] = ("Line", self.zerolinetop, self.zerolinebottom, "Grey", 1, "")

		lasthour = currenttime.gethour()

		# Print the hour labels
		for hourindex in range(lasthour, lasthour + 14):

			# Display the current hour at the current time marker only if it's exactly on the clock
			if (currenttime.getminute() == 0) or (hourindex > lasthour):

				# Position of hour marker line & text etc
				markertop, markerbottom, textposition, textlabel, indexer = self.calculatetimemarkermetrics(currenttime, hourindex, 0)

				# Draw hour marker number
				outcome["Timeline Hour Text " + indexer] = ("Text",
															textlabel, textposition, "Left", "Grey", "Timeline Hours")

			for subindex in range(0, 4):

				# Position of marker
				markertop, markerbottom, textposition, textlabel, indexer = self.calculatetimemarkermetrics(currenttime, hourindex, subindex)

				# Only draw marker if it's to the right of the current time marker
				if self.startline < markertop.getx():
					outcome["Timeline Line " + indexer] = ("Line", markertop, markerbottom, "Grey", 1, "")

		return outcome



	# -------------------------------------------------------------------
	# Paints the desired temperature at the top of the screen
	# -------------------------------------------------------------------

	def drawdesiredtemperature(self, desiredtemperature):

		outcome = {}

		self.desiredtemperature.updatevalue(desiredtemperature)

		displayedtemperature, transitionfraction, position, colour = self.calculatedesiredtempmetrics(self.desiredtemperature)

		outcome["Desired Temp"] = ("Text", str(displayedtemperature), position, "Right", colour, "Desired Temp")

		outcome["Desired Temp Screen Background"] = ("Box", self.backgroundposition, self.backgroundsize, "Black", "", 0)

		return outcome



	# -------------------------------------------------------------------
	# Paints the astro data
	# -------------------------------------------------------------------

	def drawastrodata(self, currenttime, currentdate, astrolibrary):

		outcome = {}

		counter = 0

		# Loop over scheduled times
		for astroitem in astrolibrary:

			counter = counter + 1

			displaymode = RunwayFunction.getdateshift(currentdate, astroitem.getdate())

			if displaymode != -999:
				blocksize, blockcolour, blocklabel, starttop, endtop, startbottom, endbottom, startborder, endborder = self.calculateastrometrics(astroitem, currenttime, displaymode, counter)

				# Draw block
				outcome[blocklabel + " 1"] = ("Box", starttop, blocksize, blockcolour, "", 0)

				# Draw lines
				if startborder == True:
					outcome[blocklabel + " 2"] = ("Line", starttop, startbottom, "Black", 1, "")

				if endborder == True:
					outcome[blocklabel + " 3"] = ("Line", endtop, endbottom, "Black", 1, "")

		outcome["A Background"] = ("Box", Vector.createfromvalues(0, self.astrotop),
									Vector.createfromvalues(480, self.astroheight), "Sky Nig", "", 0)

		return outcome
