from ...common_components.vector_datatype import vector_module as Vector
from ...common_components.clock_datatype import clock_module as Clock
from ...common_components.transition_datatype import transition_module as Transition
from .. import display_privatefunctions as DisplayFunction


class DefineRunway:

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

		# Data for capturing the animation of the desired temperature
		self.desiredtemperature = Transition.createoldnewtransition(500, 1000, 0)

		# Dimensions of blanking out background for desired temperature
		self.backgroundstart = Vector.createfromvalues(self.startline, 0)
		self.backgroundend = Vector.createfromvalues(self.startline * 2, self.height)


	def getinstructionposition(self, scheduledtime, currenttime):

		outcome = {}

		# Position of marker
		houroffset = Clock.getfuturetimevalue(scheduledtime.getvalue(), currenttime.getvalue()) - (3600 * currenttime.gethour())
		pixelposition = self.startline + int(houroffset * self.timescale / 3600) - self.calculatemarkeroffsets(currenttime)

		# Draw marker & Temp
		outcome["Marker Top"] = Vector.createfromvalues(pixelposition, 18)
		outcome["Marker Bottom"] = Vector.createfromvalues(pixelposition, self.height)
		outcome["Marker Text"] = Vector.createfromvalues(pixelposition + 3, self.height - 29)

		return outcome




	# -------------------------------------------------------------------
	# Paints the scheduled settings at the top of the screen
	# -------------------------------------------------------------------

	def drawinstructions(self, currenttime, schedule):

		outcome = {}

		# Get list of scheduled times
		scheduledtimes = schedule.getscheduledtimes()

		index = 0

		# Loop over scheduled times
		for scheduledtime in scheduledtimes:

			# Get position of marker & text
			positioning = self.getinstructionposition(scheduledtime, currenttime)

			# Draw marker
			outcome[index] = ("Line", positioning["Marker Top"], positioning["Marker Bottom"], "Grey", 1, "")

			# Get desired temperature
			temperature = schedule.getscheduledinstruction(scheduledtime)

			# Draw desired temperature number
			outcome[index + 1] = ("Text", str(temperature), positioning["Marker Text"], "Left",
													DisplayFunction.gettemperaturecolour(temperature), "Timeline Temps")

			index = index + 3

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
				outcome[hourindex] = ("Text", Clock.convert24hourtohuman(hourindex + lasthour),
										Vector.createfromvalues(hourmarker + 3, 1), "Left", "Grey", "Timeline Hours")

		outcome["Zero"] = ("Line", self.backgroundstart,
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
					outcome[(hourindex * 10) + subindex] = ("Line", Vector.createfromvalues(pixelposition, 0),
															Vector.createfromvalues(pixelposition,
															self.calculatemarkerlineheight(subindex)), "Grey", 1, "")

		return outcome


	# -------------------------------------------------------------------
	# Paints the desired temperature at the top of the screen
	# -------------------------------------------------------------------

	def drawdesiredtemperature(self, desiredtemperature):

		outcome = {}

		self.desiredtemperature.updatevalue(desiredtemperature)

		displayedtemperature, transitionfraction, position, colour = self.calculatedesiredtempmetrics()

		outcome["Desired Temp"] = ("Text", str(displayedtemperature), position, "Right",
																								colour, "Desired Temp")

		outcome["Screen Background"] = ("Box", self.backgroundstart, self.backgroundend, "Black", "", 0)

		return outcome



	def calculatemarkeroffsets(self, currenttime):

		# Number of pixels markers are shifted left
		return int(self.timescale * ((currenttime.getminute() * 60) + currenttime.getsecond()) / 3600)



	def calculatemarkerlineheight(self, subindex):

		if subindex == 0:
			return self.hourbottom
		else:
			return  (3 * (subindex + 1) % 2)



	def calculatedesiredtempmetrics(self):

		displayedtemperature = self.desiredtemperature.getswitchedvalue()

		transitionfraction = self.desiredtemperature.gettransitionfraction()

		positionalong = DisplayFunction.getonewaytransitionposition(self.startline - 5, self.startline, transitionfraction)
		position = Vector.createfromvalues(positionalong, -3)

		colour = DisplayFunction.gettransitioncolour(displayedtemperature, transitionfraction)

		return displayedtemperature, transitionfraction, position, colour



	def calculatemarkerposition(self, currenttime, hourindex, subindex):

		hourmarker = self.startline + (hourindex * self.timescale) - self.calculatemarkeroffsets(currenttime)

		if subindex > 0:
			return (hourmarker - int(subindex * self.timescale / 4))
		else:
			return hourmarker
