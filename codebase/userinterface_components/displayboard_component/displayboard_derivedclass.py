from ...common_components.vector_datatype import vector_module as Vector
from .. import display_sharedfunctions as DisplayFunction
from . import boardmetrics_baseclass as Metrics
from . flame_subcomponent import flame_module as Flame



class DefineBoard(Metrics.DefineBoardMetrics):

	def __init__(self):

		# Get the metrics using baseclass method
		Metrics.DefineBoardMetrics.__init__(self)

		# Data for capturing the animation of the current temperature
		self.flame = Flame.createflame()

		# The current runway display definition
		self.artefacts = {}


	# -------------------------------------------------------------------
	# Build the Board
	# -------------------------------------------------------------------

	def buildboard(self, boilercontroller):

		self.artefacts = {}

		# Update the animation stats
		self.flame.updateflame(boilercontroller.getboilerswitchstatus(), boilercontroller.getthermostatstatus())

		# Display current measured temperature
		newitems = self.drawcurrenttemperature(boilercontroller.getcurrentmeasuredtemperature())
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Board A"))

		# Display flame
		newitems = self.drawflame(boilercontroller.getboilerswitchbufferstate())
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Board B"))

		return self.artefacts



	def drawcurrenttemperature(self, currenttemperature):

		outcome = {}

		integerpart, fractionpart, colour, currentposition = self.calculatetemperaturemetrics(currenttemperature,
																				self.flame.gettransitionfraction())

		# Draw current temperature
		outcome["Current Temp Integer"] = ("Text", str(integerpart), currentposition, "Right", colour, "Actual Temp")
		outcome["Current Temp Fraction"] = ("Text", (str(fractionpart))[1:3], currentposition, "Left", colour, "Actual Temp")
		outcome["Current Temp Degree"] = ("Text", "O", Vector.add(currentposition, self.degreesoffset), "Left", colour, "Timeline Hours")
		outcome["Current Temp Celcius"] = ("Text", "C", Vector.add(currentposition, self.celciusoffset), "Left", colour, "Timeline Temps")

		return outcome



	def drawflame(self, snoozetimer):

		outcome = {}

		mainimage = "None"
		overlayimage = False


		if self.flame.getflamestate("Hidden") == False:
			mainimage = "flame_base"
			if self.flame.getflamestate("Snooze") == True:
				mainimage = "flame_disable"
				overlayimage = True
#			elif self.flame.getflamestate("On") == True:
#?				for flameversion in range(1,5):
#?					framename, flameframe = self.getflameframe(flameversion)
#?					if flameframe != "":
#?						outcome[framename] = ("Image", flameframe, self.flameposition)
#			elif self.flame.getflamestate("Transitioning") == True:
#				mainimage = self.getflametransition()
			elif self.flame.getflamestate("Forced") == True:
#?				outcome["Flame 1"] = ("Image", self.getflameframe(999), self.flameposition)
				overlayimage = True

		if mainimage != "None":
			outcome["Flame Image 1"] = ("Image", mainimage, self.flameposition)
		if overlayimage == True:
			outcome["Flame Overlay Clock"] = ("Image", "flame_snooze", self.flameposition)
			if snoozetimer > 0:
				outcome["Flame Overlay Text"] = ("Text", str(snoozetimer), self.snoozeoffset, "Centre", "Snooze", "Snooze")

		return outcome




