from ...common_components.vector_datatype import vector_module as Vector
from ...common_components.clock_datatype import clock_module as Clock
from ...common_components.transition_datatype import transition_module as Transition
from .. import display_sharedfunctions as DisplayFunction
from . import runwaymetrics_baseclass as Metrics
from schedulebuilder_subcomponent import schedulebuilder_module as ScheduleBuilder


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

	def buildrunway(self, boilercontroller, currenttime, displayobject):

		self.artefacts = {}

		# Display current desired temperature
		newitems = self.drawdesiredtemperature(boilercontroller.getcurrentdesiredtemperature())
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Runway A"))

		# Draw upcoming desired temperatures (from schedule)
		displayedschedule = ScheduleBuilder.createschedulebuilder(boilercontroller, currenttime)
		newitems = self.drawinstructions(currenttime, displayedschedule, displayobject)
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Runway B"))

		# Draw hour labels
		newitems = self.drawtimelinenumbers(currenttime)
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Runway C"))

		# Draw hour/half/quarter markers
		newitems = self.drawtimelinemarkers(currenttime)
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
	# Paints the timeline hour labels at the top of the screen
	# -------------------------------------------------------------------

	def drawtimelinenumbers(self, currenttime):

		outcome = {}

		lasthour = currenttime.gethour()

		# Print the hour labels
		for hourindex in range(0, 14):

			# Display the current hour at the current time marker only if it's exactly on the clock
			if (currenttime.getminute() == 0) or (hourindex > 0):

				# Position of hour marker line
				hourmarker = self.calculatemarkerposition(currenttime, hourindex, 0)

				# Draw hour marker number
				outcome["Timeline Hour Text " + str(1000 + hourindex)] = ("Text",
										Clock.convert24hourtohuman(hourindex + lasthour),
										Vector.createfromvalues(hourmarker + 3, 1), "Left", "Grey", "Timeline Hours")

		outcome["Timeline Zero Line"] = ("Line", self.backgroundstart,
												Vector.createfromvalues(self.startline, self.height), "Grey", 1, "")

		return outcome



	# -------------------------------------------------------------------
	# Paints the timeline markers at the top of the screen
	# -------------------------------------------------------------------

	def drawtimelinemarkers(self, currenttime):
	
		outcome = {}
	
		for hourindex in range(1, 14):

			for subindex in range(0, 4):
	
				# Position of marker
				pixelposition = self.calculatemarkerposition(currenttime, hourindex, subindex)
	
				# Only draw marker if it's to the right of the current time marker
				if self.startline < pixelposition:
					outcome["Timeline Line " + str(1000 + (hourindex * 10) + subindex)] = ("Line",
									Vector.createfromvalues(pixelposition, 0),
									Vector.createfromvalues(pixelposition, self.calculatemarkerlineheight(subindex)),
									"Grey", 1, "")

		return outcome


	# -------------------------------------------------------------------
	# Paints the desired temperature at the top of the screen
	# -------------------------------------------------------------------

	def drawdesiredtemperature(self, desiredtemperature):

		outcome = {}

		self.desiredtemperature.updatevalue(desiredtemperature)

		displayedtemperature, transitionfraction, position, colour = self.calculatedesiredtempmetrics(self.desiredtemperature)

		outcome["Desired Temp"] = ("Text", str(displayedtemperature), position, "Right", colour, "Desired Temp")

		outcome["Desired Temp Screen Background"] = ("Box", self.backgroundstart, self.backgroundend, "Black", "", 0)

		return outcome
